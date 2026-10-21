"""Task class - holds the data of a single task."""

from datetime import datetime, timezone


class Task:
    """Represent a single task."""

    def __init__(
        self,
        task_id: int,
        title: str,
        is_done: bool = False,
        created_at: str | None = None,
    ):
        if not isinstance(task_id, int) or isinstance(task_id, bool):
            raise TypeError("task_id must be an integer.")

        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a non-empty string.")

        if not isinstance(is_done, bool):
            raise TypeError("is_done must be a boolean.")

        self.id = task_id
        self.title = title.strip()
        self.is_done = is_done

        if created_at is None:
            self.created_at = datetime.now(timezone.utc).isoformat()
        elif isinstance(created_at, str) and created_at.strip():
            self.created_at = created_at
        else:
            raise ValueError("created_at must be a non-empty string.")
        

    def to_dict(self) -> dict:
        """Convert the task to a dictionary for JSON storage."""

        return {
            "id": self.id,
            "title": self.title,
            "is_done": self.is_done,
            "created_at": self.created_at,
        }
    

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Create a Task instance from a dictionary."""

        if not isinstance(data, dict):
            raise TypeError("Task data must be a dictionary.")

        return cls(
            task_id=data["id"],
            title=data["title"],
            is_done=data.get("is_done", False),
            created_at=data.get("created_at"),
        )


    def __repr__(self) -> str:
        """Return a developer-friendly representation of the task."""

        return (
            f"Task("
            f"id={self.id}, "
            f"title={self.title}, "
            f"is_done={self.is_done}, "
            f"created_at={self.created_at}"
            f")"
        )


