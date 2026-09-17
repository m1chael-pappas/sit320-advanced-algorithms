# Linear programming

SIT320 pass task 8.

Solving linear systems, then optimising over the feasible regions they define.

## What the notebook covers

| Activity | Contents |
| --- | --- |
| 1 | Solving y = Ax by LU decomposition, across four cases covering the different shapes the system can take. |
| 2 | Maximising Z = 5X1 + 3X2 graphically. Plots the feasible region, finds the corner points and evaluates Z at each. |
| 3 | Factory problem. Products A at $40 profit and 2 hours and B at $30 profit and 1 hour share one machine with 40 hours a week. Formulate and solve it. |
| 4 | Simplex on Z = 18X1 + 12.5X2. |

`fig_graphical.png` and `fig_factory.png` are the plots from activities 2 and 3, saved for the report.

The graphical method and simplex reach the same answer on these problems, which is the point of running both.

## Running it

```
pip install numpy matplotlib
jupyter notebook Code_LinearProgramming.ipynb
```
