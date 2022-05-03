import pandas as pd

df = pd.read_excel(
    "stockPricesDashboard\data\WebPageListing_20191028.xlsx", skiprows=0, index_col=None
)
df1 = df[df["Market Name"] == "London Stock Exchange"][["Name", "Symbol", "ISIN"]]
df1["Symbol"] = df1["Symbol"].apply(lambda x: x[:-1] + "." + x[-1].upper())
df1.set_index("Symbol", inplace=True)
options = [{"label": tick, "name": df1["Name"].loc[tick]} for tick in df1.index]
print(options)
