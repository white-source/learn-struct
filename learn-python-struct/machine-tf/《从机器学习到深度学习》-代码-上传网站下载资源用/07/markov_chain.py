
import numpy as np

init_probs = np.array([0.1, 0.3, 0.6])
transform_probs = np.array([[0.7, 0.1, 0.2],
                            [0.2, 0.5, 0.3],
                            [0.2, 0.4, 0.4]])

chain = [init_probs]
def check_stable():
    if len(chain)<3:
        return False
    for i in range(-2, -1):
        if not np.array_equal(np.around(chain[i], 2),  np.around(chain[i-1], 2)):
            return False
    return True

for i in range(10000):
    chain.append(chain[-1].dot(transform_probs))
    print("iter %s: %s"%(i, np.around(chain[-1], 2)))
    if check_stable():
        print("stabled!")
        break
