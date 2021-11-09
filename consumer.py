from functions import b_decode
from kafka import KafkaConsumer


TOPIC_NAME = '14104'

SERVER = '20.120.14.159:9092'

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=SERVER)

RESTRICTED = True

def Clean_data(i):
    i = i.replace("value=b", "")
    i = i.replace(chr(92), "")
    i = i.replace(chr(39), "")
    i = i.replace("{", "")
    i = i.replace("}", "")
    return i

for message in consumer:
    if RESTRICTED:
        #print(message)
        temp, hum, direct = b_decode(message[6].decode())
        print(temp,hum,direct)
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


    print(temp,hum,direct)
    ## Aqui iria el codigo del plot
    ##print('\n')    
    ##print(temp, hum, direct)
    ##print('\n')
