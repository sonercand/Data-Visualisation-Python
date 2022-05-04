from dash import Dash, dcc, html, Input, Output, callback
from layouts import layout1, layout2, homeLayout
import callbacks
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)
app._favicon = "./favicon.png"
app.title = "Test App"

server = app.server

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/":
        return homeLayout
    elif pathname == "/lse-stocks":
        return layout1
    elif pathname == "/page2":
        return layout2
    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_silence_routes_logging=False)
