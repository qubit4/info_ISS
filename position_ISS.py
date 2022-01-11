# provides current ISS coordinates

def position_info():
    import pandas as pd

    url = "http://api.open-notify.org/iss-now.json"

    # dataframe
    df = pd.read_json(url)
    df["latitude"] = df.loc["latitude", "iss_position"]
    df["longitude"] = df.loc["longitude", "iss_position"]
    df.reset_index(inplace=True)
    df = df.drop(["index", "message"], axis=1)
    print(df)


position_info()
