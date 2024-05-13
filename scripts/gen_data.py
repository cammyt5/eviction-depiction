import json
import os
import pandas as pd
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go

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


### Demographics
data["black_percentage"] = data["nhaa"] / data["pop"]
data["hispanic_percentage"] = data["lat"] / data["pop"]

data["majority_black"] = data["black_percentage"] > 0.5
data["majority_hispanic"] = data["hispanic_percentage"] > 0.5

top_20_mhi = data["mhi"].nlargest(20)
bot_20_mhi = data["mhi"].nsmallest(20)
data["high_income"] = data["mhi"].isin(top_20_mhi)
data["low_income"] = data["mhi"].isin(bot_20_mhi)

fig1 = px.scatter(
    data,
    y="eviction_rate",
    x="corp_own_rate",
    trendline="ols",
    title="Corporate Ownership Rate vs Eviction Rate",
    labels={
        "eviction_rate": "Eviction Rate (%)",
        "corp_own_rate": "Corporate Ownership Rate (%)",
    },
)
fig1.update_traces(
    hovertemplate="Eviction Rate: %{y:.2%}<br>Corporate Ownership Rate: %{x:.2%}"
)
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
data["high_corp_buy_rate"] = data["corp_buy_rate"].nlargest(20)
data["low_corp_buy_rate"] = data["corp_buy_rate"].nsmallest(20)

fig2 = px.scatter(
    data,
    y="eviction_rate",
    x="corp_buy_rate",
    trendline="ols",
    title="Corporate Buy Rate vs Eviction Rate",
    labels={
        "eviction_rate": "Eviction Rate (%)",
        "corp_buy_rate": "Corporate Buy Rate (%)",
    },
)
fig2.update_traces(
    hovertemplate="Eviction Rate: %{y:.2%}<br>Corporate Buy Rate: %{x:.2%}"
)
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

data["high_llc_buy_rate"] = data["llc_buy_rate"].nlargest(20)
data["low_llc_buy_rate"] = data["llc_buy_rate"].nsmallest(20)

data["high_gov_buy_rate"] = data["gov_buy_rate"].nlargest(20)
data["low_gov_buy_rate"] = data["gov_buy_rate"].nsmallest(20)

data["high_gse_buy_rate"] = data["gse_buy_rate"].nlargest(20)
data["low_gse_buy_rate"] = data["gse_buy_rate"].nsmallest(20)

data["high_trst_buy_rate"] = data["trst_buy_rate"].nlargest(20)
data["low_trst_buy_rate"] = data["trst_buy_rate"].nsmallest(20)

data["high_bus_buy_rate"] = data["bus_buy_rate"].nlargest(20)
data["low_bus_buy_rate"] = data["bus_buy_rate"].nsmallest(20)

data["high_bnk_buy_rate"] = data["bnk_buy_rate"].nlargest(20)
data["low_bnk_buy_rate"] = data["bnk_buy_rate"].nsmallest(20)

fig3s = [
    px.scatter(
        data,
        y="eviction_rate",
        x=col,
        trendline="ols",
        labels={
            "eviction_rate": "Eviction Rate (%)",
            col: f"Investment Rate (%)",
        },
    )
    for col in [
        "llc_buy_rate",
        "gov_buy_rate",
        "gse_buy_rate",
        "trst_buy_rate",
        "bus_buy_rate",
        "bnk_buy_rate",
    ]
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

data["high_non_investor_buy_rate"] = data["non_investor_buy_rate"].nlargest(20)
data["low_non_investor_buy_rate"] = data["non_investor_buy_rate"].nsmallest(20)
data["high_small_investor_buy_rate"] = data["small_investor_buy_rate"].nlargest(20)
data["low_small_investor_buy_rate"] = data["small_investor_buy_rate"].nsmallest(20)
data["high_medium_investor_buy_rate"] = data["medium_investor_buy_rate"].nlargest(20)
data["low_medium_investor_buy_rate"] = data["medium_investor_buy_rate"].nsmallest(20)
data["high_large_investor_buy_rate"] = data["large_investor_buy_rate"].nlargest(20)
data["low_large_investor_buy_rate"] = data["large_investor_buy_rate"].nsmallest(20)
data["high_institutional_investor_buy_rate"] = data[
    "institutional_investor_buy_rate"
].nlargest(20)
data["low_institutional_investor_buy_rate"] = data[
    "institutional_investor_buy_rate"
].nsmallest(20)

fig4s = [
    px.scatter(
        data,
        y="eviction_rate",
        x=col,
        trendline="ols",
        title=f"{col_title} vs Eviction Rate",
        labels={
            "eviction_rate": "Eviction Rate (%)",
            col: f"% {col_title}",
        },
    )
    for col, col_title in [
        ("non_investor_buy_rate", "Non Investors"),
        ("small_investor_buy_rate", "Small Investors"),
        ("medium_investor_buy_rate", "Medium Investors"),
        ("large_investor_buy_rate", "Large Investors"),
        ("institutional_investor_buy_rate", "Institutional Investors"),
    ]
]

for i, fig in enumerate(fig4s):
    fig.update_traces(
        hovertemplate="Eviction Rate: %{y:.2%}<br>Non Investors: %{x:.2%}"
    )
    with open(f"{static_dir}/fig4{chr(ord('a') + i)}.json", "w") as f:
        f.write(fig.to_json() or "")


### Plot 5
# Eviction Rate vs Median Flip Horizon [dot w trendline]

fig5 = px.scatter(
    data,
    y="eviction_rate",
    x="median_flip_horizon",
    trendline="ols",
    title="Median Filp Horizon vs Eviction Rate",
    labels={
        "eviction_rate": "Eviction Rate (%)",
        "median_flip_horizon": "Median Flip Horizon (Months)",
    },
)
fig5.update_traces(
    hovertemplate="Eviction Rate: %{y:.2%}<br>Median Flip Horizon: %{x:.2s}"
)
fig5.update_xaxes(tickformat=".2s")

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


### MAP 2
for feature in neighborhoods["features"]:
    if feature["properties"]["pop"] > 0:
        black_percentage = feature["properties"]["nhaa"] / feature["properties"]["pop"]
        hispanic_percentage = (
            feature["properties"]["lat"] / feature["properties"]["pop"]
        )

        if black_percentage >= 0.5:
            feature["properties"]["majority_black"] = True

        if hispanic_percentage >= 0.5:
            feature["properties"]["majority_hispanic"] = True

        mhi = feature["properties"]["mhi"]

        if mhi in top_20_mhi.values:
            feature["properties"]["high_income"] = True
        elif mhi in bot_20_mhi.values:
            feature["properties"]["low_income"] = True

        ### Corporation types
        num_transactions = feature["properties"]["num_sales_transactions"]
        llc_buy_rate = feature["properties"]["buyer_llc_ind_sum"] / num_transactions
        if llc_buy_rate >= data["high_llc_buy_rate"].min():
            feature["properties"]["high_llc_buy_rate"] = True
        elif llc_buy_rate <= data["low_llc_buy_rate"].max():
            feature["properties"]["low_llc_buy_rate"] = True

        gov_buy_rate = feature["properties"]["buyer_gov_ind_sum"] / num_transactions
        if gov_buy_rate >= data["high_gov_buy_rate"].min():
            feature["properties"]["high_gov_buy_rate"] = True
        elif gov_buy_rate <= data["low_gov_buy_rate"].max():
            feature["properties"]["low_gov_buy_rate"] = True

        gse_buy_rate = feature["properties"]["buyer_gse_ind_sum"] / num_transactions
        if gse_buy_rate >= data["high_gse_buy_rate"].min():
            feature["properties"]["high_gse_buy_rate"] = True
        elif gse_buy_rate <= data["low_gse_buy_rate"].max():
            feature["properties"]["low_gse_buy_rate"] = True

        trst_buy_rate = feature["properties"]["buyer_trst_ind_sum"] / num_transactions
        if trst_buy_rate >= data["high_trst_buy_rate"].min():
            feature["properties"]["high_trst_buy_rate"] = True
        elif trst_buy_rate <= data["low_trst_buy_rate"].max():
            feature["properties"]["low_trst_buy_rate"] = True

        bus_buy_rate = feature["properties"]["buyer_bus_ind_sum"] / num_transactions
        if bus_buy_rate >= data["high_bus_buy_rate"].min():
            feature["properties"]["high_bus_buy_rate"] = True
        elif bus_buy_rate <= data["low_bus_buy_rate"].max():
            feature["properties"]["low_bus_buy_rate"] = True

        bnk_buy_rate = feature["properties"]["buyer_bnk_ind_sum"] / num_transactions
        if bnk_buy_rate >= data["high_bnk_buy_rate"].min():
            feature["properties"]["high_bnk_buy_rate"] = True
        elif bnk_buy_rate <= data["low_bnk_buy_rate"].max():
            feature["properties"]["low_bnk_buy_rate"] = True

        corp_buy_rate = (
            llc_buy_rate
            + gov_buy_rate
            + gse_buy_rate
            + trst_buy_rate
            + bus_buy_rate
            + bnk_buy_rate
        )
        if corp_buy_rate >= data["high_corp_buy_rate"].min():
            feature["properties"]["high_corp_buy_rate"] = True
        if corp_buy_rate <= data["low_corp_buy_rate"].max():
            feature["properties"]["low_corp_buy_rate"] = True

        ## Investment sizes
        total_investors = (
            feature["properties"]["sum_non_investor"]
            + feature["properties"]["sum_small_investor"]
            + feature["properties"]["sum_medium_investor"]
            + feature["properties"]["sum_large_investor"]
            + feature["properties"]["sum_institutional_investor"]
        )
        non_investor_buy_rate = (
            feature["properties"]["sum_non_investor"] / total_investors
        )
        small_investor_buy_rate = feature["properties"]["sum_small_investor"]
        medium_investor_buy_rate = (
            feature["properties"]["sum_medium_investor"] / total_investors
        )
        large_investor_buy_rate = (
            feature["properties"]["sum_large_investor"] / total_investors
        )
        institutional_investor_buy_rate = (
            feature["properties"]["sum_institutional_investor"] / total_investors
        )

        if non_investor_buy_rate >= data["high_non_investor_buy_rate"].min():
            feature["properties"]["high_non_investor_buy_rate"] = True
        elif non_investor_buy_rate <= data["low_non_investor_buy_rate"].max():
            feature["properties"]["low_non_investor_buy_rate"] = True

        if small_investor_buy_rate >= data["high_small_investor_buy_rate"].min():
            feature["properties"]["high_small_investor_buy_rate"] = True
        elif small_investor_buy_rate <= data["low_small_investor_buy_rate"].max():
            feature["properties"]["low_small_investor_buy_rate"] = True

        if medium_investor_buy_rate >= data["high_medium_investor_buy_rate"].min():
            feature["properties"]["high_medium_investor_buy_rate"] = True
        elif medium_investor_buy_rate <= data["low_medium_investor_buy_rate"].max():
            feature["properties"]["low_medium_investor_buy_rate"] = True

        if large_investor_buy_rate >= data["high_large_investor_buy_rate"].min():
            feature["properties"]["high_large_investor_buy_rate"] = True
        elif large_investor_buy_rate <= data["low_large_investor_buy_rate"].max():
            feature["properties"]["low_large_investor_buy_rate"] = True

        if (
            institutional_investor_buy_rate
            >= data["high_institutional_investor_buy_rate"].min()
        ):
            feature["properties"]["high_institutional_investor_buy_rate"] = True
        elif (
            institutional_investor_buy_rate
            <= data["low_institutional_investor_buy_rate"].max()
        ):
            feature["properties"]["low_institutional_investor_buy_rate"] = True

fig2 = go.Figure(
    go.Choroplethmapbox(
        geojson=neighborhoods,
        locations=data["GEOID"],
        featureidkey="properties.GEOID",
        z=data["eviction_rate"],
        colorscale="Viridis",
        zmin=0,
        zmax=0.2,
        # zoom=10.2,  # type: ignore
        marker_opacity=0.5,
        hovertemplate="Eviction Rate: %{z:.2%}<extra></extra>",
    )
)

# Highlight or bold the outline of all the tracts with over 50% black population
fig2.update_geos(
    visible=False,
    showcountries=False,
    showcoastlines=False,
    showland=False,
    fitbounds="locations",
)
fig2.update_traces(
    marker=dict(color="red"),
    selector=dict(type="choropleth", z=data["majority_black"]),
    hovertemplate="Corporate Ownership Rate: %{z:0%}<extra></extra>",
)
fig2.update_layout(
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    mapbox_style="carto-positron",
    mapbox_center={"lat": 42.3166909, "lon": -71.0860779},
    mapbox_zoom=10.2,
)

fig2.show()

# Save the map to map2.json
with open(f"{static_dir}/map2.json", "w") as f:
    f.write(fig2.to_json() or "")


### Map 3
with open(f"{scripts_dir}/Boston_Neighborhoods.geojson") as f:
    boston_neighborhoods = json.load(f)

corp_own_rates_over_time = pd.read_csv(
    f"{scripts_dir}/Change Over Time_Corporate Ownership & Owner Occupancy Rates in Boston Neighborhoods.csv"
)

fig = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=[
        "Corporate Ownership Rate of<br>Boston Rentals (2004)",
        "Corporate Ownership Rate of<br>Boston Rentals (2024)",
    ],
    specs=[[{"type": "mapbox"}, {"type": "mapbox"}]],
)

corp_own_rates_2004 = corp_own_rates_over_time[corp_own_rates_over_time.Year == 2004]
corp_own_rates_2024 = corp_own_rates_over_time[corp_own_rates_over_time.Year == 2024]

fig.add_trace(
    go.Choroplethmapbox(
        geojson=boston_neighborhoods,
        locations=corp_own_rates_2004["Neighborhood"],
        z=corp_own_rates_2004["corp_own_rate"],
        featureidkey="properties.blockgr2020_ctr_neighb_name",
        colorscale="Viridis",
        zmin=0,
        zmax=0.4,
        marker_opacity=0.5,
        hovertemplate="Corporate Ownership Rate: %{z:0%}<extra></extra>",
    ),
    row=1,
    col=1,
)

fig.add_trace(
    go.Choroplethmapbox(
        geojson=boston_neighborhoods,
        locations=corp_own_rates_2024["Neighborhood"],
        z=corp_own_rates_2024["corp_own_rate"],
        featureidkey="properties.blockgr2020_ctr_neighb_name",
        colorscale="Viridis",
        showscale=False,
        zmin=0,
        marker_opacity=0.5,
        hovertemplate="Corporate Ownership Rate: %{z:0%}<extra></extra>",
    ),
    row=1,
    col=2,
)

fig.update_mapboxes(
    center={"lat": 42.3166909, "lon": -71.0860779},
)
fig.update_layout(
    margin=dict(l=0, r=0, t=50, b=10),
    font=dict(
        family="Times New Roman, Times, serif",
        # size=18,
        color="black",
    ),
    hoverlabel=dict(font_family="Times New Roman, Times, serif"),
)

fig.update_layout(
    mapbox1=dict(zoom=10, style="carto-positron"),
    mapbox2=dict(zoom=10, style="carto-positron"),
)

with open(f"{static_dir}/map3.json", "w") as f:
    f.write(fig.to_json() or "")

with open(f"{static_dir}/data.json", "w") as f:
    f.write(data.to_json())
