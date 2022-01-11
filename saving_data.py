import plotly.express as px
import statistics
import pandas as pd

df = pd.read_csv("savings_data_final.csv")
fig = px.scatter(df, y="quant_saved", color="rem_any")
fig.show()

import csv

with open ("savings_data_final.csv",newline="")as f:
    reader = csv.reader(f)
    savings_data = list(reader)
savings_data.pop(0)

#Finding total number of people and number of people who were reminded
total_entries = len(savings_data)
total_people_given_reminder = 0
for data in savings_data:
    if int(data[3]) == 1:
        total_people_given_reminder += 1

import plotly.graph_objs as go

fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[total_people_given_reminder, (total_entries - total_people_given_reminder)]))
fig.show()
