import math

import numpy as np


def algM():
    N = np.array([10, 20, 30])*2
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


    #for i, value_alp in enumerate(alp):
        #for j, value_N in enumerate(N):
           # if j==0:
            #print(value_alp)
    #Вычисление количества ромбических ячеек mmm и mm- количество кольцевых ребер
    H=5.585 #берется из кнопки высота конструкции
    D=2.560 #диаметр тоже кнопка
    b=np.array([ 14,14,18])*0.001#значения толщин ребер
    h=np.array([ 6,3,30])*0.001 #значения высот ребер
    alp0=19*math.pi/180
    N_sp=72 #пар спиральных ребер
    N_kol=37 #число кольцевых для исходной модели
    N_chp=2 #число шпангоутов
    ro=1781 #плотность материала


    V1=H/math.cos(alp0)*2*N_sp*b[0]*h[0]
    V2=N_kol*math.pi*D/2*b[1]*h[1]*2
    V3=N_chp*math.pi*D/2*2*b[2]*h[2]
    V=V1+V2+V3

    M1=ro*V1
    M2 = ro * V2
    M3 = ro * V3
    M=M1+M2+M3


    for i,value_alp_ in enumerate(alp):
        for j, value_N_ in enumerate(N):
            mmm=(H/(2*math.pi*D/2))*(N[j]*math.tan(alp[i]))
            mm=math.ceil(mmm)*2
            print(math.ceil(mm))
    #print(N[1]*alp)

    #вычисление длин спиральных ребер
    for i, value_alp_ in enumerate(alp):
        L = H/math.cos(alp[i])
        print(L)
    #расчет толщин ребер при фиксированной высоте

    









    x=np.linalg.solve(n,alp)
   # print(x)







if __name__ == "__main__":
    algM()





