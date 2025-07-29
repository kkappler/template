# template

This is an example of a src/ structure repo.

Previously it used requirements-dev.txt but that has been deprecated and instead we can install the dev requirements from the pyproject.toml file.

To install the environment using Conda:
> conda env create --file environment.yaml
> conda activate template

# Make the enviroment available in Jupyter Lab
> python -m ipykernel install --user --name template

Because the environment will be in flux for sometime, we may need to periodically update.  Easier than deleteing and re-installing, you can 

> conda env update --name template --file environment.yaml

Optionally include `--prune` to remove anything not in the yaml:
> conda env update --name template --file environment.yaml --prune

# Add developer tools
# > pip install -r requirements-dev.txt # deprecated
> pip install -e ".dev"  # install from toml 

# Install the package
> pip install -e .

## venv Installation

To install the environment using venv:

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip
   ```

2. Install the package in editable mode:
   ```bash
   pip install -e .
   ```

3. Install developer dependencies:
   ```bash
   pip install -e .[dev]
   ```

4. (Optional) Generate the Conda environment file:
   ```bash
   python generate_environment.py
   ```

5. Run tests:
   ```bash
   pytest -s -v --cov=./ --cov-report=xml
   ```


