# Advanced trees

SIT320 pass task 2.

Binary search trees built from scratch, then the balanced structures that fix their worst case.
Every tree is drawn with Graphviz so the shape after each operation is visible rather than described.

## What the notebook covers

| Task | Contents |
| --- | --- |
| 1 | Lesson review |
| 2 | Balance tracking in a BST |
| 3 | First common ancestor of two nodes |
| 4 | Left and right rotations |
| 5 | Red-black tree insertion and deletion |
| 6 | B+ tree insertion at order m = 3 |
| 7 | B-tree insertion at order m = 3 |
| 8 | Comparing the internal node structure of the two |
| 9 | Range query over a B+ tree |

Tasks 1 to 4 build on the lab's BST sections, which cover search, insert and delete.

## Running it

```
pip install numpy graphviz
jupyter notebook code.ipynb
```

The `graphviz` Python package needs the Graphviz binaries installed as well, through `apt install graphviz` or `brew install graphviz`.
