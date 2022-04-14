from turtle import color
import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import numpy as np

app = dash.Dash(url_base_pathname="/dash/")
np.random.seed(42)
rx = np.random.randint(1, 101, 100)
ry = np.random.randint(1, 101, 100)

app.layout = html.Div(
    [
        dcc.Graph(
            id="scatterPlot",
            figure=dict(
                data=[go.Scatter(x=rx, y=ry, mode="markers")],
                layout=go.Layout(title="Scatter Plot"),
            ),
        )
    ]
)
if __name__ == "__main__":
    app.run_server()
