from os import write
from functions import b_decode
from itertools import count
import csv

from kafka import KafkaConsumer


TOPIC_NAME = '14104'

SERVER = '20.120.14.159:9092'

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=SERVER)

RESTRICTED = True


t = [0.0]
h = [0]
d = [0]
c = [0] 

def Clean_data(i):
    i = i.replace("value=b", "")
    i = i.replace(chr(92), "")
    i = i.replace(chr(39), "")
    i = i.replace("{", "")
    i = i.replace("}", "")
    return i





cnt = 0
for message in consumer:
    if RESTRICTED:
        #print(message)
        temp, hum, direct = b_decode(message[6].decode())
        print(temp,hum,direct)

        

        


        t.append(float(temp))
        h.append(int(hum))
        d.append(int(direct))
        cnt += 1
        c.append(cnt)

        f = open('temp.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(t)
        f.close()

        f = open('hum.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(h)
        f.close()

        f = open('time.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(c)
        f.close()
    
        
        #plt.show()

    else:
        print(message)
        message = str(message).split(', ')
        data = []
        for i in message:
            if "Temperature" in i or "Humidity" in i or "Wind direction" in i:
                i = Clean_data(i)
                data.append(i)

        #Estas son las variables a plottear
        temp = float(data[0].split(" ")[-1])
        hum = int(data[1].split(" ")[-1])
        direct = int(data[2].split(" ")[-1])

        t.append(temp)
        h.append(hum)
        d.append(direct)
        cnt += 1
        c.append(cnt)
        