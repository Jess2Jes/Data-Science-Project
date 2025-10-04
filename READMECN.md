# TaskMaster CLI: Python 命令行任务管理系统

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

这是一款功能全面的、基于命令行的任务管理应用程序，使用 Python 构建。该工具允许用户直接在终端中高效地添加、跟踪、筛选和管理他们的日常任务与日程。作为一项学校项目，它展示了编程的核心概念，包括数据操作、模块化设计以及用户友好的命令行交互。

## ✨ 主要功能

-   **完整的 CRUD 功能**：轻松添加、查看、更新和删除任务。
-   **高级筛选**：根据**状态**（`待处理`、`进行中`、`已完成`）、**优先级**（`高`、`中`、`低`）或**截止日期**动态筛选任务。
-   **智能排序**：按时间顺序自动对任务进行排序，让您的日程安排井然有序。
-   **任务优先级排序**：根据优先级和截止日期的组合，即时查看“前 3 个最重要任务”。
-   **动态搜索**：通过任务名称快速找到任何任务。
-   **统计报告**：生成详细报告，包括任务总数、各状态分类统计以及用户分配情况。
-   **用户友好的界面**：一个简单直观的菜单驱动界面，可实现无缝导航。
-   **动态表格格式化**：任务列表以整洁的、可根据内容长度自动调整的表格形式显示。

## 📸 功能演示

以下是主菜单和格式化任务列表输出的快速预览：

**主菜单:**
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

**示例输出 (`Daftar Task`):**
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

## 📂 项目结构

该项目被组织成模块化文件，以提高可读性和可维护性。建议将辅助脚本放在 `helpers` 目录中。

```
your-project-name/
├── main.py                     # 应用程序的主入口点
└── helpers/
    ├── __init__.py
    ├── addData.py              # 处理添加新任务的逻辑
    ├── dataFilters.py          # 用于筛选、排序和显示任务的函数
    ├── searchUpdateTask.py     # 管理现有任务的搜索和更新
    ├── deleteTask.py           # 删除任务的逻辑
    ├── sortTask.py             # 核心的任务排序逻辑
    └── reportStats.py          # 生成并打印任务统计信息
```
*请注意：在此结构中，像 `Program Pencarian & Perubahan Data.py` 这样的原始文件名已被重命名为 `searchUpdateTask.py`，以遵循标准的 Python 命名约定。*

## 🚀 快速上手

请按照以下说明在您的本地计算机上获取并运行该项目。

### 环境要求

-   Python 3.8 或更高版本

### 安装与运行

1.  **克隆仓库（或下载文件）：**
    ```sh
    git clone [https://github.com/Dendroculus/your-repo-name.git](https://github.com/Dendroculus/your-repo-name.git)
    ```
2.  **进入项目目录：**
    ```sh
    cd your-repo-name
    ```
3.  **运行应用程序：**
    ```sh
    python main.py
    ```
    应用程序将启动，您可以通过屏幕上的菜单使用各项功能。

## 🛠️ 代码模块概览

-   **`main.py`**：应用程序的主要驱动程序。它显示主菜单并处理用户输入，以导航到不同的功能，如添加、筛选或查看任务。
-   **`helpers/addData.py`**：包含 `tambah_task` 函数。它会提示用户输入任务详细信息（名称、截止日期、优先级、状态），验证输入，并将新任务附加到列表中。
-   **`helpers/dataFilters.py`**：一个核心模块，包含以下函数：
    -   按截止日期 (`filter_by_deadline`)、优先级 (`filter_by_priority`) 和状态 (`filter_by_status`) 筛选任务。
    -   识别并返回最重要的任务 (`get_top_tasks`)。
    -   在干净、动态调整大小的表格中显示任务 (`data_task`)。
-   **`helpers/searchUpdateTask.py`**：实现搜索功能，通过任务名称查找任务，并提供更新其详细信息的界面。
-   **`helpers/deleteTask.py`**：提供从数据列表中查找并删除特定任务的逻辑。
-   **`helpers/sortTask.py`**：包含对任务列表进行排序的逻辑，主要基于它们的截止日期。
-   **`helpers/reportStats.py`**：计算并打印摘要报告，包括按状态、类别和用户统计的任务数量。

## 👤 贡献者

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

---
为学校作业而用心制作 ❤️