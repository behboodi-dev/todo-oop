"""TodoList class - manages a collection of tasks."""

from src.task import Task
from src.storage import load_tasks, save_tasks


class TodoList:
    """Manages a list of tasks with add, delete, done, and list actions."""

    def __init__(self):
        """Initialize the task list by loading from storage."""

        raw_data = load_tasks()
        self.tasks: list[Task] = [Task.from_dict(item) for item in raw_data]


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
        """Find a task by its ID. Returns None if not found."""

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

    def delete(self, task_id: int) -> bool:
        """Delete a task by its ID. Return True if successful."""
        task = self.find_task(task_id)

        if task is not None:
            self.tasks.remove(task)
            self._save()  
            return True

        return False


if __name__ == "__main__":
    todo = TodoList()
    
    t1 = todo.add("Learn OOP")
    t2 = todo.add("Write README")
    
    print("All tasks:", todo.tasks)
    
    print("Marking task 1 as done:", todo.done(1))
    print("Deleting task 2:", todo.delete(2))
    
    print("Remaining tasks:", todo.tasks)