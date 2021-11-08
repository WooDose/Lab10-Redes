from kafka import KafkaConsumer

TOPIC_NAME = '16362'

SERVER = '20.120.14.159:9092'

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=SERVER)

def Clean_data(i):
    i = i.replace("value=b", "")
    i = i.replace(chr(92), "")
    i = i.replace(chr(39), "")
    i = i.replace("{", "")
    i = i.replace("}", "")
    return i

for message in consumer:

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


    ## Aqui iria el codigo del plot
    ##print('\n')    
    ##print(temp, hum, direct)
    ##print('\n')