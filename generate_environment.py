"""
    Development Notes:
    Generally trying keep pure python projects simple and avoid conda environments.
    This script generates a conda environment file from pyproject.toml.
    Thus, this environment file is intended for use with conda and maybe no bueno with venv.

"""
from typing import Optional, Union
import toml
import yaml

def generate_environment(python_version: Optional[Union[str, float]]):
    with open("pyproject.toml", "r") as f:
        pyproject = toml.load(f)

    dependencies = pyproject["project"]["dependencies"]
    dev_dependencies = pyproject["project"].get("optional-dependencies", {}).get("dev", [])

    conda_env = {
        "name": "templates",
        "channels": ["anaconda", "conda-forge", "defaults"],
        "dependencies": [
            f"python={python_version}" if python_version else None,
            {"pip": dependencies + dev_dependencies},
        ],
    }

    # Remove None values from dependencies
    conda_env["dependencies"] = [dep for dep in conda_env["dependencies"] if dep is not None]

    out_file = f"conda_environment-{python_version}.yaml" if python_version else "conda_environment.yaml"
    with open(out_file, "w") as f:
        f.write("# Generated conda environment file\n")
        if python_version:
            f.write(f"# Python version: {python_version}\n")
        f.write(f"name: {conda_env['name']}\n")
        if conda_env["channels"]:
            f.write("channels:\n")
            for ch in conda_env["channels"]:
                f.write(f"- {ch}\n")

        f.write("dependencies:\n")
        for dep in conda_env["dependencies"]:
            if isinstance(dep, str):
                f.write(f"- {dep}\n")
            elif isinstance(dep, dict) and "pip" in dep:
                f.write("- pip:\n")
                for pip_dep in dependencies:
                    f.write(f"  - {pip_dep}\n")
                # f.write("  # Development dependencies\n")
                for pip_dev_dep in dev_dependencies:
                    f.write(f"  - {pip_dev_dep}\n")
        f.write("# note the restart of the alphabetization in pip depenndecies is where dev starts\n")
if __name__ == "__main__":
    python_versions = [None, "3.9", "3.10", "3.11", "3.12", "3.13"]
    for version in python_versions:
        generate_environment(version)
