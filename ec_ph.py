import datetime
import time
import pandas as pd
import spidev
import csv
import os
import copy

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000
# def ReadChannel3008(channel):

data = []

repeat0 = 0
repeat1 = 0
repeat2 = 0
repeat3 = 0
repeat4 = 0
repeat5 = 0
repeat6 = 0
repeat7 = 0

def ReadChannel310008(channel):
    r=spi.xfer2([6 | (channel>>2), channel<<6,0])
    adc_out=((r[1]&15)<<8)+r[2]
    return adc_out      
       

ch0=[]
ch1=[]
ch2=[]
ch3=[]
ch4=[]
ch5=[]
ch6=[]
ch7=[]

'''
def ch00():
    global repeat0
    global ch0
    ch0=[]
    repeat0 = 0
    while repeat0 < 10000 :
        repeat0 = repeat0 + 1
        inp0=ReadChannel310008(0)
        voltage0 = inp0*3.3/4095
        # calibration
        round_inp0 = round(voltage0, 3)
        #print (round_inpa)
        ch0.append(round_inp0)
        
        if repeat0 == 10000:
            ch0_now = sum(ch0, 0.0)/len(ch0)
            round_ch0=round(ch0_now,3)
            return round_ch0
'''

def ch01():
    global repeat1
    global ch1
    ch1=[]
    repeat1 = 0
    while repeat1 < 10000 :
        repeat1 = repeat1 + 1
        inp1=ReadChannel310008(1)
        voltage1 = inp1*3.3/4095
        round_inp1 = round(voltage1, 3)
        #print (round_inpa)
        ch1.append(round_inp1)
       
        if repeat1 == 10000:
            ch1_now = sum(ch1, 0.0)/len(ch1)
            round_ch1=round(ch1_now,3)
            return round_ch1
        
def ch02():
    global repeat2
    global ch2
    ch2=[]
    repeat2 = 0
    while repeat2 < 10000 :
        repeat2 = repeat2 + 1
        inp2=ReadChannel310008(2)
        voltage2 = inp2*3.3/4095
        round_inp2 = round(voltage2, 3)
        #print (round_inpa)
        ch2.append(round_inp2)
       
        if repeat2 == 10000:
            ch2_now = sum(ch2, 0.0)/len(ch2)
            round_ch2=round(ch2_now,3)
            return round_ch2
        
def ch03():
    global repeat3
    global ch3
    ch3=[]
    repeat3 = 0
    while repeat3 < 10000 :
        repeat3 = repeat3 + 1
        inp3=ReadChannel310008(3)
        voltage3 = inp3*3.3/4095
        round_inp3 = round(voltage3, 3)
        #print (round_inpa)
        ch3.append(round_inp3)
       
        if repeat3 == 10000:
            ch3_now = sum(ch3, 0.0)/len(ch3)
            round_ch3=round(ch3_now,3)
            return round_ch3
        
        
def ch04():
    global repeat4
    global ch4
    ch4=[]
    repeat4 = 0
    while repeat4 < 1000 :
        repeat4 = repeat4 + 1
        inp4=ReadChannel310008(4)
        
        voltage4 = inp4*3.3/4095
        round_inp4 = round(voltage4, 3)
        #print (round_inpa)
        ch4.append(round_inp4)
        
        if repeat4 == 1000:
            ch4_now = sum(ch4, 0.0)/len(ch4)
            round_ch4=round(ch4_now,3)
            return round_ch4

def ch05():
    global repeat5
    global ch5
    ch5=[]
    repeat5 = 0
    while repeat5 < 1000 :
        repeat5 = repeat5 + 1
        inp5=ReadChannel310008(5)
        
        voltage5 = inp5*3.0/4095
        round_inp5 = round(voltage5, 3)
        #print (round_inpa)
        ch5.append(round_inp5)
        
        if repeat5 == 1000:
            ch5_now = sum(ch5, 0.0)/len(ch5)
            round_ch5=round(ch5_now,3)
            return round_ch5
    
def ch06():
    global repeat6
    time.sleep(0.01)
    global ch6
    ch6=[]
    repeat6 = 0
    while repeat6 < 1000 :
        repeat6 = repeat6 + 1
        inp6=ReadChannel310008(6)
        voltage6 = inp6*3.0/4095
        round_inp6 = round(voltage6, 3)
        #print (round_inpa)
        ch6.append(round_inp6)

        if repeat6 == 1000:
            ch6_now = sum(ch6, 0.0)/len(ch6)
            round_ch6=round(ch6_now,3)
            return round_ch6
'''
# def ch07():
#     global repeat7
#     time.sleep(0.01)
#     global ch7
#     ch7=[]
#     repeat7 = 0
#     while repeat7 < 30000 :
#         repeat7 = repeat7 + 1
#         inp7=ReadChannel310008(7)
#         voltage7 = inp7*3.3/4095
#         round_inp7 = round(voltage7, 3)
#         #print (round_inpa)
#         ch7.append(round_inp7)
        
#         if repeat7 == 30000:
#             ch7_now = sum(ch7, 0.0)/len(ch7)
#             round_ch7=round(ch7_now,3)
#             return round_ch7
'''

############# csv write method ############
def write_csv_header(path, labels):
    try:
        with open(path, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(labels)
    except IOError:
        print("I/O error")
        #mqttc = mqtt.Client("client587643_2")
        #mqttc.on_connect = on_connect
        #mqttc.connect('121.134.15.187', 2883)
        #mqttc.publish("fault/io", "csv error")

def write_csv(path, dic, labels):
    try:
        with open(path, 'a') as f:
            writer = csv.DictWriter(f, fieldnames=labels)
            writer.writerow(dic)
    except IOError:
        print("I/O error")
        #mqttc = mqtt.Client("client587643_3")
        #mqttc.on_connect = on_connect
        #mqttc.connect('121.134.15.187', 2883)
        #mqttc.publish("fault/io", "csv error")
        
def write_csv_rows(path, dic, labels):
    try:
        with open(path, 'a') as f:
            writer = csv.DictWriter(f, fieldnames=labels)
            for row in dic:
                writer.writerow(row)
    except IOError:
        print("I/O error")
        #mqttc = mqtt.Client("client587643_3")
        #mqttc.on_connect = on_connect
        #mqttc.connect('121.134.15.187', 2883)
        #mqttc.publish("fault/io", "csv error")

###########################################
###########################################

def set_log(data1, data2, data3, data4, data5, data6, data7, data8):
    #### time check
    x = datetime.datetime.now()
    x_date = x.date()
    x_time = x.time()
    x_time = x_time.strftime("%H:%M:%S")
    dct1 = {"Date": x_date, "Time":x_time, "ec": data1, "ph": data2, "MixTank_lv": data3, "Disct1_lv": data4, "Disct2_lv": data5, "MixTank_mv": data6, "Disct1_mv": data7, "Disct2_mv": data8}
    labels = ['Date', 'Time', 'ec', 'ph', 'MixTank_lv', 'Disct1_lv', 'Disct2_lv', 'MixTank_mv', 'Disct1_mv', 'Disct2_mv']
    log_list.append(dct1)
    
cnt = 0

current_datetime = datetime.datetime.now()
#exit_datetime = current_datetime + datetime.timedelta(hours=2)
exit_datetime = current_datetime + datetime.timedelta(minutes=2)
exit_time = exit_datetime.time()
log_list = []

try:    
    while True:
        start = time.time()
        # Channel0 = ch00() # not used
        ### water level
        Channel1 = ch01()
        Channel2 = ch02()
        Channel3 = ch03()
        ### ec, ph
        Channel4 = ch04() 
        Channel5 = ch05()
        ###
        Channel6 = ch06()  # not used
        # Channel7 = ch07()  # not used
        
        cnt = cnt + 1
        
        if cnt > 30:
            mixTank_lv = (Channel1 - 0.8314)/0.0354
            disct1_lv = (Channel2 - 0.9226)/0.0667
            disct2_lv = (Channel3 - 0.9944)/0.0676
            ec = 5.4894*Channel6 - 6.6144
            ph = 6.6994*Channel5 - 5.6964
            
            at = datetime.datetime.now()
            print(at, "EC:", ec, "pH:", ph, "MixTank_lv:", mixTank_lv, "Disct1_lv:", disct1_lv, "Disct2_lv:", disct2_lv)
            set_log(ec, ph, mixTank_lv, disct1_lv, disct2_lv, Channel1, Channel2, Channel3)
            cnt = 0
        
        nowchk = datetime.datetime.now()
        nowtchk = nowchk.time()   
        if (exit_time < nowtchk):
            #####logging
            labels = ['Date', 'Time', 'ec', 'ph', 'MixTank_lv', 'Disct1_lv', 'Disct2_lv', 'MixTank_mv', 'Disct1_mv', 'Disct2_mv']
            print("labels construction")
            write_csv_rows("./Data/lvecph.csv", log_list, labels) 
            #df = pd.read_csv("./Data/csv_dct.csv")
            #x = datetime.datetime.now()
            #x_date = x.date()
            #x_time = x.time()
            #x_time = x_time.strftime("%H")
            #df.to_csv("./Data/csv_dct.csv" + str(x_date)+str(x_time))
            print("logs saved")
            #os.remove("./Data/csv_dct.csv")
            #df = pd.read_csv("./Data/csv_dct_header.csv")
            #df.to_csv("./Data/csv_dct.csv")
            break

        if (time.time() - start) < 2.00:
            time.sleep(2.00-(time.time()-start))
        
except Exception as e:
    print(e)
    print("error")
