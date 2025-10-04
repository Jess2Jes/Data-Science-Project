English | | [Bahasa Indonesia](READMEid.md) | [中文](READMECN.md)
# TaskMaster CLI: Python Task Management System

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

A comprehensive, command-line based task management application built with Python. This tool allows users to efficiently add, track, filter, and manage their daily tasks and schedules directly from the terminal. Designed as a school project, it demonstrates core programming concepts including data manipulation, modular design, and user-friendly command-line interaction.

## ✨ Key Features

-   **Full CRUD Functionality**: Add, view, update, and delete tasks with ease.
-   **Advanced Filtering**: Dynamically filter tasks by **status** (`Pending`, `In Progress`, `Completed`), **priority** (`High`, `Medium`, `Low`), or **deadline**.
-   **Smart Sorting**: Automatically sort tasks chronologically to keep your schedule organized.
-   **Task Prioritization**: Instantly view the "Top 3 Most Important Tasks" based on a combination of priority and upcoming deadlines.
-   **Dynamic Search**: Quickly find any task by its name.
-   **Statistical Reporting**: Generate a detailed report including total tasks, status breakdowns, and user assignments.
-   **User-Friendly Interface**: A simple and intuitive menu-driven interface for seamless navigation.
-   **Dynamic Table Formatting**: Task lists are displayed in neatly formatted tables that adjust to the content length.

## 📸 Demo

Here's a quick look at the main menu and the formatted task list output:

**Main Menu:**
```
────────────────────Menu────────────────────
1. Tambah Task
2. Daftar Task
3. Cari Task
4. Sortir Task
5. Laporan Statistik
6. Filter
7. Keluar
────────────────────────────────────────────
Pilihan : 2
```

**Sample Output (`Daftar Task`):**
```
──────────────────────────────────────────────────────────────────────────────────────────
                                       Semua Task
──────────────────────────────────────────────────────────────────────────────────────────
ID │ Task                      │ Deadline            │ Priority │ Status
──────────────────────────────────────────────────────────────────────────────────────────
1  │ Kerjakan Tugas Basis Data │ 2025-10-05 13:00 PM │ High     │ Pending
2  │ Belajar Algoritma         │ 2025-10-06 12:57 PM │ Medium   │ In Progress
3  │ Buat Slide Presentasi     │ 2025-10-08 16:49 PM │ High     │ Completed
4  │ Rapat Tim                 │ 2025-10-04 15:00 PM │ Low      │ Completed
5  │ Kerjakan Tugas PBO        │ 2025-10-04 15:00 PM │ High     │ Completed
──────────────────────────────────────────────────────────────────────────────────────────
```

## 📂 Project Structure

The project is organized into modular files for better readability and maintenance. It is recommended to place the helper scripts inside a `helpers` directory.

```
your-project-name/
├── main.py                     # Main entry point of the application
└── helpers/
    ├── __init__.py
    ├── addData.py              # Handles logic for adding new tasks
    ├── dataFilters.py          # Functions for filtering, sorting, and displaying tasks
    ├── searchUpdateTask.py     # Manages searching and updating existing tasks
    ├── deleteTask.py           # Logic for deleting tasks
    ├── sortTask.py             # Core sorting logic for tasks
    └── reportStats.py          # Generates and prints task statistics
```
*Note: The original file names like `Program Pencarian & Perubahan Data.py` have been renamed to `searchUpdateTask.py` in this structure for standard Python naming conventions.*

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.8 or higher

### Installation & Running

1.  **Clone the repository (or download the files):**
    ```sh
    git clone [https://github.com/Dendroculus/your-repo-name.git](https://github.com/Dendroculus/your-repo-name.git)
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd your-repo-name
    ```
3.  **Run the application:**
    ```sh
    python main.py
    ```
    The application will start, and you can navigate through the features using the on-screen menu.

## 🛠️ Code Modules Overview

-   **`main.py`**: The main driver of the application. It displays the primary menu and handles user input to navigate to different functionalities like adding, filtering, or viewing tasks.
-   **`helpers/addData.py`**: Contains the `tambah_task` function. It prompts the user for task details (name, deadline, priority, status), validates the input, and appends the new task to the list.
-   **`helpers/dataFilters.py`**: A core module that includes functions to:
    -   Filter tasks by deadline (`filter_by_deadline`), priority (`filter_by_priority`), and status (`filter_by_status`).
    -   Identify and return the most important tasks (`get_top_tasks`).
    -   Display tasks in a clean, dynamically sized table (`data_task`).
-   **`helpers/searchUpdateTask.py`**: Implements the search functionality to find a task by its name and provides an interface to update its details.
-   **`helpers/deleteTask.py`**: Provides the logic to find and remove a specific task from the data list.
-   **`helpers/sortTask.py`**: Contains the logic for sorting the list of tasks, primarily based on their deadlines.
-   **`helpers/reportStats.py`**: Calculates and prints a summary report, including task counts by status, category, and user.

## 👤 Contributors

<table border="0" cellspacing="10" cellpadding="5">
  <tr>
    <td align="center" style="border: 1px solid #555; padding: 10px;">
      <a href="https://github.com/Jess2Jes">
        <img src="https://github.com/Jess2Jes.png" width="100" height="100" alt="Jess2Jes" style="border-radius: 50%;"/>
      </a>
      <br/>
      <a href="https://github.com/Jess2Jes">Jess2Jes</a>
    </td>
    <td align="center" style="border: 1px solid #555; padding: 10px;">
      <a href="https://github.com/Dendroculus">
        <img src="https://github.com/Dendroculus.png" width="100" height="100" alt="Hans 展豪" style="border-radius: 50%;"/>
      </a>
      <br/>
      <a href="https://github.com/Dendroculus">Hans 展豪</a>
    </td>
    <td align="center" style="border: 1px solid #555; padding: 10px;">
      <a href="https://github.com/Solynixx">
        <img src="https://github.com/Solynixx.png" width="100" height="100" alt="Solynixx" style="border-radius: 50%;"/>
      </a>
      <br/>
      <a href="https://github.com/Solynixx">Solynixx</a>
    </td>
    <td align="center" style="border: 1px solid #555; padding: 10px;">
      <a href="https://github.com/StevNard">
        <img src="https://github.com/StevNard.png" width="100" height="100" alt="StevNard" style="border-radius: 50%;"/>
      </a>
      <br/>
      <a href="https://github.com/StevNard">StevNard</a>
    </td>
    <td align="center" style="border: 1px solid #555; padding: 10px;">
      <a href="https://github.com/Milkdrinker-creator">
        <img src="https://github.com/Milkdrinker-creator.png" width="100" height="100" alt="Milkdrinker-creator" style="border-radius: 50%;"/>
      </a>
      <br/>
      <a href="https://github.com/Milkdrinker-creator">Milkdrinker-creator</a>
    </td>
    
  </tr>
</table>

