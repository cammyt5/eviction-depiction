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
        "The median national rent is $15216 annually or $1268/month",
        "In Boston, these figures rise to $23772 annually or $1981 monthly",
        "The average renter household earns $41000 nationally, meaning rent costs 37.1% of earnings",
        "In Boston, renter households actually make less at $40501 annually, meaning rent costs total 58.7% of earnings",
        "Homeowner households nationally earn a household income of $78000",
        "In Boston, homeonwers earn more at $102062",
        "Further, in Boston, renter households in majority black neighborhoods earn on average $26830 annually" 
    ]

    const chartConfig = {
        width: 400,
        height: 300,
        marginTop: 30,
        marginRight: 20,
        marginBottom: 30,
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

        return svg;
    }

    function addRentLine(data, svg) {
        svg.append("line")
            .attr("x1", chartParams.marginLeft)
            .attr("y1", chartParams.yScale(data.medianAnnualRent))
            .attr("x2", chartParams.width - chartParams.marginRight)
            .attr("y2", chartParams.yScale(data.medianAnnualRent))
            .style("stroke", "black")
            .style("stroke-dasharray", "3,3");
    }
    function addBar(data, svg, labels) {
        svg.selectAll("rect").remove();
        svg.selectAll(".barText").remove();
        const x = chartParams.xScale.domain([...chartParams.xScale.domain(), ...labels]);
        const y = chartParams.yScale;

        labels.forEach(label => {
            const currentData = data.objects.find(obj => obj.label === label);

            svg.append("rect")
                .attr("x", x(label))
                .attr("y", y(currentData.value))
                .attr("width", x.bandwidth())
                .attr("height", chartParams.height - chartParams.marginBottom - y(currentData.value))
                .attr("fill", "steelblue");

            svg.append("text")
                .attr("class", "barText")
                .attr("x", x(label) + x.bandwidth() / 2)
                .attr("y", y(currentData.value) - 5)
                .attr("text-anchor", "middle")
                .text(currentData.value);
        });

    }

    // function createBarChart(data, containerId) {
    //     const width = 400;
    //     const height = 300;
    //     const marginTop = 30;
    //     const marginRight = 20;
    //     const marginBottom = 30;
    //     const marginLeft = 60;
        
    //     d3.select(containerId).select("svg").remove();

    //     const svg = d3.select(containerId)
    //         .append("svg")
    //         .attr("width", width)
    //         .attr("height", height);

    //     const x = d3.scaleBand()
    //         .domain(data.objects.map(d => d.label))
    //         .range([marginLeft, width - marginRight])
    //         .padding(0.1);

    //     const y = d3.scaleLinear()
    //         .domain([0, 111000])
    //         .range([height - marginBottom, marginTop]);

    //     svg.selectAll("rect")
    //         .data(data.objects)
    //         .enter()
    //         .append("rect")
    //         .attr("x", d => x(d.label))
    //         .attr("y", d => y(d.value))
    //         .attr("width", x.bandwidth())
    //         .attr("height", d => height - marginBottom - y(d.value))
    //         .attr("fill", "steelblue");

    //     svg.selectAll(".barText")
    //         .data(data.objects)
    //         .enter()
    //         .append("text")
    //         .attr("class", "barText")
    //         .attr("x", d => x(d.label) + x.bandwidth() / 2)
    //         .attr("y", d => y(d.value) - 5)
    //         .attr("text-anchor", "middle")
    //         .text(d => d.value); // Display the amount written out above all bars

    //     svg.append("line")
    //         .attr("x1", marginLeft)
    //         .attr("y1", y(data.medianAnnualRent))
    //         .attr("x2", width - marginRight)
    //         .attr("y2", y(data.medianAnnualRent))
    //         .style("stroke", "black")
    //         .style("stroke-dasharray", "3,3");

    //     svg.append("g")
    //         .attr("transform", `translate(0,${height - marginBottom})`)
    //         .call(d3.axisBottom(x));

    //     svg.append("g")
    //         .attr("transform", `translate(${marginLeft},0)`)
    //         .call(d3.axisLeft(y));

    //     return svg;
    // }

    onMount(() => {
        createBarChart(nationalData, "#nationalChart");
        createBarChart(bostonData, "#bostonChart");
        currentStep = 0;
    });

    function updateChart(step) {
        if (step >= 10) {
            addRentLine(nationalData, d3.select("#nationalChart svg"));
        }
        if (step >= 20) {
            addRentLine(bostonData, d3.select("#bostonChart svg"));
        }
        if (step >= 30) {
            addBar(nationalData, d3.select("#nationalChart svg"), ["Renters"]);
        }
        if (step >= 40) {
            addBar(bostonData, d3.select("#bostonChart svg"), ["Renters"]);
        }
        if (step >= 50) {
            addBar(nationalData, d3.select("#nationalChart svg"), ["Renters", "Owners"]);
        }
        if (step >= 60) {
            addBar(bostonData, d3.select("#bostonChart svg"), ["Renters", "Owners"]);
        }
        if (step >= 70) {
            addBar(bostonData, d3.select("#bostonChart svg"), ["Renters", "Owners", "Majority Black Neighborhoods"]);
        }
    }

    $: updateChart(currentStep);
</script>

<style>
    mark {
		padding: 0.5em;
		position: fixed;
		top: 0;
		right: 0;
	}
</style>

<mark>currentStep: {currentStep}</mark>

<Scrolly bind:progress={currentStep}>
    <div id="nationalChart"></div>
    <div id="bostonChart"></div>
</Scrolly>

<!-- <div id="nationalChart"></div>
<div id="bostonChart"></div> -->
