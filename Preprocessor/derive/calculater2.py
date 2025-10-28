import math
import numpy as np
def algM():
    N = np.array([30,45,60,75])*2
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
    HH=5.585 #берется из кнопки высота конструкции кнопка
    D=2.560 #диаметр тоже кнопка
    b=np.array([14,14,18])*0.001 #значения толщин ребер кнопка
    h=np.array([6,3,30])*0.001 #значения высот ребер кнопка
    alp0=19*math.pi/180 #исходной угол кнопка
    N_sp=72 #пар спиральных ребер кнопка для исходной
    N_kol=37 #число кольцевых для исходной модели расчет по формуле для mm
    N_chp=2 #число шпангоутов кнопка
    ro=1781 #плотность материала


    V1=HH/math.cos(alp0)*2*N_sp*b[0]*h[0]
    V2=N_kol*math.pi*D/2*b[1]*h[1]*2
    V3=N_chp*math.pi*D/2*2*b[2]*h[2]
    V=V1+V2+V3
    #print(V2)
    #Расчет масс приходящихся на каждое из семейства ребер
    M1=ro*V1
    M2 = ro * V2
    M3 = ro * V3
    M=M1+M2+M3

    #расчет длин спиральных ребер в зависимости от угла наклона
    L = np.zeros(len(alp))
    #вычисление длин спиральных ребер
    for i, value_alp_ in enumerate(alp):
        L [i] = HH/math.cos(alp[i])
    #print(L)

    #расчет спиральных толщин ребер при фиксированной высоте
    mmm = np.zeros((len(alp), len(N)))
    mm = np.zeros((len(alp), len(N)))
    bb_k = np.zeros((len(alp), len(N)))
    bb_sp = np.zeros((len(alp), len(N)))
    bb_ = np.zeros((len(alp), len(N)))
    hh_k = np.zeros((len(alp), len(N)))
    hh_sp = np.zeros((len(alp), len(N)))

    for i in range(0,len(alp)):
        for j in range(0,len(N)):
            for k in range(4,0,-1):
                #Расчет для толщин с фиксированной высотой относительно исходной конструкции
             bb_sp[i,j]=V1/(N[j]*h[0]*L [i])
             mmm[i,j]= (HH / (2 * math.pi * D / 2)) * (N[j] * math.tan(alp[i]))/2
             mm [i,j] = np.round(mmm[i,j])+4*k#(k-1)*2 #число кольцевых ребер
             bb_k [i,j] = V2 / ((mm [i,j]) *2* math.pi * D / 2 * h[1])
             bb_[i,j]=(bb_k[i,j]+bb_sp[i,j])/2
            #Расчет высоты реберной структуры при фиксированной толщине относительно исходной конструкции
             hh_sp[i,j]=V1/(N[j]*b[0]*L [i])  #диапазон высот для каждой из моделей для спиральных ребер
             hh_k[i, j] = V2 / ((mm[i, j]) * 2 * math.pi * D / 2 * b[1]) #диапазон высот для каждой из моделей для кольцевых ребер

    print(hh_sp)
    print(hh_k)
    #print(bb_k)




    # расчет кольцевых толщин ребер при фиксированной высоте )

   # {
 #     "a11": h[0],
  #    "b11": bb_,
   #    "c": 1.2,
   #    "dd": 1.8,
   #    "a22": h[1],
   #    "b22": bb_,
   #    "N": 99,
   #    "m": 4,
   #    "d": 62.516999999999996,
   #    "HH": 25.0,
   #    "alp": 0.75
  # }
    #for i in range(0, enumerate(N)):
    #    print(i)




   # x=np.linalg.solve(n,alp)
   # print(x)




if __name__ == "__main__":
    algM()





