import hashlib
import json
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from preprocessor.config.loader import load_config
from preprocessor.config.validator import validate_config
from preprocessor.derive.calculator import compute
from preprocessor.mapping.solver_params import build_solver_params
from preprocessor.template.renderer import RenderReport, render_apdl
from preprocessor.utils.normalaizer import to_si


@dataclass
class PreprocessResult:
    run_dir: Path
    input_apdl_path: Path
    snapshot_template_path: Path
    solver_params_path: Path
    normalized_config_path: Path
    derived_params_path: Path
    run_manifest_path: Path


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _write_json(path: Path, obj: Any) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def run_preprocessor(
        config_path: Path,
        template_path: Path,
        runs_root: Path,
        output_name: str = "input.apdl",
) -> PreprocessResult:
    """Сквозной запуск препроцессора (шаблонный режим)."""
    # 1) загрузка + валидация + приведение к СИ
    raw = load_config(config_path)
    cfg = validate_config(raw)
    cfg = to_si(cfg)

    # 2) производные + плоская карта
    drv = compute(cfg)
    params = build_solver_params(cfg, drv)

    # 3) создаем папку прогона
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    project = cfg.metadata.project_name
    run_dir = runs_root / f"{ts}_{project}"
    run_dir.mkdir(parents=True, exist_ok=True)

    # 4) сохраняем входы/вспомогательные файлы
    raw_config_path = run_dir / ("raw_config.yaml" if config_path.suffix.lower() in {".yaml", ".yml"} else "raw_config.json")
    raw_config_path.write_text(Path(config_path).read_text(encoding="utf-8"), encoding="utf-8")

    normalized_config_path = run_dir / "normalized_config.json"
    _write_json(normalized_config_path, json.loads(cfg.model_dump_json()))

    derived_params_path = run_dir / "derived_params.json"
    _write_json(derived_params_path, drv)

    solver_params_path = run_dir / "solver_params.json"
    _write_json(solver_params_path, params)

    # 5) снимок шаблона + рендер
    snapshot_dir = run_dir / "template_snapshot"
    snapshot_dir.mkdir(exist_ok=True)
    snapshot_template_path = snapshot_dir / Path(template_path).name
    shutil.copy2(template_path, snapshot_template_path)

    input_apdl_path = run_dir / output_name
    report: RenderReport = render_apdl(snapshot_template_path, params, input_apdl_path)

    # 6) манифест
    manifest = {
        "run_id": run_dir.name,
        "project_name": project,
        "timestamp": ts,
        "template_file": str(template_path),
        "template_sha256": _sha256_text(snapshot_template_path.read_text(encoding="utf-8")),
        "raw_config_sha256": _sha256_text(Path(config_path).read_text(encoding="utf-8")),
        "solver_params_sha256": _sha256_text(json.dumps(params, ensure_ascii=False, sort_keys=True)),
        "analyses": cfg.solver.analyses,
        "renderer": {"replaced": report.replaced, "inserted": report.inserted, "total_expected": report.total_expected},
        "paths": {"run_dir": str(run_dir), "input_apdl": str(input_apdl_path),
                  "snapshot_template": str(snapshot_template_path)}
    }
    run_manifest_path = run_dir / "run_manifest.json"
    _write_json(run_manifest_path, manifest)

    return PreprocessResult(
        run_dir=run_dir,
        input_apdl_path=input_apdl_path,
        snapshot_template_path=snapshot_template_path,
        solver_params_path=solver_params_path,
        normalized_config_path=normalized_config_path,
        derived_params_path=derived_params_path,
        run_manifest_path=run_manifest_path,
    )