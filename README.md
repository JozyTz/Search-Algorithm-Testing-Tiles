# Search-Algorithm-Testing-Tiles

Uses various search algorithms to solve a tile puzzle and formats the results to read.
*Breadth-First search
*Iterative Deepening DFS
*A-star with heuristics:
  - number of misplaced pieces
  - manhattan distances from goal state
  - Euclidian distances from goal state

To run:
python Run.py <filepath> <searchType>
with filepath being a formatted puzzle txt file and searchType being "BFS", "IDS", "h1", "h2", or "h3"

Look at autorunner.py and Run.py for usage/examples
