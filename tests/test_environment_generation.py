import filecmp
import pathlib
import pytest


def test_conda_env_matches_saved():
    """
    Test that conda_environment.yaml and environment.yaml are identical after generation.
    """
    # Adjust paths if needed
    conda_env = pathlib.Path("conda_environment.yaml")
    saved_env = pathlib.Path("environment.yaml")
    assert conda_env.exists(), f"Missing: {conda_env}"
    assert saved_env.exists(), f"Missing: {saved_env}"
    # Compare files
    assert filecmp.cmp(conda_env, saved_env, shallow=False), (
        f"{conda_env} and {saved_env} differ!"
    )
