import numpy as np


def algM():
    N = np.array([10, 20, 30,])
    alp = np.array([1, 2, 3,  ])
    n=np.array([[2,5,2],[15,5,5],[0.2,5,8]])
    y=n.transpose()

    print(y)
    print(alp)
    #print(N*alp)
    print(N[1])

    for i, value in enumerate(N):
        print(f"N[{i}] = {value}")

    for i, value in enumerate(alp):
        print(f"alp[{i}] = {value}")

    for i, value_alp in enumerate(alp):
        for j, value_N in enumerate(N):
            if j==1:
                print(value_alp)

    print(N[1]*alp)
    w = N[1]*alp

    x=np.linalg.solve(n,alp)
    print(x)







if __name__ == "__main__":
    algM()





