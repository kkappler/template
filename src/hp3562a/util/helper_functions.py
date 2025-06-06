"""
    This module contains various tools that we may need to import.
"""

import matplotlib
import subprocess


def set_matplotlib_backend(backend: str = "TkAgg"):
    """

    Parameters
    ----------
    backend: str
        Specify the matplotlib backend
        TkAgg
        wxAgg
        Qt5Agg
        Qt4Agg
        Read more here: https://matplotlib.org/stable/users/explain/figure/backends.html
        When a jupyter notebook is giving weird figure creation outside the notebook, set to "ipympl"

    Returns
    -------

    """

    try:
        matplotlib.use(backend)
    except ImportError:
        msg = f"couldnt use {backend} -- possibly running in headless mode"
        logger.debug(msg)


def execute_subprocess(cmd, **kwargs):
    """
    A wrapper for subprocess.call

    Parameters
    ----------
    cmd : string
        command as it would be typed in a terminal
    kwargs: denotes keyword arguments that would be passed to subprocess

    """
    # old version commented out
    # exit_status = subprocess.call([cmd], shell=True, **kwargs)
    # if exit_status != 0:
    #     raise Exception("Failed to execute \n {}".format(cmd))
    result = subprocess.check_output([cmd], shell=True, **kwargs)
    return result
