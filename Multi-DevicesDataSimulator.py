#!/usr/bin/env python

import time
import random
import paho.mqtt.client as mqtt 
from   threading import Thread

 
def GenerateData():
    #runningStatusTotalData = ["On","Off","On","On","On","On","On","On","On","On"]
    runningStatusTotalData = [1,0,1,1,1,1,1,1,1,1]

    speedTotalData = [600,900,1200]

    numberOfMachineData = ["S-05","S-06","S-07","S-08","S-09","S-10"]

    modelOfMachineData = "30B6S"

    modelOfProductData = ["3/4-10 HEX(不電鍍)","3/4-10 HEX(電鍍)","3/4-16 HEX(不電鍍)","3/4-16 HEX(電鍍)","3/4-10 HEX SLOT(不電鍍)","3/4-10 HEX SLOT(電鍍)"]
    

    for i in range(len(numberOfMachineData)):
        runningStatusDataIndex = random.randint(0,len(runningStatusTotalData)-1)
        runningStatusData = runningStatusTotalData[runningStatusDataIndex]
        
        yieldData = random.randint(35,55)

        timeData = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        availabilityData = random.randint(9,18)

        speedDataIndex = random.randint(0,len(speedTotalData)-1)
        speedData = speedTotalData[speedDataIndex]

        voltageData = random.randint(70,150)

        currentData = random.randint(20,50)

        if runningStatusData == 1:
            publishData = '{"RunningStatus": ' + str(runningStatusData) + ',"Yield": ' + str(yieldData) + ',"Time": "' + timeData + '","Availability": ' + str(availabilityData) + ',"Speed": ' + str(speedData) + ',"Voltage": ' + str(voltageData) + ',"Current": ' + str(currentData) + ',"機台編號": "' + numberOfMachineData[i] + '","機台型號": "' + modelOfMachineData + '","生產產品型號": "' + modelOfProductData[i] + '"}'
        else:
            publishData = '{"RunningStatus": ' + str(runningStatusData) + ',"Yield": 0' + ',"Time": "' + timeData + '","Availability": ' + str(availabilityData) + ',"Speed": 0' + ',"Voltage": 0' + ',"Current": 0' + ',"機台編號": "' + numberOfMachineData[i] + '","機台型號": "' + modelOfMachineData + '","生產產品型號": "' + modelOfProductData[i] + '"}'

        MQTT_InfluxPublisher(publishData)
    #print(publishData)


def MQTT_InfluxPublisher(newData):
    #mqtt connection metadata
    mqtt_host = "124.9.14.79"
    mqtt_port = 1883
    mqtt_username = '296efb60-c105-4721-9585-3663778f0ba4:38b893d0-077f-428b-afb2-ec26b05cb2bd'
    mqtt_password  = '6BDRZzFMvCiyYSVPZ8ODZI0Tu'
    #mqtt_topic = "III.in.MES"
    mqtt_topic = "iii.in.MES"
    client = mqtt.Client()
    client.username_pw_set(mqtt_username,mqtt_password)
    client.connect(mqtt_host, port=mqtt_port)

    try:
        client.publish(mqtt_topic,newData)
        print('----------Upload [ ' + newData + ' ] Data To InfluxDB Complete----------\n')
    except KeyboardInterrupt:
        client.disconnect()


if __name__ == "__main__":
    timeInterval = input("Time Interval: ")
    Thread(target=GenerateData).start()

    while True:
        time.sleep(int(timeInterval))
        Thread(target=GenerateData).start()
