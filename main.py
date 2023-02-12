from v1.MqttClient import MQTTClient

# create and start the MQTT client
printer_client = MQTTClient(client_name="printer",
                            subscribe_topic="command/device1/request",
                            publish_topic="command/device1/response"
                            )

printer_client.run(broker="localhost",
                   port=1883
                   )
#delete
