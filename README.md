# CTRS Capstone Project

**Project Title:** CTRS - Cat Triage and Rescue System  
**Author:** Judilyn Lucena

## Overview
CTRS is a Python capstone project that models a small cat rescue operation. The program demonstrates how core data structures and graph algorithms can be applied to a realistic rescue workflow, including cat intake, foster prioritization, adoption ordering, fast record lookup, and rescue route planning.

This repository is ready to run with:

```bash
python src/main.py
```

## Project Goals
The capstone was designed to satisfy a data structures and algorithms requirement while still matching the CTRS rescue theme. The application shows how to:
- record cat intake events
- organize adoptable cats efficiently
- prioritize urgent medical and foster cases
- retrieve cat records quickly
- compute the shortest route across a rescue network

## Data Structures and Algorithms Used
### 1. Stack
File: `src/stack_history.py`
- Used to track intake history in last-in, first-out order.
- Example use: the latest intake can be reviewed instantly using `peek()`.

### 2. Hash Table with Collision Handling
File: `src/hash_table.py`
- Used as the main cat registry.
- Implements **separate chaining** to handle collisions.
- Tracks collision count and rehashes when the load factor exceeds 0.75.

### 3. Priority Queue / Heap
File: `src/priority_queue.py`
- Uses Python's binary heap implementation.
- One heap manages foster requests by urgency.
- One heap manages medical cases by composite priority score.

### 4. BST / Self-Balancing Tree (AVL Tree)
File: `src/avl_tree.py`
- Stores adoptable cats ordered by `(age_months, cat_id)`.
- Automatically rotates to remain balanced.
- Guarantees efficient insertion and traversal compared with an unbalanced BST.

### 5. Graph Theory and Weighted Graphs
Files: `src/graph_routes.py`, `data/network.txt`
- The rescue network is represented as an **adjacency list** weighted graph.
- The program runs **Dijkstra's algorithm** to compute shortest travel distance between rescue sites.

## Repository Structure
```text
ctrs_capstone/
├── README.md
├── requirements.txt
├── data/
│   └── network.txt
└── src/
    ├── main.py
    ├── ctrs_system.py
    ├── models.py
    ├── stack_history.py
    ├── hash_table.py
    ├── priority_queue.py
    ├── avl_tree.py
    └── graph_routes.py
```

## How the Program Works
When `main.py` runs, it:
1. loads a weighted rescue network from `data/network.txt`
2. seeds sample cats and foster requests
3. prints a dashboard summary
4. shows adoptable cats ordered through the AVL tree
5. pops the highest-priority foster request from the heap
6. pops the most urgent medical case from the priority queue
7. performs a hash-table lookup by cat ID
8. calculates the shortest route between two rescue locations
9. displays intake history stored in a stack

## Complexity Analysis
| Operation | Data Structure / Algorithm | Time Complexity |
|---|---|---|
| Push intake history | Stack | O(1) |
| Peek latest intake | Stack | O(1) |
| Insert or lookup cat | Hash Table (average) | O(1) |
| Insert or lookup cat | Hash Table (worst case with heavy collisions) | O(n) |
| Rehash table | Hash Table | O(n) |
| Push / pop foster request | Binary Heap | O(log n) |
| Push / pop medical case | Binary Heap | O(log n) |
| Insert adoptable cat | AVL Tree | O(log n) |
| In-order traversal of adoptable cats | AVL Tree | O(n) |
| Shortest route | Dijkstra with heap | O((V + E) log V) |

## Why This Is a Strong Capstone
- It integrates multiple required structures in one coherent domain.
- It is easy for an instructor to run and verify.
- It shows both implementation details and practical use cases.
- It includes collision handling, self-balancing trees, heaps, and weighted graphs.

## Running the Project
### 1. Clone the repository
```bash
git clone <ttps://github.com/Judilyn28/CTRS-Capstone-Project.git>
cd ctrs_capstone
```

### 2. Run the project
```bash
python src/main.py
```

## Sample Output
```text
CTRS CAPSTONE - Cat Triage and Rescue System
Author: Judilyn Lucena
...
```

## Submission Checklist
- [x] Public GitHub repository
- [x] `src/` folder with `main.py` and modules
- [x] `data/network.txt`
- [x] `README.md` with complexity analysis
- [x] `requirements.txt`

## GitHub Steps
1. Create a new public repository on GitHub.
2. Upload all files from this project.
3. Commit with a message like `Finalize CTRS capstone project`.
4. Copy the public repository URL and submit it to your instructor.
