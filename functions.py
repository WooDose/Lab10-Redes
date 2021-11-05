from random import randint, gauss
from time import sleep


def truncate(n, type_='int'):
    a = n if n < 100.00 else 100.00
    a = n if n > 0.00 else 0.00
    a = a if type_ == "float" else int(a)
    return a

def produce_data():
    data = {
        'Temperature' : truncate(gauss(50,50/3), 'float'),
        'Humidity' : truncate(gauss(50,50/3)),
        'Wind direction': randint(0,7)}
    return data

##while True:
##    print(produce_data)
##    sleep(3)    
##
##    
