import os

# Define file renaming dictionary
file_rename_map = {
    "FACADE_EAST.jpg": "FACHADA_ESTE.jpg",
    "FACADE_NORTH.jpg": "FACHADA_NORTE.jpg",
    "FACADE_SOUTH.jpg": "FACHADA_SUR.jpg",
    "FACADE_WEST.jpg": "FACHADA_OESTE.jpg",
    "LEVEL_00.jpg": "PLANTA_BAJA.jpg",
    "ROOF.jpg": "TECHO.jpg",
    "SITEPLAN.jpg": "PLANO_DE_SITIO.jpg"
}

# Rename files
for old_name, new_name in file_rename_map.items():
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed: {old_name} → {new_name}")
    else:
        print(f"File not found: {old_name}")
