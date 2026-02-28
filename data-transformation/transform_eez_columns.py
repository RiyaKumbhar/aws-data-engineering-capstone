import pandas as pd

df = pd.read_csv("SAU-EEZ-242-v48-0-old.csv")

df.rename(columns={
    "fish_name": "common_name",
    "country": "fishing_entity"
}, inplace=True)

df.to_parquet("SAU-EEZ-242-v48-0.parquet")