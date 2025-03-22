import requests
from datetime import datetime

USERNAME = "your_username"
TOKEN = "your_token"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": "graph1",
    "name": "Python_coding",
    "unit": "hrs",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

today = datetime.now()

value_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}

# value_to_graph = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
# response = requests.post(url=value_to_graph, json=value_parameters, headers=headers)

put_pixel_params = {
    "quantity": "1",
}

# put_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20250318"
# response = requests.put(url=put_pixel, json=put_pixel_params, headers=headers)
# print(response.text)

delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20250318"
response = requests.delete(url=delete_pixel, headers=headers)
print(response.text)
