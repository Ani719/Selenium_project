import requests

response_object = requests.head('https://www.youtube.com/')
#print(response_object.status_code)
print(response_object.content)
#print(response_object.headers)
#print(response_object.text)