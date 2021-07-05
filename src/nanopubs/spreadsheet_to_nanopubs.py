import os
import pandas as pd
import json


# https://docs.google.com/spreadsheets/d/1fCykLEgAd2Z7nC9rTcW296KtBsFBBZMD8Yghcwv4WaE/edit#gid=1574253813
googledocs_id = '1fCykLEgAd2Z7nC9rTcW296KtBsFBBZMD8Yghcwv4WaE'
sheet = 'Load'

# Build URL to download CSV from google docs
googledocs_url = 'https://docs.google.com/spreadsheets/d/' + googledocs_id + '/gviz/tq?tqx=out:csv&sheet=' + sheet

## Load csv to a pandas dataframe from the URL
df = pd.read_csv(googledocs_url)
## Read from local to dev faster:
# df = pd.read_csv('data/data.csv')

