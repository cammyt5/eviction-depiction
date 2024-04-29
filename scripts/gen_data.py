import json
import os
import pandas as pd
import plotly.express as px

scripts_dir = os.path.dirname(os.path.realpath(__file__))
static_dir = f"{os.path.dirname(scripts_dir)}/static"

data = pd.read_csv(f"{scripts_dir}/eviction_census_data.csv")
data = data[data["pop"] > 0]

### Plot 1
# Eviction Rate vs Corp Own Rate [dot w trendline]
# Tooltip: Neighborhood, Eviction Rate, Corp Own Rate
# Eviction Rate = ([2023 Eviction] + [2022 Eviction] + [2021 Eviction] + [2020 Eviction]) / ([Pop] * (1 - [Own Occ Rate]))

data["eviction_rate"] = (
    data["2023_eviction"]
    + data["2022_eviction"]
    + data["2021_eviction"]
    + data["2020_eviction"]
) / (data["pop"] * (1 - data["own_occ_rate"]))


fig1 = px.scatter(data, x="eviction_rate", y="corp_own_rate", trendline="ols")
with open(f"{static_dir}/fig1.json", "w") as f:
    f.write(fig1.to_json() or "")

### Plot 2
# Eviction Rate vs Corp Buy Rate [dot w trendline]
# Tooltip
# Corp Buy Rate = ([Buyer Llc Ind Sum] + [Buyer Bnk Ind Sum] + [Buyer Bus Ind Sum] + [Buyer Gov Ind Sum] + [Buyer Gse Ind Sum] + [Buyer Trst Ind Sum]) / [Num Sales Transactions]
data["corp_buy_rate"] = (
    data["buyer_llc_ind_sum"]
    + data["buyer_bnk_ind_sum"]
    + data["buyer_bus_ind_sum"]
    + data["buyer_gov_ind_sum"]
    + data["buyer_gse_ind_sum"]
    + data["buyer_trst_ind_sum"]
) / data["num_sales_transactions"]

fig2 = px.scatter(data, x="eviction_rate", y="corp_buy_rate", trendline="ols")
with open(f"{static_dir}/fig2.json", "w") as f:
    f.write(fig2.to_json() or "")

### Plot 3
# Eviction Rate vs LLC, Gov, GSE, Trust, Business, Bank Buy Rates [dot w trendline]
# LLC Buy Rate = [Buyer Llc Ind Sum] / [Num Sales Transactions]
# Gov Buy Rate = [Buyer Gov Ind Sum] / [Num Sales Transactions]
# GSE Buy Rate = [Buyer Gse Ind Sum] / [Num Sales Transactions]
# Trust Buy Rate = [Buyer Trst Ind Sum] / [Num Sales Transactions]
# Business Buy Rate = [Buyer Bus Ind Sum] / [Num Sales Transactions]
# Bank Buy Rate = [Buyer Bnk Ind Sum] / [Num Sales Transactions]

data["llc_buy_rate"] = data["buyer_llc_ind_sum"] / data["num_sales_transactions"]
data["gov_buy_rate"] = data["buyer_gov_ind_sum"] / data["num_sales_transactions"]
data["gse_buy_rate"] = data["buyer_gse_ind_sum"] / data["num_sales_transactions"]
data["trst_buy_rate"] = data["buyer_trst_ind_sum"] / data["num_sales_transactions"]
data["bus_buy_rate"] = data["buyer_bus_ind_sum"] / data["num_sales_transactions"]
data["bnk_buy_rate"] = data["buyer_bnk_ind_sum"] / data["num_sales_transactions"]

fig3s = [
    px.scatter(data, x="eviction_rate", y="llc_buy_rate", trendline="ols"),
    px.scatter(data, x="eviction_rate", y="gov_buy_rate", trendline="ols"),
    px.scatter(data, x="eviction_rate", y="gse_buy_rate", trendline="ols"),
    px.scatter(data, x="eviction_rate", y="trst_buy_rate", trendline="ols"),
    px.scatter(data, x="eviction_rate", y="bus_buy_rate", trendline="ols"),
    px.scatter(data, x="eviction_rate", y="bnk_buy_rate", trendline="ols"),
]

for i, fig in enumerate(fig3s):
    with open(f"{static_dir}/fig3{chr(ord('a') + i)}.json", "w") as f:
        f.write(fig.to_json() or "")

### Plot 4
# Eviction Rate vs Non, Small, Med, Large, Institutional Investor Buy Rates [dot w trendline]
# Non-Investor Buy Rate = [Sum Non Investor] / [Total Investors]
# Small Investor Buy Rate = [Sum Small Investor] / [Total Investors]
# Medium Investor Buy Rate = [Sum Medium Investor] / [Total Investors]
# Large Investor Buy Rate = [Sum Large Investor] / [Total Investors]
# Institutional Investor Buy Rate = [Sum Institutional Investor] / [Total Investors]

data["total_investors"] = (
    data["sum_non_investor"]
    + data["sum_small_investor"]
    + data["sum_medium_investor"]
    + data["sum_large_investor"]
    + data["sum_institutional_investor"]
)
data["non_investor_buy_rate"] = data["sum_non_investor"] / data["total_investors"]
data["small_investor_buy_rate"] = data["sum_small_investor"] / data["total_investors"]
data["medium_investor_buy_rate"] = data["sum_medium_investor"] / data["total_investors"]
data["large_investor_buy_rate"] = data["sum_large_investor"] / data["total_investors"]
data["institutional_investor_buy_rate"] = (
    data["sum_institutional_investor"] / data["total_investors"]
)

fig4s = [
    px.scatter(data, x="eviction_rate", y="non_investor_buy_rate", trendline="ols"),
    px.scatter(data, x="eviction_rate", y="small_investor_buy_rate", trendline="ols"),
    px.scatter(data, x="eviction_rate", y="medium_investor_buy_rate", trendline="ols"),
    px.scatter(data, x="eviction_rate", y="large_investor_buy_rate", trendline="ols"),
    px.scatter(
        data, x="eviction_rate", y="institutional_investor_buy_rate", trendline="ols"
    ),
]

for i, fig in enumerate(fig4s):
    with open(f"{static_dir}/fig4{chr(ord('a') + i)}.json", "w") as f:
        f.write(fig.to_json() or "")


### Plot 5
# Eviction Rate vs Median Flip Horizon [dot w trendline]

fig5 = px.scatter(data, x="eviction_rate", y="median_flip_horizon", trendline="ols")

with open(f"{static_dir}/fig5.json", "w") as f:
    f.write(fig5.to_json() or "")

### Map
with open(f"{scripts_dir}/evictions_with_geo.geojson") as f:
    neighborhoods = json.load(f)

# little hack to get eviction_rate in geojson
for feature in neighborhoods["features"]:
    if feature["properties"]["pop"] > 0:
        feature["properties"]["eviction_rate"] = (
            feature["properties"]["2023_eviction"]
            + feature["properties"]["2022_eviction"]
            + feature["properties"]["2021_eviction"]
            + feature["properties"]["2020_eviction"]
        ) / (feature["properties"]["pop"] * (1 - feature["properties"]["own_occ_rate"]))

fig = px.choropleth_mapbox(
    data,
    geojson=neighborhoods,
    locations="GEOID",
    featureidkey="properties.GEOID",
    color="eviction_rate",
    color_continuous_scale="Viridis",
    range_color=(0, 0.2),
    mapbox_style="carto-positron",
    zoom=11,
    center={"lat": 42.3016909, "lon": -71.1010779},
    opacity=0.5,
    labels={"unemp": "unemployment rate"},
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

with open(f"{static_dir}/map.json", "w") as f:
    f.write(fig.to_json() or "")
