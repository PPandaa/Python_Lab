import paho.mqtt.client as mqtt


def MQTT_InfluxPublisher(newData):
    mqtt_host = "124.9.14.79"
    mqtt_port = 1883
    mqtt_username = '296efb60-c105-4721-9585-3663778f0ba4:38b893d0-077f-428b-afb2-ec26b05cb2bd'
    mqtt_password  = '6BDRZzFMvCiyYSVPZ8ODZI0Tu'
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
    publishData = '{"RunningStatus": "Run"}'
    MQTT_InfluxPublisher(publishData)