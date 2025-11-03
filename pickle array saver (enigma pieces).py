import numpy as np
import pickle

pieces = [
np.array([[0, 1, 1.02, 1],
       [1, 1, 0, 0]]), 
np.array([[1.02, 0, 0, 0],
       [1, 1, 1, 1.02]]), 
np.array([[1, 0, 0],
       [1.02, 1, 1.02],
       [0, 1, 0]]), 
np.array([[1, 1, 1, 1.02],
       [0, 0, 1, 0]]), 
np.array([[1.02, 1, 1],
       [1, 0, 1]]), 
np.array([[1, 1.02, 1],
       [0, 1, 1.02]]), 
np.array([[1, 1.02, 1],
       [0, 1, 0]]), 
np.array([[1.02, 1],
       [1, 0]]), 
np.array([[1.02, 1, 1],
       [0, 0, 1],
       [0, 0, 1]]), 
np.array([[1.02, 0, 0],
       [1, 1.02, 1]]), 
np.array([[1, 1, 0],
       [0, 1.02, 1]])
]
with open('enigma_pieces.pkl', 'wb') as f:
    pickle.dump(pieces, f)

