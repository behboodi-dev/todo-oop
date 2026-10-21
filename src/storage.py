
"""Storage module - handles reading and writing tasks to a JSON file."""

import json
import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

TASKS_FILE = Path(os.getenv("TASKS_FILE", "data/tasks.json"))


def load_tasks() -> list[dict]:
    """Load tasks from JSON. Return an empty list if the file is missing or invalid."""
    
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

    except json.JSONDecodeError as exc:
        print(f"Warning: The tasks file contains invalid JSON: {exc}")
        return []

    except OSError as exc:
        print(f"Warning: Could not read the tasks file: {exc}")
        return []

    if not isinstance(data, list):
        print("Warning: The tasks file must contain a JSON list.")
        return []

    if not all(isinstance(task, dict) for task in data):
        print("Warning: The tasks file contains invalid task entries.")
        return []

    return data


def save_tasks(tasks: list[dict]) -> None:
    """Save tasks to the JSON file."""

    if not isinstance(tasks, list):
        raise TypeError("tasks must be a list.")

    if not all(isinstance(task, dict) for task in tasks):
        raise TypeError("Every task must be a dictionary.")

    try:
        TASKS_FILE.parent.mkdir(parents=True, exist_ok=True)

        with TASKS_FILE.open("w", encoding="utf-8") as file:
            json.dump(
                tasks,
                file,
                indent=4,
                ensure_ascii=False,
            )

    except OSError as exc:
        raise OSError(
            f"Could not save tasks to '{TASKS_FILE}'."
        ) from exc
