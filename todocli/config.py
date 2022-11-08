"""This module provides the To-DO configuration functionality."""

import configparser
from pathlib import Path
import typer
from todocli import (
    DB_WRITE_ERROR, DIR_ERROR, FILE_ERROR, SUCCESS, __app_name__
)

# path to the app's directory
CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
# path to the configuration file
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"


def init_app(db_path: str) -> int:
    """Initialize the application"""

    # Initialize the configuration file
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code

    # Initialize the database
    database_code = _create_database(db_path)
    if database_code != SUCCESS:
        return database_code

    return SUCCESS


def _init_config_file() -> int:
    """Create the configuration directory and the configuration file.

    Finally, this function returns the proper error codes if something
    wrong happens during the creation of the directory and file.

    It returns SUCCESS if everything goes okay."""

    # Create the configuration directory
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except OSError:
        return DIR_ERROR

    # Create the configuration file
    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        return FILE_ERROR

    return SUCCESS


def _create_database(db_path: str) -> int:
    """Create the to-do database.

    This function returns the appropriate error codes if something
    happens while creating the database.
    It returns SUCCESS if the process succeeds."""

    config_parser = configparser.ConfigParser()
    config_parser["General"] = {"database": db_path}
    try:
        with CONFIG_FILE_PATH.open(("w")) as file:
            config_parser.write(file)
    except OSError:
        return DB_WRITE_ERROR
    return SUCCESS
