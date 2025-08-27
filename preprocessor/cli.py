import argparse
from pathlib import Path

from preprocessor.runner import run_preprocessor


def main():
    p = argparse.ArgumentParser(description="Опти-препроцессор: формирование input.apdl из конфига и шаблона.")
    p.add_argument("--config", "-c", required=True, help="Путь к конфигурации (YAML или JSON).")
    p.add_argument("--template", "-t", required=True, help="Путь к APDL-шаблону (например, templates/apdl/shell_v1/1.txt).")
    p.add_argument("--runs", "-r", required=True, help="Каталог, куда складывать результаты прогона (runs/).")
    p.add_argument("--output-name", default="input.apdl", help="Имя итогового файла для MAPDL (по умолчанию input.apdl).")
    args = p.parse_args()

    res = run_preprocessor(
        config_path=Path(args.config),
        template_path=Path(args.template),
        runs_root=Path(args.runs),
        output_name=args.output_name,
    )
    print("OK")
    print("Run dir:         ", res.run_dir)
    print("Input APDL:      ", res.input_apdl_path)
    print("Template snapshot:", res.snapshot_template_path)
    print("Solver params:   ", res.solver_params_path)
    print("Manifest:        ", res.run_manifest_path)

if __name__ == "__main__":
    main()