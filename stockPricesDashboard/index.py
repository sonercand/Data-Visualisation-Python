from ast import Global
from audioop import mul
from pickle import GLOBAL
import dash
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd

app = dash.Dash()


# Get tickers for lse main market#
df = pd.read_excel(
    "stockPricesDashboard\data\WebPageListing_20191028.xlsx", skiprows=0, index_col=None
)


df1 = df[df["Market Name"] == "London Stock Exchange"][["Name", "Symbol", "ISIN"]]
df1["Symbol"] = df1["Symbol"].apply(lambda x: x[:-1] + "." + x[-1].upper())
df1.set_index("Symbol", inplace=True)

options = [
    {"value": tick, "label": df1["Name"].loc[tick], "ISIN": df1["ISIN"].loc[tick]}
    for tick in df1.index
]
# end #
app.layout = html.Div(
    [
        html.H1("Stock Ticker Dashboard"),
        html.Div(
            [
                html.H3("Enter a stock symbol:", style={"paddingRight": "30px"}),
                dcc.Dropdown(
                    id="stock_picker", options=options, value=["TSLA"], multi=True
                ),
            ],
            style={"display": "inline-block", "verticalAlign": "top", "width": "30%"},
        ),
        html.Div(
            [
                html.H3("Select dates"),
                dcc.DatePickerRange(
                    id="date_picker",
                    min_date_allowed=datetime(2015, 1, 1),
                    max_date_allowed=datetime.today(),
                    start_date=datetime(2020, 1, 1),
                    end_date=datetime.today(),
                ),
            ],
            style={"display": "inline-block"},
        ),
        dcc.Graph(
            id="graph",
            figure={
                "data": [{"x": [1, 2], "y": [3, 1]}],
                "layout": {"title": "Default Title"},
            },
        ),
        dcc.Graph(
            id="graph1",
            figure={
                "data": [{"x": [1, 2], "y": [3, 1]}],
                "layout": {"title": "Default Title"},
            },
        ),
    ],
)


@app.callback(
    Output("graph", "figure"),
    [
        Input("stock_picker", "value"),
        Input("date_picker", "start_date"),
        Input("date_picker", "end_date"),
    ],
)
def update_graph(stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], "%Y-%m-%d")
    end = datetime.strptime(end_date[:10], "%Y-%m-%d")
    traces = []
    for tic in stock_ticker:
        print(tic)
        df = web.DataReader(tic, "yahoo", start=start, end=end)
        traces.append({"x": df.index, "y": df["Close"], "name": tic})
    fig = {
        "data": traces,
        "layout": {"title": stock_ticker},
    }
    return fig


if __name__ == "__main__":
    app.run_server()
