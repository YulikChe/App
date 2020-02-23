import numpy as np
import matplotlib.pyplot as plt

def test(coordinats):
    print(len(coordinats))
    for i in coordinats:
        print(i)
    coordinats = np.array([[coordinats[0], coordinats[1]], [coordinats[2], coordinats[3]], [coordinats[4], coordinats[5]]])
    plt.figure()
    plt.scatter(coordinats[:, 0], coordinats[:, 1])
    t2 = plt.Polygon(coordinats)
    plt.gca().add_patch(t2)
    plt.show()