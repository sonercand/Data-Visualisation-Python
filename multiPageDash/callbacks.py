from dash import Input, Output, callback_context, callback
from datetime import datetime
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd


@callback(Output("page-2-display-value", "children"), Input("page-2-dropdown", "value"))
def display_value(value):
    return f"You have selected {value}"


@callback(
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
        df = web.DataReader(tic, "yahoo", start=start, end=end)
        traces.append({"x": df.index, "y": df["Close"], "name": tic})
    fig = {
        "data": traces,
        "layout": {"title": stock_ticker},
    }
    return fig


@callback(Output("table", "text"), [Input("stock_picker", "value")])
def update_table(stock_picker):
    print(stock_picker)
    ticks_df = pd.read_excel(
        ".\data\WebPageListing_20191028.xlsx", skiprows=0, index_col=None
    )
    df1 = ticks_df[ticks_df["Market Name"] == "London Stock Exchange"][
        ["Name", "Symbol", "ISIN"]
    ]
    df1["Symbol"] = df1["Symbol"].apply(lambda x: x[:-1] + "." + x[-1].upper())
    data = df1[df1.Symbol.isin(stock_picker)][["Name", "ISIN"]]
    print(data)
    data_ = []
    a = {}
    a["name"] = "a"
    a["isin"] = "b"
    data_.append(a)
    return "hello world"
