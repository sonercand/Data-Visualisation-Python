from dash import dcc, dash_table
from dash import html
from dash.dependencies import Input, Output
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd
import dash_bootstrap_components as dbc

# Get tickers for lse main market#
ticks_df = pd.read_excel(
    ".\data\WebPageListing_20191028.xlsx", skiprows=0, index_col=None
)
df1 = ticks_df[ticks_df["Market Name"] == "London Stock Exchange"][
    ["Name", "Symbol", "ISIN"]
]
df1["Symbol"] = df1["Symbol"].apply(lambda x: x[:-1] + "." + x[-1].upper())
df1.set_index("Symbol", inplace=True)

options = [tick for tick in df1.index]
#####
nav = dbc.Nav(
    [
        dbc.NavLink("LSE Stocks", active=True, href="/lse-stocks"),
        dbc.NavLink("Page 2", href="/page2"),
        dbc.NavLink("Home", href="/"),
    ]
)
###

homeLayout = html.Div(nav)
layout1 = html.Div(
    [
        nav,
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(html.P(id="Table")),
                        dbc.Col(
                            [
                                html.H2("Stock Prices"),
                                html.Hr(),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            html.Div(
                                                [
                                                    html.H3(
                                                        "Enter a stock symbol:",
                                                        style={
                                                            "padding": "0",
                                                            "line-height": "2em",
                                                            "bottom": "0",
                                                            "vertical-align": "center",
                                                            "height": "2em",
                                                            "color": "brown",
                                                        },
                                                    ),
                                                    dcc.Dropdown(
                                                        id="stock_picker",
                                                        options=options,
                                                        value=["TSLA"],
                                                        multi=True,
                                                        style={
                                                            "line-height": "2em",
                                                            "bottom": "0",
                                                            "vertical-align": "center",
                                                            "color": "brown",
                                                        },
                                                    ),
                                                ]
                                            )
                                        ),
                                        dbc.Col(
                                            html.Div(
                                                [
                                                    html.H3(
                                                        "Select dates",
                                                        style={
                                                            "padding": "0",
                                                            "line-height": "2em",
                                                            "color": "brown",
                                                        },
                                                    ),
                                                    dcc.DatePickerRange(
                                                        id="date_picker",
                                                        min_date_allowed=datetime(
                                                            2015, 1, 1
                                                        ),
                                                        max_date_allowed=datetime.today(),
                                                        start_date=datetime(2020, 1, 1),
                                                        end_date=datetime.today(),
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                ),
                                dbc.Row(
                                    dbc.Col(
                                        html.Div(
                                            dcc.Graph(
                                                id="graph",
                                                figure={
                                                    "data": [
                                                        {"x": [1, 2], "y": [3, 1]}
                                                    ],
                                                    "layout": {
                                                        "title": "Default Title"
                                                    },
                                                },
                                            ),
                                        )
                                    )
                                ),
                            ],
                            style={
                                "background": "white",
                                "padding": "2px",
                                "border-width": "1px",
                                "border-color": "#ccc",
                                "border-style": "solid",
                                "padding": "1em",
                            },
                        ),
                    ]
                ),
            ]
        ),
    ]
)

layout2 = html.Div(
    [
        nav,
        html.H3("Page 2"),
        dcc.Dropdown(
            {f"Page 2 - {i}": f"{i}" for i in ["London", "Berlin", "Paris"]},
            id="page-2-dropdown",
        ),
        html.Div(id="page-2-display-value"),
        dcc.Link("Go to Page 1", href="/lse-stocks"),
    ]
)
