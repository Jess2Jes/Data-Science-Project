[English](README.md) | [Bahasa Indonesia](READMEid.md) | 中文

# TaskMaster CLI: Python 命令行任务管理系统

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

这是一款功能全面的、基于命令行的任务管理应用程序，使用 Python 构建。该工具允许用户直接在终端中高效地添加、跟踪、筛选和管理他们的日常任务与日程。作为一项学校项目，它展示了编程的核心概念，包括数据操作、模块化设计以及用户友好的命令行交互。

## ✨ 主要功能

-   **完整的 CRUD 功能**：轻松添加、查看、更新和删除任务。
-   **高级排序**：按**截止日期**、**名称**、**优先级**或**状态**，以升序或降序对任务进行排序。
-   **智能筛选**：按不同的时间段（`今日`、`明日`、`本周`、`本月`）、优先级或状态动态筛选任务。
-   **任务优先级排序**：根据优先级和截止日期的组合，即时查看“前 3 个最重要任务”。
-   **快捷操作**：轻松将任务标记为“已完成”，或一次性删除所有已完成的任务。
-   **统计报告**：生成详细且格式精美的报告，包括任务总数、状态分类以及优先级统计。
-   **用户友好的界面**：一个简单直观的菜单驱动界面，可实现无缝导航。
-   **动态表格格式化**：任务列表以整洁的、可根据内容长度自动调整的表格形式显示。

## 📸 功能演示

以下是新版主菜单和格式化任务列表输出的快速预览：

**主菜单:**

<img src="assets/MENU_APPEARANCE.png" alt="Menu Appearance" width="300">


**示例输出 (`Daftar Task`):**
```
──────────────────────────────────────────────────────────────────────────────────
                                   Semua Task
──────────────────────────────────────────────────────────────────────────────────
ID │ Task                      │ Deadline              │ Priority │ Status
──────────────────────────────────────────────────────────────────────────────────
1  │ Kerjakan Tugas Basis Data │ 2025 05 October 13:00 │ High     │ Pending
2  │ Belajar Algoritma         │ 2025 06 October 12:57 │ Medium   │ In Progress
3  │ Buat Slide Presentasi     │ 2025 08 October 16:49 │ High     │ Completed
4  │ Rapat Tim                 │ 2025 04 October 15:00 │ Low      │ Completed
5  │ Kerjakan Tugas Pbo        │ 2025 04 October 15:00 │ High     │ Completed
──────────────────────────────────────────────────────────────────────────────────
```

## 📂 项目结构

该项目被组织成模块化文件，以提高可读性和可维护性。

```
your-project-name/
├── main.py                     # 应用程序的主入口点
└── helpers/
    ├── __init__.py
    ├── addData.py              # 处理添加新任务的逻辑
    ├── changeData.py           # 用于更新、删除和标记任务为完成的函数
    ├── dataFilters.py          # 用于筛选任务和显示数据表的函数
    ├── reports.py              # 生成并打印统计报告
    ├── search.py               # 实现任务搜索功能
    └── sorter.py               # 包含所有高级任务排序的函数
```

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

-   **`main.py`**：应用程序的主要驱动程序。它显示主菜单并处理用户输入，以调用辅助模块中的函数。
-   **`helpers/addData.py`**：包含 `tambah_task` 函数。它会提示用户输入任务详细信息，验证输入（例如，检查重复名称和有效日期），并将新任务添加到列表中。
-   **`helpers/changeData.py`**：一个用于修改任务的模块。它包括更新任务特定字段 (`ubah_task`)、删除特定任务 (`hapus_data`)、将任务标记为完成 (`selesaikan_task`) 以及清除所有已完成任务 (`hapus_task_selesai`) 的函数。
-   **`helpers/dataFilters.py`**：一个核心模块，包含按不同时间范围、优先级和状态筛选任务的函数。它还包含关键的 `data_task` 函数，用于在干净、动态调整大小的表格中显示所有数据。
-   **`helpers/reports.py`**：包含 `laporan_statistik` 函数，该函数以格式化的框计算并打印摘要报告。
-   **`helpers/search.py`**：实现 `cari_task` 功能，以根据关键字搜索和显示任务。
-   **`helpers/sorter.py`**：提供一套全面的排序函数。它可以按截止日期、名称、优先级或状态，以升序或降序对任务进行排序。

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
        <td align="center" style="border: 1px solid #555; padding: 10px;">
      <a href="https://github.com/Azelezasl">
        <img src="https://github.com/Azelezasl.png" width="100" height="100" alt="Azelezasl" style="border-radius: 50%;"/>
      </a>
      <br/>
      <a href="https://github.com/Azelezasl">Azelezasl</a>
    </td>
    
  </tr>
</table>