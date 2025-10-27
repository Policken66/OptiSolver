import math
import numpy as np
def algM():
    N = np.array([30,45,60,75,90])*2
    alp = np.array([14,16,18,20,22,24])*math.pi/180



    #n=np.array([[2,5,2],[15,5,5],[0.2,5,8]])
    #y=n.transpose()



    #print(alp)
    #print(N*alp)
    #print(N[1])

   # for i, value in enumerate(N):
       #print(f"N[{i}] = {value}")

#    for i, value in enumerate(alp):
       # print(f"alp[{i}] = {value}")


    #for i, value_alp in enumerate(alp):
        #for j, value_N in enumerate(N):
           # if j==0:
            #print(value_alp)
    #Вычисление количества ромбических ячеек mmm и mm- количество кольцевых ребер
    HH=5.585 #берется из кнопки высота конструкции
    D=2.560 #диаметр тоже кнопка
    b=np.array([ 14,14,18])*0.001#значения толщин ребер
    h=np.array([ 6,3,30])*0.001 #значения высот ребер
    alp0=19*math.pi/180
    N_sp=72 #пар спиральных ребер
    N_kol=37 #число кольцевых для исходной модели
    N_chp=2 #число шпангоутов
    ro=1781 #плотность материала


    V1=HH/math.cos(alp0)*2*N_sp*b[0]*h[0]
    V2=N_kol*math.pi*D/2*b[1]*h[1]*2
    V3=N_chp*math.pi*D/2*2*b[2]*h[2]
    V=V1+V2+V3
    #print(V2)

    M1=ro*V1
    M2 = ro * V2
    M3 = ro * V3
    M=M1+M2+M3


    for i,value_alp_ in enumerate(alp):
        for j, value_N_ in enumerate(N):
            for k, value_N_ in enumerate(h):
             mmm=(HH/(math.pi*D))*(N[0]*math.tan(18*math.pi/180))
             mm=math.ceil(mmm)-k
           # print(math.ceil(mm))
           # print(mm)

    #вычисление длин спиральных ребер
    for i, value_alp_ in enumerate(alp):
        L = HH/math.cos(alp[i])
        #print(L)
    #расчет спиральных толщин ребер при фиксированной высоте

    for i, value_alp_ in enumerate(alp):
        for j, value_alp_ in enumerate(N):
            bb_sp=V1/(N[j]*h[0]*HH/math.cos(alp[i]))
            mmm = (HH / (2 * math.pi * D / 2)) * (N[j] * math.tan(alp[i]))/2
            mm = math.ceil(mmm)
            bb_k = V2 / (mm *2* math.pi * D / 2 * h[1])
            bb_=(bb_k+bb_sp)/2
            print(bb_)



    # расчет кольцевых толщин ребер при фиксированной высоте )

#    {
#      "a11": h[0],
#      "b11": bb_,
#       "c": 1.2,
#       "dd": 1.8,
#       "a22": h[1],
#       "b22": bb_,
#       "N": 99,
#       "m": 4,
#       "d": 62.516999999999996,
#       "HH": 25.0,
#       "alp": 0.75
#   }
    #for i in range(0, enumerate(N)):
    #    print(i)




   # x=np.linalg.solve(n,alp)
   # print(x)




if __name__ == "__main__":
    algM()





