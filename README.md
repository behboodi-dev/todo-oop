# Todo App — OOP Refactor

A command-line To-Do application built with Python. That is the **refactored version** of first To-Do app.
The goal of this project is to turn loose functions into **classes**, split the
code into **independent modules**, and store tasks in a **JSON** file — without
breaking the existing behavior of the app.

---

## Features

- ✅ **Object-Oriented Architecture** — `Task` (data) + `TodoList` (behavior)
- ✅ **Modular code** — each file has one responsibility
- ✅ **JSON storage** — each task is an object with `id`, `title`, `status`
- ✅ **Auto Task ID** — every new task gets a unique id (max existing id + 1)
- ✅ **Edit command** — change a task's title and/or status (`todo` / `done`)
- ✅ **Sort & filter by status (Bonus)** — todo first, done last
- ✅ **Graceful Fail** — the app never crashes on a missing or broken JSON file

---

## Project Goals

- Use **classes** to represent tasks (`Task`) and manage the task list (`TodoList`).
- Organize the application into **separate Python modules**.
- Store tasks in a **JSON file** so each task can hold more than just a title.
- Add, list, delete, and mark tasks as done.
- Assign a **unique ID** to every task automatically.
- **Edit** a task's title and status.
- Handle missing or invalid JSON data safely (**Graceful Fail**).
- **Bonus:** sort and filter tasks by status.