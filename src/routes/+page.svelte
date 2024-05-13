<script>
    import Plot from "$lib/plot.svelte";
    import RangeSlider from "svelte-range-slider-pips";
    import DataTable from "../lib/dataTable.svelte";
    import HoLineChart from "../lib/hoLineChart.svelte"
    import ScrollyBarChart from "../lib/scrollyBarChart.svelte";
    import { homeOwnershipData } from "../data/tables/homeOwnership";
    import EvictionDashboard from "../lib/evictionDashboard.svelte";

    let values = [0, .2];

    let selectorValue = "";
    const menuOptions = ["Demographics", "Corporations", "Investors"];
    const optionsToFeatures = {
        "Demographics": ["majority_black", "majority_hispanic", "high_income", "low_income"],
        "Corporations": ["high_corp_buy_rate", "low_corp_buy_rate", "high_llc_buy_rate", "low_llc_buy_rate", "high_gov_buy_rate", "low_gov_buy_rate", 
                        "high_gse_buy_rate", "low_gse_buy_rate", "high_trst_buy_rate", "low_trst_buy_rate", 
                        "high_bus_buy_rate", "low_bus_buy_rate", "high_bnk_buy_rate", "low_bnk_buy_rate"],
        "Investors": ["high_non_investor_buy_rate", "low_non_investor_buy_rate", 
                    "high_small_investor_buy_rate", "low_small_investor_buy_rate", 
                    "high_medium_investor_buy_rate", "low_medium_investor_buy_rate", 
                    "high_large_investor_buy_rate", "low_large_investor_buy_rate", 
                    "high_institutional_investor_buy_rate", "low_institutional_investor_buy_rate"],
    };


    const featureNameMap = {
        "high_llc_buy_rate": "High LLC Buy Rate",
        "low_llc_buy_rate": "Low LLC Buy Rate",
        "majority_black": "Majority Black Population",
        "majority_hispanic": "Majority Hispanic Population",
        "high_income": "High Median Household Income",
        "low_income": "Low Median Household Income",
        "high_gov_buy_rate": "High Government Buyer Rate",
        "low_gov_buy_rate": "Low Government Buyer Rate",
        "high_gse_buy_rate": "High Government-Sponsored Enterprise Buyer Rate",
        "low_gse_buy_rate": "Low Government-Sponsored Enterprise Buyer Rate",
        "high_trst_buy_rate": "High Trust Buyer Rate",
        "low_trst_buy_rate": "Low Trust Buyer Rate",
        "high_bus_buy_rate": "High Business Buyer Rate",
        "low_bus_buy_rate": "Low Business Buyer Rate",
        "high_bnk_buy_rate": "High Bank Buyer Rate",
        "low_bnk_buy_rate": "Low Bank Buyer Rate",
        "high_non_investor_buy_rate": "High Non-Investor Buyer Rate",
        "low_non_investor_buy_rate": "Low Non-Investor Buyer Rate",
        "high_small_investor_buy_rate": "High Small Investor Buyer Rate",
        "low_small_investor_buy_rate": "Low Small Investor Buyer Rate",
        "high_medium_investor_buy_rate": "High Medium Investor Buyer Rate",
        "low_medium_investor_buy_rate": "Low Medium Investor Buyer Rate",
        "high_large_investor_buy_rate": "High Large Investor Buyer Rate",
        "low_large_investor_buy_rate": "Low Large Investor Buyer Rate",
        "high_institutional_investor_buy_rate": "High Institutional Investor Buyer Rate",
        "low_institutional_investor_buy_rate": "Low Institutional Investor Buyer Rate",
        "high_corp_buy_rate": "High Corporate Buy Rate",
        "low_corp_buy_rate": "Low Corporate Buy Rate"
    };

    let expandedCategory = null;

    function toggleCategory(category) {
        expandedCategory = expandedCategory === category ? null : category;
    }
    function handleFeatureSelect(feature) {
        selectorValue = feature === selectorValue ? "" : feature;
    }

    let investment = [0];
</script>

<style>
    body {
        max-width: 100ch;
        margin-left: auto;
        margin-right: auto;
        font-family: "Times New Roman", Times, serif;
    }

    h1 {
        text-align: center;
        font-size: 3em;
    }

    h2 {
        text-align: center;
    }

    p {
        font-size: 110%;
        line-height: 140%;
    }

    p.names {
        text-align: center;
        padding-bottom: 15px;
    }

    hr {
        border: 0;
        height: 8px;
    }

    hr.blue {
        background-image: linear-gradient(to right, rgba(0, 0, 0, 0), #9FD2FF, rgba(0, 0, 0, 0));
    }

    hr.yellow {
        background-image: linear-gradient(to right, rgba(0, 0, 0, 0), #FFE262, rgba(0, 0, 0, 0));
    }

    [data-tooltip]:hover::after {
        display: block;
        position: absolute;
        content: attr(data-tooltip);
        border: 1px solid black;
        background: #9FD2FF;
        margin: .5em;
        padding: .25em;
    }

    .text-tooltip {
        text-decoration-line: underline;
        text-decoration-color: #2C6DC3;
        text-decoration-thickness: 2px;
    }

    .viz-placeholder {
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-top: 3em;
        margin-bottom: 3em;
        width: 25em;
        height: 25em;
        background-color: gray;
    }

    img {
        width: 60%;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    .small-multiples-wrapper {
        display: flex;
        flex-wrap: wrap;
    }

    .small-multiple {
        flex: 0 0 calc(50% - 10px); /* 50% width with some spacing */
        margin: 5px; /* Adjust spacing between items */
    }

    .small-multiple-title {
        text-align: center;
        font: 130% bold;
        font-family: sans-serif;
    }

    .dropbtn {
        background-color: #3498db;
        color: white;
        padding: 16px;
        font-size: 16px;
        border: none;
        cursor: pointer;
    }

    /* Style the dropdown content */
    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f9f9f9;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
    }

    /* Show the dropdown menu on hover */
    .dropdown:hover .dropdown-content {
        display: block;
    }

    /* Style the dropdown item */
    .dropdown-item {
        padding: 10px;
    }

    /* Style the option title */
    .option-title {
        cursor: pointer;
        font-weight: bold;
    }

    /* Style the feature links */
    .dropdown-content a {
        display: block;
        padding: 5px 0;
    }

    .dropdown-content a:hover {
        background-color: #ddd;
    }

    h4 {
        margin-bottom: 0;
    }

    ul {
        margin: 1px;
    }

    .viz {
        margin-top: 3em;
        margin-bottom: 3em;
    }
    .container {
        display: flex;
        flex-direction: row;
    }

    .sidebar {
        width: 250px; /* Adjust as needed */
        padding: 10px;
        border-right: 1px solid #ccc; /* Optionally, add a border between sidebar and map */
    }

    .map-container {
        flex: 1;
        padding: 10px;
    }
</style>

<body>
    <hr class="blue"/><hr class="yellow"/>
    <h1>The LLC Next Door</h1>
    <h2><em>An analysis of corporate housing ownership (by corporation type) <br/>impacting eviction rates in Boston</em></h2>
    <p class="names">By Cameron Dougal, Brian Zheng, Aleksandar Jovanovic-Hacon, and Max Katz-Christy</p>
    <hr class="yellow"/><hr class="blue"/>

    <h3>In this Article</h3>
    <p>TODO - VERY SHORT SUMMARY OF TAKEAWAYS</p>

    <h3>Background: Homeownership & Renting in Boston</h3>
    <p>In the bustling streets of Boston, a city known for its rich history and vibrant culture, a quiet yet seismic shift has been occurring in the realm of housing. Over the past decade, the landscape of homeownership has undergone a remarkable transformation, with fewer Bostonians finding themselves holding the keys to their own home. The quintessential American dream of owning a home is slipping through the fingers of an increasing number of residents.</p>
    <div class="viz"><HoLineChart/></div>

    <p>When comparing home ownership rates across US cities, Boston comes in at number 24. The only city where a smaller percentage of residents own their home is New York City.</p>
    <div class="viz"><DataTable data={homeOwnershipData}/></div>

    <p style="margin-top: 5em;">To add to the difficulty of living in Boston, renters face a much higher rent burden than the national average. This is especially true for disadvantaged communities, such as black neighborhoods.</p>
    <div class="viz" style="margin-bottom: 0;"><ScrollyBarChart /></div>

    <p>The housing crisis in Boston has developed in tandem with another major phenomenon: the rise in corporate ownership across the city.</p>
    <img src="img/intro3.JPG" alt="Boston corporate ownership ownership rate over time">

    <p>The concept of "corporate ownership" calls to mind an image of large, faceless corporation barreling into a neighborhood and evicting long-time residents just to jack up rent to maximize profit. Who are these "corporate owners," really? Do they all behave the same, and are they all bad actors? In the remainder of this article, to examine the impact of corporations on each neighborhood, we will look specifically the corrolation between corporate owners and evictions.</p>

    <hr class="yellow"/>
    <h3>Corporate Ownership ≠ Evictions</h3>
    <p>Let's investigate the link between corporate ownership and evictions in Boston using a dataset of Boston evictions between 2020-2023 on the <span class="text-tooltip" data-tooltip="Roughly neighborhood-sized chunks of the city.">census tract level</span>.</p>
    <p>First, we must define a few terms: in our analysis, we define the <em>eviction rate</em> in a given census tract to be the <em>annual number of evictions filed</em> divided by the <span class="text-tooltip" data-tooltip="Determined by multiplying the census tract population by one minus the tract's owner-occupancy rate."><em>renter population</em></span>.
        
    <p>The natural first step is to compare the <em>corporate ownership rate</em> to the <em>eviction rate</em> in each census tracts. However, the resulting graph does demonstrate any obvious corrolation:</p>

    <div class="viz"><Plot fname="fig1.json" /></div>

    <p>That's because we're comparing apples to oranges: evictions happen at a distinct point in time, while the corporate ownership rate is the result of decades of compounded investment in an area. A better measure to compare against is the <em>corporate buy rate</em>, or the percentage of properties purchased by a business:</p>

    <div class="viz"><Plot fname="fig2.json" /></div>

    <hr class="blue"/>
    <h3>Not All Corporations are Equal</h3>
    <p>The term "corporate ownership" is an umbrella that covers a wide range of ownership scenarios: big banks, large companies, family businesses, live-in landlords, and even some cases of government ownership. As we consider each corporation type individually, how does the corrolation to eviction rates vary?</p>
    <p>[DEFINE TYPES, STATE HIGHEST CORROLATION]</p>

    <p>We can break down corporate purchases by investor "magnitude" and see that areas with high purchase rates by large investors and institutional investors also tend to have the highest eviction rates. In contrast, areas with high purchase rates by small investors and non-investors do not tend to have high eviction rates.</p>

    <div class="viz" style="margin-bottom: 6em;">
        <div style="height: 450px; width: 800px;">
            {#key investment}
            <Plot fname={["fig4a.json", "fig4b.json", "fig4c.json", "fig4d.json", "fig4e.json"][investment[0]]} />
            {/key}
        </div>
        <RangeSlider min={0} max={4} step={1} pipstep={1} pips float first=label last=label formatter={i => ["No Investment", "Small Investor", "Medium Investor", "Large Investor", "Institutional Investor"][i]} bind:values={investment} />
    </div>

    <p>Yet another way to consider differences between corporate owners is to analyze their intent. One practice that can be specifically disruptive is "flipping," or buying a property with the intention of quickly evicting any residents, adding value through rennovations, and putting it back on market. If we consider how quickly the average property is bought and sold, the <em>flip horizon</em>, we see that a shorter flip horizon corrolates with higher evictions.</p>

    <div class="viz"><Plot fname="fig5.json" /></div>
 
    <hr class="yellow"/>

    <h3>How Evictions Are Spatially Related to Corporate Activity (by Corporation Type) and Demographics</h3>

    <p>TODO: update to reflect refactored dashboard - These dynamics play out in geographically across Boston: areas of the city with high eviction rates also tend to have a higher corporate buy rate. Move the slider to filter neighborhoods by corporate buy rate - the higher the corporate buy rate, the more likely the neighborhood also has a high eviction rate.</p>
    <div class="container">
        <div class="sidebar">
            <EvictionDashboard selectedValue={selectorValue} dictionary={featureNameMap}/>
            <div class="dropdown">
                <button class="dropbtn">Show me areas with</button>
                <div class="dropdown-content">
                    {#each menuOptions as option}
                    <div class="dropdown-item">
                        <span class="option-title" on:click={() => toggleCategory(option)}>
                            {option}
                        </span>
                        {#if expandedCategory === option}
                        {#each optionsToFeatures[option] as feature}
                        <a on:click={() => handleFeatureSelect(feature)}>
                            {featureNameMap[feature]}
                        </a>
                        {/each}
                        {/if}
                    </div>
                    {/each}
                </div>
            </div>
        </div>
        <div class="map-container">
            <Plot fname="map2.json" filter={(data, original) => {
                if (data && data.length > 0) {
                    if (selectorValue) {
                        const filteredFeatures = original[0].geojson.features.filter(feature => feature.properties[selectorValue]);
                        data[0].geojson.features = filteredFeatures;
                    } else {
                        data[0].geojson.features = original[0].geojson.features;
                    }
                }
            }} />
        </div>
    </div>
    <hr class="blue"/>

    <h3>Conclusion</h3>
    <p>Corporate ownership is part of the complex landscape of housing in Boston. When a higher percentage of rental properties are bought by corporations in a neighborhood, that neighborhood is more likely to have a high rate of evictions. However, these corporations are not all made equal: specifically, when there are more institutional investors, businesses making large investments, and house-flippers in a neighborhood, the eviction rate is more likely to be high. Small investors and non-investors are not tied to evictions in the same way.</p>

    <h3>Attribution</h3>
    <p>This project was developed with guidance and feedback from the <a href="https://www.mapc.org/">Metropolitan Area Planning Commission (MAPC)</a>.</p>
    <h4>Data Sources</h4>
    <ul>
        <li>City of Boston Department of Neighborhood Development - Boston Housing Court Eviction Filing Records (2014-2016)</li>
        <li>City of Boston Department of Neighborhood Development - Income-Restricted Housing Database (2018)</li>
        <li>American Community Survey 5-year Estimates (2013-2017)
    </ul>
</body>
