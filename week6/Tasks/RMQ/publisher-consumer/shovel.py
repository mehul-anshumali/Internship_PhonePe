import requests

API_ENDPOINT = 'http://192.168.178.128:15672/api/parameters/shovel/testvhost/my-shovel'

headers = {'content-type': 'application/json'}

data = {
  "value": {
    "src-protocol": "amqp091",
    "src-uri": "amqp://mehul:mehul@/testvhost",
    "src-queue": "DATA",
    "dest-protocol": "amqp091",
    "dest-uri": "amqp://mehul:mehul@/testvhost",
    "dest-queue": "DATA_SIDELINE"
  }
}

req = requests.put(url = API_ENDPOINT ,auth=('mehul', 'mehul'), json = data, headers=headers)
