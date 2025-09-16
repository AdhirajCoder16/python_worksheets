import numpy as np

positions = np.array([[0, 0],
                      [2, 3],
                      [4, 7],
                      [7, 10],
                      [10, 15]])
dist = np.linalg.norm(positions[-1] - positions[0])
total_dist = np.sum(np.linalg.norm(np.diff(positions, axis=0), axis=1))
