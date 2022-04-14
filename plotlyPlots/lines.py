import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go

np.random.seed(42)
x_val = np.linspace(0, 1, 100)
y_val = np.random.randn(100)
trace0 = go.Scatter(x=x_val, y=y_val + 5, mode="markers", name="markers")
trace1 = go.Scatter(x=x_val, y=y_val, mode="lines", name="lines")
trace2 = go.Scatter(x=x_val, y=y_val + 10, mode="lines+markers", name="lines+markers")
data = [trace0, trace1, trace2]
layout = go.Layout(title="line charts")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename=".\plotlyPlots\lines.html")
