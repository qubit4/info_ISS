# prints the names of astronauts currently on the ISS

def astros_info():
    import requests

    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)

    if response.status_code == 200:

        jsonresponse = response.json()
        inspace = jsonresponse["people"]
        onISS = [item["name"]
                 for item in inspace if item["craft"] == "ISS"]
        print("Astronauts currently on the ISS are: \n", onISS)

    else:
        print("Failed to read data. Status code is : {}".format(
            response.status_code))


astros_info()
