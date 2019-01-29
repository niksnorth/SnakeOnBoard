# SnakeOnBoard
Laying a snake on square matrix


Question:

    How many different ways can you lay a snake of length 16 on a 4x4 grid? 
    Crossing or diagonal movements are not allowed.


Grid:

    +---------+---------+---------+---------+
    |         |         |         |         |
    |    0    |    1    |    2    |    3    |
    |         |         |         |         |
    +---------+---------+---------+---------+
    |         |         |         |         |
    |    4    |    5    |    6    |    7    |
    |         |         |         |         |
    +---------+---------+---------+---------+
    |         |         |         |         |
    |    8    |    9    |   10    |   11    |
    |         |         |         |         |
    +---------+---------+---------+---------+
    |         |         |         |         |
    |   12    |   13    |   14    |   15    |
    |         |         |         |         |
    +---------+---------+---------+---------+


ie. One way is:

    +---------+---------+---------+---------+
    |         |         |         |         |
    |    0---------1---------2---------3    |
    |         |         |         |    |    |
    +---------+---------+---------+----|----+
    |         |         |         |    |    |
    |    4---------5---------6---------7    |
    |    |    |         |         |         |
    +----|----+---------+---------+---------+
    |    |    |         |         |         |
    |    8---------9---------10-------11    |
    |         |         |         |    |    |
    +---------+---------+---------+----|----+
    |         |         |         |    |    |
    |    12-------13--------14--------15    |
    |         |         |         |         |
    +---------+---------+---------+---------+


And another:

    +---------+---------+---------+---------+
    |         |         |         |         |
    |    0    |    1---------2---------3    |
    |    |    |    |    |         |    |    |
    +----|----+----|----+---------+----|----+
    |    |    |    |    |         |    |    |
    |    4    |    5    |    6---------7    |
    |    |    |    |    |    |    |         |
    +----|----+----|----+----|----+---------+
    |    |    |    |    |    |    |         |
    |    8    |    9    |    10--------11   |
    |    |    |    |    |         |    |    |
    +----|----+----|----+---------+----|----+
    |    |    |    |    |         |    |    |
    |    12--------13   |    14--------15   |
    |         |         |         |         |
    +---------+---------+---------+---------+


Use Python 3.6+ and the standard modules only.

Do not output all the valid paths, just the total valid path count.  A single
number is all that is required as output of this program.

Answers for smaller square grids:

    * 1x1 grid (snake length 1) has 1 path
    * 2x2 grid (snake length 4) has 8 paths
    * 3x3 grid (snake length 9) has 40 paths

