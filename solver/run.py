from pathlib import Path
from runner import run_mapdl

report = run_mapdl(
    input_apdl=Path("C:\\Users\\komle\\source\\PycharmProjects\\OptiSolver\\runs\\input.apdl"),
    work_dir=Path("C:/Artem/output/sat-shell-001/work"),
    results_dir=Path("C:/Artem/output/sat-shell-001/results"),
    #mapdl_exec="C:/Program Files/ANSYS Inc/v232/ansys/bin/winx64/ANSYS232.exe",  # твой путь к MAPDL
    jobname="sat_shell_001",
)

print("Отчёт о запуске:")
print(report)

