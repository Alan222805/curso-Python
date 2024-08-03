from pathlib import Path, PureWindowsPath

carpeta = Path("C:/Users/Alanj/OneDrive/Escritorio/alternativo/Otro_archiv.txt")
ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)

""" if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe") """