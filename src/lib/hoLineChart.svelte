<script>
    import * as d3 from "d3";

    import metroBostonData from "../data/homeOwnership/metroB.js"
    import suffolkData from "../data/homeOwnership/suffolkC.js"
    import nationalData from "../data/homeOwnership/national.js"
    
    /**
     * Want to create a line chart with the data from each json
     * I want each line labeled and colored differently
     * 
     * On hover; I want to create a tooltip that displays the number
     * at that year for each dataset
     * 
     * 
     * 
     * 
    */

   // Define the dimensions and margins of the graph
    const margin = { top: 20, right: 30, bottom: 30, left: 60 },
        width = 800 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

    // Append the SVG object to the body of the page
    const svg = d3
        .select("body")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // Parse the date/time
    const parseYear = d3.timeParse("%Y");

    // Set the ranges
    const x = d3.scaleTime().range([0, width]);
    const y = d3.scaleLinear().range([height, 0]);

    // Define the line
    const valueline = d3
        .line()
        .x(function (d) {
            return x(d.year);
        })
        .y(function (d) {
            return y(d.rate); // Updated to 'rate'
        });

    // Format the data
    const formatData = (data) => {
        return data.objects.map((d) => ({
            year: parseYear(d.year),
            rate: d.rate // Updated to 'rate'
        }));
        };

    // Load the data
    const loadData = (data) => {
        const formattedData = formatData(data);
            // Scale the range of the data
            x.domain(
                d3.extent(formattedData, function (d) {
                return d.year;
                })
            );
        y.domain([
            d3.min(formattedData, function (d) {
            return d.rate;
            }) - 5,
            d3.max(formattedData, function (d) {
            return d.rate;
            }) + 5,
        ]);

        // Add the valueline path
        svg
            .append("path")
            .data([formattedData])
            .attr("class", "line")
            .attr("d", valueline);

        // Add the X Axis
        svg
            .append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));

        // Add the Y Axis
        svg.append("g").call(d3.axisLeft(y));

        // Add a title to the graph
        svg
            .append("text")
            .attr("x", width / 2)
            .attr("y", 0 - margin.top / 2)
            .attr("text-anchor", "middle")
            .style("font-size", "16px")
            .text("Homeownership Rate Over Time");
    };

    // Load data for each dataset
    loadData(metroBostonData);
    loadData(suffolkData);
    loadData(nationalData);

</script>
<p>Hello</p>