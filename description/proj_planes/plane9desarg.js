const plane9 = {
    lines: 
  [[[6, 5, 1, 4, 0, 8, 2, 7, 3],
    [7, 3, 2, 5, 1, 6, 0, 8, 4],
    [8, 4, 0, 3, 2, 7, 1, 6, 5],
    [0, 8, 4, 7, 3, 2, 5, 1, 6],
    [1, 6, 5, 8, 4, 0, 3, 2, 7],
    [2, 7, 3, 6, 5, 1, 4, 0, 8],
    [3, 2, 7, 1, 6, 5, 8, 4, 0],
    [4, 0, 8, 2, 7, 3, 6, 5, 1],
    [5, 1, 6, 0, 8, 4, 7, 3, 2]],
   [[5, 2, 8, 3, 0, 6, 4, 1, 7],
    [3, 0, 6, 4, 1, 7, 5, 2, 8],
    [4, 1, 7, 5, 2, 8, 3, 0, 6],
    [8, 5, 2, 6, 3, 0, 7, 4, 1],
    [6, 3, 0, 7, 4, 1, 8, 5, 2],
    [7, 4, 1, 8, 5, 2, 6, 3, 0],
    [2, 8, 5, 0, 6, 3, 1, 7, 4],
    [0, 6, 3, 1, 7, 4, 2, 8, 5],
    [1, 7, 4, 2, 8, 5, 0, 6, 3]],
   [[1, 8, 3, 5, 0, 7, 6, 4, 2],
    [2, 6, 4, 3, 1, 8, 7, 5, 0],
    [0, 7, 5, 4, 2, 6, 8, 3, 1],
    [4, 2, 6, 8, 3, 1, 0, 7, 5],
    [5, 0, 7, 6, 4, 2, 1, 8, 3],
    [3, 1, 8, 7, 5, 0, 2, 6, 4],
    [7, 5, 0, 2, 6, 4, 3, 1, 8],
    [8, 3, 1, 0, 7, 5, 4, 2, 6],
    [6, 4, 2, 1, 8, 3, 5, 0, 7]],
   [[4, 3, 5, 1, 0, 2, 7, 6, 8],
    [5, 4, 3, 2, 1, 0, 8, 7, 6],
    [3, 5, 4, 0, 2, 1, 6, 8, 7],
    [7, 6, 8, 4, 3, 5, 1, 0, 2],
    [8, 7, 6, 5, 4, 3, 2, 1, 0],
    [6, 8, 7, 3, 5, 4, 0, 2, 1],
    [1, 0, 2, 7, 6, 8, 4, 3, 5],
    [2, 1, 0, 8, 7, 6, 5, 4, 3],
    [0, 2, 1, 6, 8, 7, 3, 5, 4]],
   [[8, 6, 7, 2, 0, 1, 5, 3, 4],
    [6, 7, 8, 0, 1, 2, 3, 4, 5],
    [7, 8, 6, 1, 2, 0, 4, 5, 3],
    [2, 0, 1, 5, 3, 4, 8, 6, 7],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 0, 4, 5, 3, 7, 8, 6],
    [5, 3, 4, 8, 6, 7, 2, 0, 1],
    [3, 4, 5, 6, 7, 8, 0, 1, 2],
    [4, 5, 3, 7, 8, 6, 1, 2, 0]],
   [[2, 4, 6, 7, 0, 5, 3, 8, 1],
    [0, 5, 7, 8, 1, 3, 4, 6, 2],
    [1, 3, 8, 6, 2, 4, 5, 7, 0],
    [5, 7, 0, 1, 3, 8, 6, 2, 4],
    [3, 8, 1, 2, 4, 6, 7, 0, 5],
    [4, 6, 2, 0, 5, 7, 8, 1, 3],
    [8, 1, 3, 4, 6, 2, 0, 5, 7],
    [6, 2, 4, 5, 7, 0, 1, 3, 8],
    [7, 0, 5, 3, 8, 1, 2, 4, 6]],
   [[7, 1, 4, 6, 0, 3, 8, 2, 5],
    [8, 2, 5, 7, 1, 4, 6, 0, 3],
    [6, 0, 3, 8, 2, 5, 7, 1, 4],
    [1, 4, 7, 0, 3, 6, 2, 5, 8],
    [2, 5, 8, 1, 4, 7, 0, 3, 6],
    [0, 3, 6, 2, 5, 8, 1, 4, 7],
    [4, 7, 1, 3, 6, 0, 5, 8, 2],
    [5, 8, 2, 4, 7, 1, 3, 6, 0],
    [3, 6, 0, 5, 8, 2, 4, 7, 1]],
   [[3, 7, 2, 8, 0, 4, 1, 5, 6],
    [4, 8, 0, 6, 1, 5, 2, 3, 7],
    [5, 6, 1, 7, 2, 3, 0, 4, 8],
    [6, 1, 5, 2, 3, 7, 4, 8, 0],
    [7, 2, 3, 0, 4, 8, 5, 6, 1],
    [8, 0, 4, 1, 5, 6, 3, 7, 2],
    [0, 4, 8, 5, 6, 1, 7, 2, 3],
    [1, 5, 6, 3, 7, 2, 8, 0, 4],
    [2, 3, 7, 4, 8, 0, 6, 1, 5]]]
};