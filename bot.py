from v1.MqttClient_testing import MobilePhone

# create and start the MQTT client
printer_client = MobilePhone(client_name="mobile_phone",
                            subscribe_topic="command/device1/response",
                            publish_topic="command/device1/request"
                            )
printer_client.run(broker="localhost",
                   port=1883
                   )

while True:
    message = input("Message to send: ")
    printer_client.send_request(message)


