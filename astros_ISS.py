# prints the names of astronauts currently on the ISS

def astros_info():
    import requests

    url = "http://api.open-notify.org/astros.json"

    response = requests.get(url)
    jsonresponse = response.json()
    inspace = jsonresponse["people"]
    onISS = [item["name"]
             for item in inspace if item["craft"] == "ISS"]

    print("astronauts currently on the ISS are: \n", onISS)


astros_info()
