<script>
    import * as d3 from "d3";
    import { onMount } from 'svelte';
    import Scrolly from "svelte-scrolly";

    let nationalData = {
        "objects": [ 
            {
                label: "Renters",
                value: 41000
            }, 
            {
                label: "Owners",
                value: 78000
            },
        ],
        "medianAnnualRent": 15216,
    };
    let bostonData = {
        "objects": [ 
            {
                label: "Renters",
                value: 40501
            }, 
            {
                label: "Owners",
                value: 102062
            },
            {
                label: "Majority Black Neighborhoods",
                value: 26830
            },
        ],
        "medianAnnualRent": 23772,
    };
    let currentStep = 0;
    let steps = [
        "National Rent",
        "Boston Rent",
        "National Renter Income",
        "Boston Renter Income",
        "National Owner Income",
        "Boston Owner Income",
        "Renter Household Income in Majority Black Neighborhoods"
    ];
    let narrative = [
        "Nationally, average rent is $15,216 annually, or $1,268/month.",
        "In Boston, these figures rise to $23,772 annually, or $1,981/month.",
        "The average renter household earns $41,000 nationally, meaning rent costs 37.1% of earnings.",
        "In Boston, renter households make only $40,501 annually, meaning rent costs 58.7% of earnings.",
        "Homeowner households nationally earn a household income of $78,000.",
        "In Boston, homeowners earn more, at $102,062 - making the jump from renting to owning even more challenging.",
        "Further, in Boston, renter households in majority black neighborhoods earn, on average, $26,830 annually - meaning they face an even more unaffordable rental market." 
    ]

    const chartConfig = {
        width: 800,
        height: 250,
        marginTop: 30,
        marginRight: 200,
        marginBottom: 50,
        marginLeft: 60,
    };

    const chartParams = {
        ...chartConfig,
        yScale: d3.scaleLinear()
            .domain([0, 111000])
            .range([chartConfig.height - chartConfig.marginBottom, chartConfig.marginTop]),
        xScale: d3.scaleBand()
            .range([chartConfig.marginLeft, chartConfig.width - chartConfig.marginRight])
            .padding(0.1),
    };

    
    // //before step 0 have the outline of the charts generated
    // $: if (currentStep == 1) {
    //     //Draw dottted line on graph 1
    // } else if (currentStep == 1) {
    //     //Draw dotted line on graph 2
    // } else if (currentStep == 1) {
    //     //Draw rent bar on graph 1
    // } else if (currentStep == 1) {
    //     //Draw rent bar on graph 2
    // } else if (currentStep == 1) {
    //     //Draw owner bar on graph 1
    // } else if (currentStep == 1) {
    //     //Draw owner bar on graph 2
    // } else if (currentStep == 1) {
    //     //Draw majority black bar on graph 2
    // }
    function createBarChart(data, containerId) {
        const svg = d3.select(containerId)
            .append("svg")
            .attr("width", chartParams.width)
            .attr("height", chartParams.height);

        const x = chartParams.xScale
        const y = chartParams.yScale;

        svg.append("g")
            .attr("transform", `translate(0,${chartParams.height - chartParams.marginBottom})`)
            .call(d3.axisBottom(x));

        svg.append("g")
            .attr("transform", `translate(${chartParams.marginLeft},0)`)
            .call(d3.axisLeft(y));

        svg.append("text")
            .attr("class", "y label")
            .attr("text-anchor", "end")
            .attr("y", -2)
            .attr("x", -75)
            .attr("dy", ".75em")
            .attr("transform", "rotate(-90)")
            .text("dollars");

        return svg;
    }

    function addRentLine(data, svg) {
        const lineGroup = svg.append("g");
        lineGroup.append("line")
            .attr("x1", chartParams.marginLeft)
            .attr("y1", chartParams.yScale(data.medianAnnualRent))
            .attr("x2", chartParams.width - chartParams.marginRight)
            .attr("y2", chartParams.yScale(data.medianAnnualRent))
            .style("stroke", "black")
            .style("stroke-dasharray", "3,3");
        lineGroup.append("text")
            .attr("class", "lineText")
            .style("fill", "black")
            .text(`median annual rent`)
            .attr("x", chartParams.width - chartParams.marginRight + 2)           // set x position of left side of text
            .attr("y", chartParams.yScale(data.medianAnnualRent) + 5);          // set y pisition of bottom of text
    }
    function addBar(data, svg, labels, color) {
        // svg.selectAll("rect").remove();
        // svg.selectAll(".barText").remove();
        // svg.selectAll(".xAxisLabel").remove(); 

        const x = chartParams.xScale.domain([...chartParams.xScale.domain(), ...labels]);
        const y = chartParams.yScale;
        const currencyFormat = d3.format("$,.0f");

        labels.forEach(label => {
            const currentData = data.objects.find(obj => obj.label === label);

            svg.append("rect")
                .attr("x", x(label))
                .attr("y", y(currentData.value))
                .attr("width", x.bandwidth())
                .attr("height", chartParams.height - chartParams.marginBottom - y(currentData.value))
                .attr("fill", color);

            svg.append("text")
                .attr("class", "barText")
                .attr("x", x(label) + x.bandwidth() / 2)
                .attr("y", y(currentData.value) - 5)
                .attr("text-anchor", "middle")
                .text(currencyFormat(currentData.value));

            svg.append("text")
                .attr("class", "xAxisLabel")
                .style("font-size", "75%")
                .attr("x", x(label) + x.bandwidth() / 2)
                .attr("y", chartParams.height - 30)
                .attr("text-anchor", "middle")
                .text(label);

        });
            svg.append("text")
                .attr("class", "xlabel")
                .attr("text-anchor", "end")
                .attr("x", chartParams.width/2)
                .attr("y", chartParams.height - 5)
                .text("Average Annual Income");
    }

    onMount(() => {
        createBarChart(nationalData, "#nationalChart");
        createBarChart(bostonData, "#bostonChart");
        currentStep = 0;
    });

    function updateChart(step) {
        if (step < 6) {
            try {
                let svgNat = d3.select("#nationalChart svg");
                svgNat.selectAll("line").remove();
                svgNat.selectAll(".xlabel").remove();
                svgNat.selectAll(".lineText").remove();

            } catch (e) {
                //svgs have not been created yet, do nothing
            }
        }

        if (step >= 6) {
            let svgNat = d3.select("#nationalChart svg");
            svgNat.selectAll("rect").remove();
            svgNat.selectAll(".barText").remove();
            svgNat.selectAll(".xAxisLabel").remove();
            svgNat.selectAll(".xlabel").remove();
            svgNat.selectAll(".lineText").remove();

            let svgBos = d3.select("#bostonChart svg");
            svgBos.selectAll(".xlabel").remove();
            svgBos.selectAll(".lineText").remove();
            svgBos.selectAll("line").remove();

            addRentLine(nationalData, svgNat);
        }
        if (step >= 21) {
            let svg = d3.select("#bostonChart svg");
            svg.selectAll("rect").remove();
            svg.selectAll(".barText").remove();
            svg.selectAll(".xlabel").remove();
            svg.selectAll(".xAxisLabel").remove(); 
            addRentLine(bostonData, svg);
        }
        if (step >= 37) {
            let svg = d3.select("#nationalChart svg");
            svg.selectAll("rect").remove();
            svg.selectAll(".barText").remove();
            svg.selectAll(".xlabel").remove();
            svg.selectAll(".xAxisLabel").remove(); 
            addBar(nationalData, svg, ["Renters"], "yellow");
        }
        if (step >= 51) {
            let svg = d3.select("#bostonChart svg");
            svg.selectAll("rect").remove();
            svg.selectAll(".barText").remove();
            svg.selectAll(".xlabel").remove();
            svg.selectAll(".xAxisLabel").remove(); 
            addBar(bostonData, svg, ["Renters"], "steelBlue");
        }
        if (step >= 67) {
            let svg = d3.select("#nationalChart svg");
            svg.selectAll("rect").remove();
            svg.selectAll(".barText").remove();
            svg.selectAll(".xlabel").remove();
            svg.selectAll(".xAxisLabel").remove(); 
            addBar(nationalData, svg, ["Renters", "Owners"], "yellow");
        }
        if (step >= 80) {
            let svg = d3.select("#bostonChart svg");
            svg.selectAll("rect").remove();
            svg.selectAll(".barText").remove();
            svg.selectAll(".xlabel").remove();
            svg.selectAll(".xAxisLabel").remove(); 
            addBar(bostonData, svg, ["Renters", "Owners"], "steelBlue");
        }
        if (step >= 95) {
            let svg = d3.select("#bostonChart svg");
            svg.selectAll("rect").remove();
            svg.selectAll(".barText").remove();
            svg.selectAll(".xlabel").remove();
            svg.selectAll(".xAxisLabel").remove(); 
            addBar(bostonData, svg, ["Renters", "Owners", "Majority Black Neighborhoods"], "steelBlue");
        }
    }

    $: updateChart(currentStep);
</script>

<style>
    /* mark {
		padding: 0.5em;
		position: fixed;
		top: 0;
		right: 0;
	} */

    p.narrative {
        margin-top: 15em;
        margin-bottom: 15em;
    }

    h3 {
        margin-bottom: 0;
    }
</style>

<!-- <mark>**DEBUG** currentStep: {currentStep}</mark> -->

<Scrolly bind:progress={currentStep}>
    {#each narrative as line, index }
        <p class="narrative">{line}</p>
    {/each}
    <svelte:fragment slot="viz">
        <h3>National</h3>
        <div id="nationalChart"></div>
        <h3>Boston</h3>
        <div id="bostonChart"></div>
    </svelte:fragment>
</Scrolly>

