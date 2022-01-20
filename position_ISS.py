# provides current ISS coordinates

def position_info():
    import requests
    import pandas as pd

    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)

    if response.status_code == 200:

        # dataframe
        df = pd.read_json(url)
        df["latitude"] = df.loc["latitude", "iss_position"]
        df["longitude"] = df.loc["longitude", "iss_position"]
        df.reset_index(inplace=True)
        df = df.drop(["index", "message"], axis=1)
        print(df)

    else:
        print("Failed to read data. Status code is : {}".format(
            response.status_code))


position_info()
