from turtle import color
import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import numpy as np

external_stylesheets = [
    {
        "href": "https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css",
        "rel": "stylesheet",
        "integrity": "sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm",
        "crossorigin": "anonymous",
    },
]
external_scripts = [
    "https://www.google-analytics.com/analytics.js",
    {"src": "https://cdn.polyfill.io/v2/polyfill.min.js"},
    {
        "src": "https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js",
        "integrity": "sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=",
        "crossorigin": "anonymous",
    },
]

app = dash.Dash(
    url_base_pathname="/dash/",
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
)
np.random.seed(42)
rx = np.random.randint(1, 101, 100)
ry = np.random.randint(1, 101, 100)

app.layout = html.Div(
    className="container",
    style={"min-height": "100em"},
    children=[
        html.Div(
            className="row",
            style={"min-height": "40em", "border": "1px green solid"},
            children=[
                dcc.Graph(
                    id="scatterPlot",
                    className="col",
                    style={"min-height": "20em", "border": "1px green solid"},
                    figure=dict(
                        data=[go.Scatter(x=rx, y=ry, mode="markers")],
                        layout=go.Layout(
                            title="Scatter Plot",
                            xaxis=dict(title="X Axis"),
                            yaxis=dict(title="Y Axis"),
                        ),
                    ),
                ),
                dcc.Graph(
                    className="col",
                    id="scatterPlot2",
                    style={"min-height": "20em", "border": "1px green solid"},
                    figure=dict(
                        data=[go.Scatter(x=rx, y=ry, mode="markers")],
                        layout=go.Layout(
                            title="Scatter Plot",
                            xaxis=dict(title="X Axis"),
                            yaxis=dict(title="Y Axis"),
                        ),
                    ),
                ),
            ],
        ),
        html.Div(
            className="row",
            style={"min-height": "40em", "border": "1px green solid"},
            children=[
                dcc.Graph(
                    id="barChart1",
                    className="col",
                    style={"min-height": "20em", "border": "1px green solid"},
                    figure=dict(
                        data=[go.Bar(x=rx, y=ry, type="bar")],
                        layout=go.Layout(
                            title="Scatter Plot",
                            xaxis=dict(title="X Axis"),
                            yaxis=dict(title="Y Axis"),
                        ),
                    ),
                ),
                dcc.Graph(
                    className="col",
                    id="barChart2",
                    style={"min-height": "20em", "border": "1px green solid"},
                    figure=dict(
                        data=[go.Bar(x=rx, y=ry, type="bar")],
                        layout=go.Layout(
                            title="Scatter Plot",
                            xaxis=dict(title="X Axis"),
                            yaxis=dict(title="Y Axis"),
                        ),
                    ),
                ),
            ],
        ),
    ],
)
if __name__ == "__main__":
    app.run_server()
