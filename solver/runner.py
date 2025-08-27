import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

from ansys.mapdl.core import launch_mapdl


class SolverRunError(Exception):
    """Ошибка запуска MAPDL."""


def run_mapdl(
    input_apdl: Path,
    work_dir: Path,
    results_dir: Path,
    mapdl_exec: str | None = None,
    jobname: str = "job",
    timeout_sec: int = 7200,
) -> Dict[str, Any]:
    """
    Запускает MAPDL в минимальном режиме интеграции: подаёт input.apdl и сохраняет результаты.

    :param input_apdl: Путь к входному APDL-файлу.
    :param work_dir: Рабочая директория для MAPDL.
    :param results_dir: Папка для выходных файлов.
    :param mapdl_exec: Путь к исполняемому файлу MAPDL (если None, используется автопоиск).
    :param jobname: Имя задания MAPDL (используется в названиях файлов).
    :param timeout_sec: Ограничение по времени работы (секунды).
    :return: Словарь с отчётом о запуске.
    """
    work_dir = Path(work_dir).resolve()
    results_dir = Path(results_dir).resolve()
    input_apdl = Path(input_apdl).resolve()

    if not input_apdl.exists():
        raise SolverRunError(f"Входной файл не найден: {input_apdl}")

    work_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)

    # Копируем input.apdl в рабочую директорию
    local_input = work_dir / input_apdl.name
    shutil.copy2(input_apdl, local_input)

    # Запускаем MAPDL через PyMAPDL
    start = datetime.now()
    mapdl = launch_mapdl(
        run_location=str(work_dir),
        jobname=jobname,
    )
    try:
        mapdl.clear()
        mapdl.input(str(local_input))
        # ждём окончания работы
        mapdl.finish()
    except Exception as e:
        raise SolverRunError(f"Ошибка при выполнении MAPDL: {e}")
    finally:
        mapdl.exit()  # корректное завершение

    elapsed = (datetime.now() - start).total_seconds()

    # Сохраняем выходные файлы в results_dir
    produced_files = []
    for f in work_dir.iterdir():
        if f.suffix.lower() in (".out", ".rst", ".log", ".err"):
            target = results_dir / f.name
            shutil.copy2(f, target)
            produced_files.append(str(target))

    return {
        "jobname": jobname,
        "work_dir": str(work_dir),
        "results_dir": str(results_dir),
        "input_apdl": str(local_input),
        "elapsed_sec": elapsed,
        "produced_files": produced_files,
    }