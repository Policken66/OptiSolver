import hashlib
import json
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from Preprocessor.config.loader import load_config
from Preprocessor.config.validator import validate_config
from Preprocessor.derive.calculator import compute
from Preprocessor.mapping.solver_params import build_solver_params
from Preprocessor.template.renderer import RenderReport, render_apdl
from Preprocessor.utils.normalaizer import to_si


@dataclass
class PreprocessResult:
    run_dir: Path
    input_apdl_path: Path
    solver_params_path: Path
    normalized_config_path: Path
    derived_params_path: Path
    run_manifest_path: Path
    validation_report_path: Path


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _write_json(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def run_preprocessor(
        path_to_config: Path,
        template_dir: Path,
        runs_root: Path,
        template_filename: str = "1.txt",
) -> PreprocessResult:
    """
    Сквозной запуск препроцессора в шаблонном режиме:
    1) загрузка + валидация
    2) нормализация (СИ)
    3) производные
    4) solver_params
    5) копия шаблона в папку прогона (snapshot) + подстановка -> input.apdl
    6) сохранение артефактов и манифеста
    :param path_to_config:
    :param template_dir:
    :param runs_root:
    :param template_filename:
    :return:
    """
    # 0) создаем папку прогона
    raw = load_config(path_to_config)
    cfg = validate_config(raw)
    cfg = to_si(cfg)
    drv = compute(cfg)
    params = build_solver_params(cfg, drv)

    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    project = cfg.metadata.project_name if hasattr(cfg, "metadata") else "project"
    run_dir = runs_root / f"{ts}_{project}"
    run_dir.mkdir(parents=True, exist_ok=True)

    # 1) сохраняем вход как есть
    raw_config_path = run_dir / "raw_config.json"
    _write_json(raw_config_path, raw)

    normalized_config_path = run_dir / "normalized_config.json"
    _write_json(normalized_config_path, json.loads(cfg.model_dump_json()))

    derived_params_path = run_dir / "derived_params.json"
    _write_json(derived_params_path, drv)

    solver_params_path = run_dir / "solver_params.json"
    _write_json(solver_params_path, params)

    # 2) снимок шаблона
    src_template_path = template_dir / template_filename
    snapshot_dir = run_dir / "template_snapshot"
    snapshot_dir.mkdir(exist_ok=True)
    snapshot_template_path = snapshot_dir / template_filename
    shutil.copy2(src_template_path, snapshot_template_path)

    # 3) рендерим input.apdl
    input_apdl_path = run_dir / "input.apdl"
    report: RenderReport = render_apdl(snapshot_template_path, params, input_apdl_path)

    # 4) манифест (минимально необходимое)
    manifest = {
        "run_id": run_dir.name,
        "project_name": project,
        "timestamp": ts,
        "template_file": str(src_template_path),
    }
    run_manifest_path = run_dir / "run_manifest.json"
    _write_json(run_manifest_path, manifest)

    # 5) отчет о валидации (пустой, раз валидатор не упал)
    validation_report_path = run_dir / "validation_report.txt"
    validation_report_path.write_text("OK: validation passed\n", encoding="utf-8")

    return PreprocessResult(
        run_dir=run_dir,
        input_apdl_path=input_apdl_path,
        solver_params_path=solver_params_path,
        normalized_config_path=normalized_config_path,
        derived_params_path=derived_params_path,
        run_manifest_path=run_manifest_path,
        validation_report_path=validation_report_path,
    )
