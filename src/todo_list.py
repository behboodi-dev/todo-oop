
"""TodoList class - manages a collection of tasks."""

from src.task import Task
from src.storage import load_tasks, save_tasks


class TodoList:
    """Manages a list of tasks with add, delete, done, edit, and list actions."""

    def __init__(self):
        """Initialize the task list by loading from storage."""

        raw_data = load_tasks()
        self.tasks: list[Task] = [
            Task.from_dict(item) for item in raw_data
        ]

    def _save(self) -> None:
        """Helper method to save the current tasks to storage."""

        raw_data = [task.to_dict() for task in self.tasks]
        save_tasks(raw_data)

    def add(self, title: str) -> Task:
        """Create a new task and add it to the list."""

        if self.tasks:
            new_id = max(task.id for task in self.tasks) + 1
        else:
            new_id = 1

        new_task = Task(task_id=new_id, title=title)
        self.tasks.append(new_task)

        self._save()
        return new_task

    def list_tasks(self) -> list[Task]:
        """Return a copy of the task list."""

        return self.tasks.copy()

    def find_task(self, task_id: int) -> Task | None:
        """Find a task by its ID. Return None if not found."""

        for task in self.tasks:
            if task.id == task_id:
                return task

        return None

    def done(self, task_id: int) -> bool:
        """Mark a task as done. Return True if successful."""

        task = self.find_task(task_id)

        if task is not None:
            task.is_done = True
            self._save()
            return True

        return False

    def edit(
        self,
        task_id: int,
        new_title: str | None = None,
        is_done: bool | None = None,
    ) -> bool:
        """Edit a task's title and/or completion status."""

        task = self.find_task(task_id)

        if task is None:
            return False

        if new_title is not None:
            if not isinstance(new_title, str) or not new_title.strip():
                raise ValueError("Task title cannot be empty.")

            task.title = new_title.strip()

        if is_done is not None:
            if not isinstance(is_done, bool):
                raise TypeError("is_done must be a boolean.")

            task.is_done = is_done

        self._save()
        return True

    def delete(self, task_id: int) -> bool:
        """Delete a task by its ID. Return True if successful."""

        task = self.find_task(task_id)

        if task is not None:
            self.tasks.remove(task)
            self._save()
            return True

        return False


