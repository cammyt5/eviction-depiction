<script>
    import * as d3 from "d3";
    import { onMount } from 'svelte';

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
        ]
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
        ]
    };

    function createBarChart(data, containerId) {
        const width = 400;
        const height = 300;
        const marginTop = 30;
        const marginRight = 20;
        const marginBottom = 30;
        const marginLeft = 40;

        const svg = d3.select(containerId)
            .append("svg")
            .attr("width", width)
            .attr("height", height);

        const x = d3.scaleBand()
            .domain(data.objects.map(d => d.label))
            .range([marginLeft, width - marginRight])
            .padding(0.1);

        const y = d3.scaleLinear()
            .domain([0, d3.max(data.objects, d => d.value)])
            .range([height - marginBottom, marginTop]);

        svg.selectAll("rect")
            .data(data.objects)
            .enter()
            .append("rect")
            .attr("x", d => x(d.label))
            .attr("y", d => y(d.value))
            .attr("width", x.bandwidth())
            .attr("height", d => height - marginBottom - y(d.value))
            .attr("fill", "steelblue");

        svg.append("g")
            .attr("transform", `translate(0,${height - marginBottom})`)
            .call(d3.axisBottom(x));

        svg.append("g")
            .attr("transform", `translate(${marginLeft},0)`)
            .call(d3.axisLeft(y));

        return svg;
    }

    onMount(() => {
        createBarChart(nationalData, "#nationalChart");
        createBarChart(bostonData, "#bostonChart");
    });
</script>

<style>
    /* Add your styles here */
</style>

<div id="nationalChart"></div>
<div id="bostonChart"></div>
