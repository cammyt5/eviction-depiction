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

    img {
        width: 60%;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
</style>

<body>
    <hr class="blue"/><hr class="yellow"/>
    <h1>The LLC Next Door</h1>
    <h2><em>An analysis of corporate housing ownership (by corporation type) <br/>impacting eviction rates in Boston</em></h2>
    <p class="names">By Cameron Dougal, Brian Zheng, Aleksandar Jovanovic-Hacon, and Max Katz-Christy</p>
    <hr class="yellow"/><hr class="blue"/>

    <h3>Background: Corporate Ownership on the Rise</h3>
    <img src="img/intro1.JPG" alt="Boston home ownership rate over time">
    <p>In the bustling streets of Boston, a city known for its rich history and vibrant culture, a quiet yet seismic shift has been occurring in the realm of housing. Over the past decade, the landscape of homeownership has undergone a remarkable transformation, with fewer Bostonians finding themselves holding the keys to their own abode. The quintessential American dream of owning a home, once within reach for many, now seems to be slipping through the fingers of an increasing number of residents.</p>

    <img src="img/intro2.JPG" alt="Boston eviction rate maps over time">
    <p>Yet, amidst this backdrop of corporate expansion, a curious trend emerges from our final visualization—a tale of two maps depicting the average annual eviction rates of Boston in 2014 versus 2023. Contrary to expectations, the eviction rate has notably declined, prompting us to pause and ponder: What role, if any, do these corporate entities play in this unexpected narrative of diminishing evictions?</p>

    <img src="img/intro3.JPG" alt="Boston corporate ownership ownership rate over time">
    <p>To shed light on this phenomenon, we turn our attention to the dynamics of renting, particularly in the realm of corporate landlordship. With the rise of corporate entities dominating the rental market, questions emerge regarding the impact of this shift on housing stability and community well-being. Have these corporate giants reshaped the fabric of Boston's neighborhoods, or are they merely responding to broader societal trends?</p>

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
    <p>The term "corporate ownership" is an umbrella that covers a wide range of ownership scenarios: big banks, large companies, family businesses, live-in landlords, and even some cases of government ownership. As we consider each corporation type individually, how does the corrolation to eviction rates vary?</p>

    <div class="viz-placeholder">small multiples of corporation types - w/ hover that syncs between all 6 - make sure that axes are the same across all</div>

    <p>Alternatively, we can break down corporate purchases by investor "magnitude" and see that areas with high purchase rates by large investors and institutional investors also tend to have the highest eviction rates. In contrast, areas with high purchase rates by small investors and non-investors do not tend to have high eviction rates.</p>

    <div class="viz-placeholder">small multiples of corporation sizes w/ slider that allows user to toggle which viz appears</div>

    <p>Yet another way to consider differences between corporate owners is to analyze their intent. One practice that can be specifically disruptive is "flipping," or buying a property with the intention of quickly evicting any residents, adding value through rennovations, and putting it back on market. If we consider how quickly the average property is bought and sold, the <em>flip horizon</em>, we see that a shorter flip horizon corrolates with higher evictions.</p>

    <div class="viz-placeholder">flip horizon</div>

    <hr class="yellow"/>
    <h3>Conclusion</h3>
    <p></p>


</body>


