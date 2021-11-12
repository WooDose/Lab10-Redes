import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import itertools




def an(i):

    dfT = pd.read_csv('temp.csv')
    dfT = list(dfT)
    dfT = [float(t) for t in dfT]
    #print(dfT)

    dfH = pd.read_csv('hum.csv')
    dfH = list(dfH)
    dfH = [float(h) for h in dfH]

    dfC = pd.read_csv('time.csv')
    dfC = list(dfC)

    ax.cla()
    ax1.cla()

    tempx = [a for a in range(len(dfT))]
    hmx = [a for a in range(len(dfH))]
    print(dfT, tempx, len(dfT), len(tempx))
    ax.scatter(tempx, dfT)
    
    ax1.scatter(hmx, dfH)
    #ax.text(len(dfT)-1, str(dfT[-1])+2, "{}%".format(str(dfT[-1])))
    #ax1.text(len(dfH)-1, str(dfH[-1])+2, "{}%".format(str(dfH[-1])))
    ax.set_ylim(0,100)
    ax1.set_ylim(0,100)
    ax.set_ylabel('Temperatura')
    ax1.set_ylabel('Humedad')
    #ax.plot(tempx,dfT)
    #ax1.plot(hmx,dfH)


fig = plt.figure(figsize=(12,6), facecolor='#DEDEDE')
ax = plt.subplot(121)
ax1 = plt.subplot(122)
ax.set_facecolor('#DEDEDE')
ax1.set_facecolor('#DEDEDE')


#ani = FuncAnimation(plt.gcf(), cons)
ani = FuncAnimation(plt.gcf(), an, interval=3000)
#an('e')
plt.show()
