from pathlib import Path
from runner import run_mapdl

report = run_mapdl(
    input_apdl=Path("C:\\Users\\komle\\source\\PycharmProjects\\OptiSolver\\Resources\\APDL_template\\1.txt"),
    work_dir=Path("C:/Artem/output/sat-shell-001/work"),
    results_dir=Path("C:/Artem/output/sat-shell-001/results"),
    jobname="sat_shell_001",
)

print("Отчёт о запуске:")
print(report)