import math

import numpy as np


def algM():
    N = np.array([10, 20, 30])
    alp = np.array([10, 15,20])*math.pi/180


    n=np.array([[2,5,2],[15,5,5],[0.2,5,8]])
    #y=n.transpose()



    print(alp)
    #print(N*alp)
    #print(N[1])

    for i, value in enumerate(N):
       print(f"N[{i}] = {value}")

    for i, value in enumerate(alp):
        print(f"alp[{i}] = {value}")


    for i, value_alp in enumerate(alp):
        for j, value_N in enumerate(N):
            if j==0:


                print(value_alp)
    H=5.585
    D=2.560
    for i,value_alp_ in enumerate(alp):
        for j, value_N_ in enumerate(N):
            mm=H/(2*math.pi*D/2*N[j]*math.tan(alp[i]))*2
            mmm=H/(2*math.pi*D/2)
            print(math.ceil(mm))
    print(math.tan(alp[0]))
    #print(N[1]*alp)

    w = N[1]*alp





    x=np.linalg.solve(n,alp)
   # print(x)







if __name__ == "__main__":
    algM()





