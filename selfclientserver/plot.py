import plotly
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
import json


def create_plot(x):
    new_content=[]
    for i in range(len(list(x.keys()))//3):
        Task=x['Task'+str(i)+str(1)]
        Start=x['Start'+str(i)+str(2)]
        Finish=x['Finish'+str(i)+str(3)]
        new_content.append({'Task':Task,'Start':Start,'Finish':Finish})

    print(new_content)
    df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')
    ])

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
    fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up

    graphJSON = fig.to_json()

    return graphJSON
