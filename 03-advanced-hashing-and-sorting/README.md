# Advanced hashing and sorting

SIT320 credit task 3.

Two halves.
The first takes a provided extendible hashing implementation, finds the bugs in it and fixes them.
The second builds external merge sort for data that does not fit in memory.

## Task 3: extendible hashing

I worked the insertion trace by hand first, then wrote a simulator to check it.
It replays both hash schemes across all 17 insertions, keeps the duplicated keys 26 and 47 as separate records, and reports the final directory and bucket layout, which is where the comparison table in the report comes from.

The provided code loses records.
The notebook shows each bug with a run that triggers it, then the run after the patch, so the failure and the fix sit next to each other.
Seven tests cover the hand-worked trace, the keys the original code drops, duplicates and repeated hash values, an empty structure, varying the initial bucket count, deletion with buddy merging and directory halving, loading from an external file, and mixed insert and delete sequences.

## Task 4: simulated external merge sort

Sort and merge passes over data too large for memory, with a sweep over buffer size to show how the number of passes responds.

`keys.csv` holds 15 key, amount and user records and is the external file the load test reads.

## Running it

```
pip install numpy
jupyter notebook SIT320_Code_1.ipynb
```

Keep `keys.csv` in the same folder as the notebook.
