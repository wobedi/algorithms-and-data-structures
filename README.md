> Looking at this repo in 2023? Note that I coded this in 2020 and have been working mostly in TypeScript since then - the result: https://www.bilateralstimulation.io/about

# Data Structures and Algorithms

> Implementations and performance plots for fundamental data structures and algorithms

## Built with

- Python
- [Perfplot](https://pypi.org/project/perfplot/) for the performance plots

## Background

I am a self-taught software engineer with no formal CS background.

I was already working as a professional web developer but I always felt the urge to learn more about CS fundamentals.

So I created a study plan and spent nights and weekends learning about and implementing common algorithms and data structures.

This repo is the result.

## Scope

![Read-Black Binary Search Tree](https://user-images.githubusercontent.com/31690419/83269557-8fb83780-a1c7-11ea-8a89-6d4d2433e502.png)

**This repo includes implementations of the following algorithms and data structures:**

### Arrays

- Deque via a dynamically-sized array with ring buffer
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

### Symbol Tables

- Binary search tree
- Hash map with separate chaining
- Hash map with linear probing
- Read black binary search tree (proud of this one)

Each implementation includes a unit test in its `if __name__ == '__main__':`

## Performance plots

![searching-integers_sample-size-500](https://user-images.githubusercontent.com/31690419/86478766-20e07800-bd4b-11ea-9868-2125ed8162b5.png)

**In addition, this repo also includes performance plots for the following scenarios:**

- Calculating the n-th fiboncacci number (recursively vs. memoized)
- Searching a graph depth-first and breadth-first
- Solving the 0-1 knapsack problem (recursively vs. memoized)
- Inserting items into a priority queue
- Sorting integers (with various algorithms)
- Searching integers (within various data structures)

An interesting observation about these performance plots is that they do not always illustrate the big O time complexity of the underlying algorithms the way you would expect. Often times the sample size is too small for big O to really kick in; at small sample sizes the platform, coefficients and overhead can make up the bulk of the running time.

## Installing and running it locally

Clone the repo:

```bash
git clone https://github.com/wobedi/algorithms-and-data-structures.git
```

Then run the following commands in your terminal from the project root folder to install it:

```bash
pip3 install virtualenv
virtualenv env
source env/bin/activate

pip3 install -e .
pip3 install -r requirements.txt
```

You can run unit tests for any implementation by navigating to its folder and then running it as a python module:

```bash
cd src/implementations/symbol_tables
python3 hash_map_w_chaining.py
```

Likewise, you can generate performance plots like so:

```bash
# adjust the sample size in src/perf_plots/config.py
cd src/perf_plots
python3 fibonacci.py
```
