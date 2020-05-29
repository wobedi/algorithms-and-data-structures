# Data Structures and Algorithms

> Implementations and performance plots for fundamental data structures and algorithms

## Built with

- Python
- [Perfplot](https://pypi.org/project/perfplot/) for the performance plots

## Background

I am a self-taught software engineer with no formal CS background.

I was already working as a professional web developer but I always felt the urge to learn more about CS fundamentals.

So I embarked on a months-long learning journey, focusing on data structures and algorithms.

I created a study plan and spent nights and weekends learning about and implementing common algorithms and data structures.

This repo is the result.

## Scope

![Read-Black Binary Search Tree](https://user-images.githubusercontent.com/31690419/83269557-8fb83780-a1c7-11ea-8a89-6d4d2433e502.png)

**This repo includes implementations of the following algorithms and data structures:**

### Arrays

- Dequeue via a dynamically-sized array with ring buffer
- Binary search
- Quickselect

### Dynamic Programming

- Calculating the n-th fibonacci number
- Solving the 0-1 knapsack problem
- Finding the longest common subsequence (LCS) of two strings

### Graph representations

- Undirected
- Directed
- Weighted

### Graph operations

- Breadth-first search
- Depth-first search
- Connectivity of two nodes
- Shortest path via Dijkstra's algorithm
- Topological sort

### Misc

- LRU cache
- Priority queue via binary heap

### Sorting

- Basic sorts (selection, insertion, shell)
- Mergesort
- Heapsort
- Quicksort
- Radixsort

### Strings

- Huffman encoding
- R-way trie
- Suffix trie
- Ternary search trie
- Symbol Tables
  - Binary search tree
  - Hash map with separate chaining
  - Hash map with linear probing
  - Read black binary search tree (proud of this one)

Each implementation includes a unit test in in its `if __name__ == '__main__'`

## Performance plots

![fibonacci-plot_size-11](https://user-images.githubusercontent.com/31690419/83267964-3d761700-a1c5-11ea-961f-a7aaf0d6d559.png)

**In addition, this repo also includes performance plots for the following scenarios:**

- Calculating the n-th fiboncacci number (recursively vs. memoized)
- Solving the 0-1 knapsack problem (recursively vs. memoized)
- Sorting integers (with various algorithms)

## Installing it locally

```bash
git clone

pip3 install virtualenv
virtualenv env
source env/bin/activate

pip3 install -e .
pip3 install -r requirements.txt
```
