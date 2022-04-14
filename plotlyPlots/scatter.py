# Using graph_objects
import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go

np.random.seed(42)
random_x = np.random.randint(1, 201, 200)
random_y = np.random.randint(1, 201, 200)
data = [
    go.Scatter(
        x=random_x,
        y=random_y,
        mode="markers",
        marker=dict(
            size=12, color="rgb(51,204,153)", symbol="pentagon", line={"width": 2}
        ),
    )
]
layout = go.Layout(
    title="Scatter Plot",
    xaxis={"title": "x axis"},
    yaxis={"title": "y axis"},
    hovermode="closest",
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="scatter.html")
