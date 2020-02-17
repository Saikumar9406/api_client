import requests

"""!!!!!!!! GET THE TOKEN $$$$$$$$$$$$$$"""
def get_token():
    url="http://127.0.0.1:8000/authentication"
    response=requests.post(url,data={'username':'sai','password':'usha'})
    return response.json()

"""!!!!!!!!!!!! GET THE DETAILS @@@@@@@@@@@@@"""
def post_details(i):
    url=f"http://127.0.0.1:8000/classbasedapi"
    header={"Authorization":f'Token {get_token()}'}
    data={
        "sid": f"100{i}",
        "name": "sachintendulkar",
        "address": "mumbai",
        "email": "sacin@gmail.com"
    }
    response=requests.post(url,data=data,headers=header)
    print(response.text)
for i in range(20,25):
    post_details(i)


"""!!!!!!!!!!!! POST THE DETAILS @@@@@@@@@@@@@"""
def UPDATE_details(id):
    url=f"http://127.0.0.1:8000/update/{id}"
    header={"Authorization":f'Token {get_token()}'}

    response=requests.get(url,headers=header)
    print(response.text)
UPDATE_details(8)
