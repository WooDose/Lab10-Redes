from random import randint, gauss
from time import sleep
import json

def truncate(n, type_='int'):
    a = n if n < 100.00 else 100.00
    a = n if n > 0.00 else 0.00
    a = a if type_ == "float" else int(a)
    return a

def produce_data():
    data_raw = {
        'Temperature' : round(truncate(gauss(50,50/3), 'float'), 2),
        'Humidity' : truncate(gauss(50,50/3)),
        'Wind direction': randint(0,7)}
    
    
    data = json.dumps(data_raw).encode('utf-8')
    return data, data_raw


def byteize(data):
    tmp_bit = int(data['Temperature']*100)
    tmp_bit = format(tmp_bit, 'b').zfill(14)
    ## Add all to one 3 byte string
    data_bit = format(data['Wind direction'],'b').zfill(3) + format(data['Humidity'], 'b').zfill(7) + tmp_bit
    ## convert to characters
    f_byte, s_byte, l_byte = chr(int(data_bit[0:8], 2)), chr(int(data_bit[8:16], 2)), chr(int(data_bit[16:], 2))
    bytestr = f_byte+s_byte+l_byte
    return(bytestr)
    

def b_decode(bytestr):
    ## Add all into one string, padding
    #data_bit = format(ord(f_byte),'b').zfill(8) + format(ord(s_byte),'b').zfill(8) + format(ord(l_byte),'b').zfill(8)
    data_bit = format(ord(bytestr[0]),'b').zfill(8) +  format(ord(bytestr[1]),'b').zfill(8) +  format(ord(bytestr[2]),'b').zfill(8)
    print(data_bit)
    ## split into wd, hum, temp
    wd,hum,temp = data_bit[0:3],data_bit[3:10],data_bit[10:]
    ## revert to int
    wd,hum,temp = int(wd,2),int(hum,2),int(temp,2)
    ## convert temp to real value
    temp=float(temp/100.00)
    return(temp,hum,wd)


    
    

# while True:
#    data, data_raw  = produce_data()
#    print(data)
#    print(decode(byteize(data_raw)))


#    sleep(3)    

   
