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

    p.names {
        text-align: center;
        padding-bottom: 15px;
    }

    hr {
        border: 0;
        height: 3px;
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
</style>

<body>
    <hr class="blue"/><hr class="yellow"/>
    <h1>The LLC Next Door</h1>
    <h2><em>An analysis of corporate housing ownership (by corporation type) <br/>impacting eviction rates in Boston</em></h2>
    <p class="names">By Cameron Dougal, Brian Zheng, Aleksandar Jovanovic-Hacon, and Max Katz-Christy</p>
    <hr class="yellow"/><hr class="blue"/>

    <h3>Background: Corporate Ownership on the Rise</h3>
    <p></p>

    <hr class="yellow"/>
    <h3>Corporate Ownership ≠ Evictions</h3>
    <p>Let's investigate the link between corporate ownership and evictions in Boston using a dataset of Boston evictions between 2020-2023 on the <span class="text-tooltip" data-tooltip="Roughly neighborhood-sized chunks of the city.">census tract level</span>.</p>
    <p>First, we must define a few terms: in our analysis, we define the <em>eviction rate</em> in a given census tract to be the <em>annual number of evictions filed</em> divided by the <span class="text-tooltip" data-tooltip="Determined by multiplying the census tract population by one minus the tract's owner-occupancy rate."><em>renter population</em></span>.
        
    <p>The natural first step is to compare the <em>corporate ownership rate</em> to the <em>eviction rate</em> in each census tracts. However, the resulting graph does demonstrate any obvious corrolation:</p>

    <div class="viz-placeholder">ownership rate vs. evictions scatterplot</div>

    <p>That's because we're comparing apples to oranges: evictions happen at a distinct point in time, while the corporate ownership rate is the result of decades of compounded investment in an area. A better measure to compare against is the <em>corporate buy rate</em>, or the percentage of properties purchased by a business:</p>

    <div class="viz-placeholder">buy rate vs. evicions scatterplot</div>

    <p>These dynamics play out in geographically across Boston: areas of the city with high eviction rates also tend to have a higher corporate buy rate. Move the slider to filter neighborhoods by corporate buy rate - the higher the corporate buy rate, the more likely the neighborhood also has a high eviction rate.</p>

    <div class="viz-placeholder">buy rate vs. evicions map w/ slider</div>

    <hr class="blue"/>
    <h3>Not All Corporations are Equal</h3>
    <p></p>

    <hr class="yellow"/>
    <h3>Conclusion</h3>
    <p></p>


</body>


