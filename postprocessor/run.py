import numpy as np
from ansys.mapdl import reader as pymapdl_reader
from pathlib import Path

# путь к готовому rst-файлу
rst_path = Path(r"C:\Artem\output\sat-shell-001\results\sat_shell_001.rst")

# открываем результаты напрямую (без MAPDL)
result = pymapdl_reader.read_binary(str(rst_path))

# 1. Узнать какие результаты есть
print("Load steps:", result.nsets)
print("Time values:", result.time_values)

# 2. Собственные частоты (для модального анализа)
if hasattr(result, "modal_frequencies") and result.modal_frequencies is not None:
    print("Modal frequencies (Hz):", result.modal_frequencies)

# 3. Узловые перемещения (пример: первый набор результатов)
nnum, disp = result.nodal_displacement(0)   # step = 0
print("Макс. перемещение:", disp.max())

# 4. Узловые напряжения (пример: первый набор результатов)
nnum, stress = result.nodal_stress(0)
valid = np.nanmax(stress, axis=0)   # максимум по каждой компоненте
print("Макс. напряжение:", valid)
