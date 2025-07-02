# AI-Lab2-RoshanShrestha-021368

# 🔍 Heuristic Search Algorithms

This repository contains Python implementations of two classic heuristic search problems:

1. **8-Puzzle Problem** using **Breadth-First Search (BFS)** with Manhattan distance as a heuristic.
2. **Block Arrangement Problem** using **Hill Climbing** algorithm with misplaced block heuristic.

---

## 📌 Contents

- `eight_puzzle_bfs.py` - Solves the 8-puzzle problem using BFS.
- `block_arrangement_hill_climb.py` - Solves the block arrangement problem using Hill Climbing.
- `README.md` - This documentation.

---

## 1️⃣ 8-Puzzle Problem (BFS with Manhattan Heuristic)

### 🧩 Problem Description
A 3x3 puzzle board with tiles numbered 1–8 and one blank tile (0). The goal is to reach the state:

- 1 2 3
- 4 5 6
- 7 8 0

### 📈 Heuristic Used
- **Manhattan Distance**: Sum of the distances each tile is from its goal position.

### 🛠 Features
- Accepts any solvable initial state.
- Explores states using BFS.
- Prints heuristic values of each explored state.
- Shows the sequence of moves to reach the goal.

---

## 2️⃣ Block Arrangement Problem (Hill Climbing)

### 📦 Problem Description
Arrange four labeled blocks `[A, B, C, D]` in correct order using swap of adjacent elements. For example:

Initial: `[C, A, D, B]` → Goal: `[A, B, C, D]`

### 📈 Heuristic Used
- **Number of misplaced blocks** compared to the goal state.

### 🛠 Features
- Implements simple Hill Climbing.
- Detects if algorithm gets stuck in local maximum.
- Shows the moves taken and current heuristic at each step.

---

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.x

### ▶️ Running the Programs

To run the 8-puzzle problem:
```bash
python eight_puzzle_bfs.py
python block_arrangement_hill_climb.py
