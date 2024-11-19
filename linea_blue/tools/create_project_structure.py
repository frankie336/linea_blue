import os

def create_project_structure(project_name):
    # Define the folder structure
    folders = [
        f"{project_name}/plans",
        f"{project_name}/plans/sections",
        f"{project_name}/models",
        f"{project_name}/models/renders",
        f"{project_name}/budget",
        f"{project_name}/docs",
        f"{project_name}/photos",
        f"{project_name}/photos/design_references",
        f"{project_name}/photos/progress_updates"
    ]

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    # Create placeholder files
    files = {
        f"{project_name}/plans/floor_plan.pdf": "Placeholder for floor plan PDF.",
        f"{project_name}/plans/roof_plan.pdf": "Placeholder for roof plan PDF.",
        f"{project_name}/plans/sections/ground_section.pdf": "Placeholder for ground section PDF.",
        f"{project_name}/models/3d_model.skp": "Placeholder for SketchUp model.",
        f"{project_name}/budget/materials_cost.xlsx": "Placeholder for materials cost spreadsheet.",
        f"{project_name}/budget/labor_cost.xlsx": "Placeholder for labor cost spreadsheet.",
        f"{project_name}/docs/README.md": "# Project Documentation\n\nAdd details about the project here.",
        f"{project_name}/docs/license_agreement.pdf": "Placeholder for license agreement.",
        f"{project_name}/photos/site_preparation.jpg": "Placeholder for site preparation photo.",
        f"{project_name}/photos/foundation_pour.jpg": "Placeholder for foundation pour photo.",
        f"{project_name}/photos/design_references/paperhouses_example.jpg": "Placeholder for PaperHouses example photo."
    }

    for file_path, content in files.items():
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    # Set your project name
    project_name = "linea_blue"  # Change this to your preferred project name
    create_project_structure(project_name)
