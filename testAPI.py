import requests

# req = {
#     "schemas" : "teste....",
#     "version" : "1.0"
# }

res = requests.get('http://localhost:5000/api/estoque/db/sinc')
if res.ok:
    print(res.content)