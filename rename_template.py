# rename_template.py tool to rename 'template' to custom repo name

import os
import shutil
from typing import Optional

def replace_in_file(file_path: str, old: str, new: str) -> None:
    """Replace all instances of 'old' with 'new' in the given file."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        lines: list[str] = f.readlines()

    updated: list[str] = [line.replace(old, new) for line in lines]

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(updated)

    print(f"Updated: {file_path}")

def rename_template_to_new(project_name: str) -> None:
    """Rename all instances of 'template' to the given project name across key files and directories."""
    print(f"Renaming 'template' to: '{project_name}'")

    # 1. environment.yaml
    replace_in_file("environment.yaml", "template", project_name)

    # 2. Rename src/template → src/{project_name}
    old_src_dir: str = os.path.join("src", "template")
    new_src_dir: str = os.path.join("src", project_name)

    if os.path.exists(old_src_dir):
        shutil.move(old_src_dir, new_src_dir)
        print(f"Renamed folder: {old_src_dir} -> {new_src_dir}")
    else:
        print(f"Folder not found: {old_src_dir}")

    # 3. pyproject.toml
    pyproject_file: str = "pyproject.toml"
    replace_in_file(pyproject_file, 'name = "template"', f'name = "{project_name}"')
    replace_in_file(pyproject_file, 'Tools for working with template data', f'Tools for working with {project_name} data')
    replace_in_file(pyproject_file, 'keywords = ["template", ]', f'keywords = ["{project_name}", ]')
    replace_in_file(pyproject_file, 'https://github.com/kkappler/template.git', f'https://github.com/kkappler/{project_name}.git')
    replace_in_file(pyproject_file, 'https://github.com/kkappler/template/issues', f'https://github.com/kkappler/{project_name}/issues')

    # 4. test_helper_functions.py
    test_file: str = os.path.join("test", "util", "test_helper_functions.py")
    replace_in_file(test_file, "template.util.helper_functions", f"{project_name}.util.helper_functions")

    # 5. README.md
    readme_file: str = "README.md"
    replace_in_file(readme_file, "template", project_name)

    print("All references updated.")

if __name__ == "__main__":
    new_name: Optional[str] = input("Enter new repo/project name: ").strip()
    if new_name:
        rename_template_to_new(new_name)
    else:
        print("No project name entered. Aborting.")
