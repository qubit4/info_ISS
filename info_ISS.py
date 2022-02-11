import requests
import pandas as pd


# provides current ISS coordinates
def position_info():

    url1 = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url1)

    if response.status_code == 200:
        # dataframe
        df = pd.read_json(url1)
        df = df.drop(["message"], axis=1)
        print("Current position of the International Space Station:")
        print(df)

    else:
        print("Failed to read data. Status code is : {}".format(
            response.status_code))


# prints the names of astronauts currently on the ISS
def astros_info():

    url2 = "http://api.open-notify.org/astros.json"
    response = requests.get(url2)

    if response.status_code == 200:

        jsonresponse = response.json()
        inspace = jsonresponse["people"]
        onISS = [item["name"]
                 for item in inspace if item["craft"] == "ISS"]
        print("Astronauts currently on the ISS are:")
        print(", ".join(onISS))

    else:
        print("Failed to read data. Status code is : {}".format(
            response.status_code))


position_info()
print("\n")
astros_info()
