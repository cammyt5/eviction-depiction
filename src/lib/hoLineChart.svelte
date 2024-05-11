<script>
  import * as d3 from "d3";

  import { metroBostonData } from "../data/homeOwnership/metroB.js";
  import { suffolkData } from "../data/homeOwnership/suffolkC.js";
  import { nationalData } from "../data/homeOwnership/national.js";

  /**
   * On hover: I want to create a tooltip that displays the number
   * at that year for each dataset
   */

  const transformData = (data) => {
    return [...data.objects].map((d) => {
      return {
        year: d3.timeParse("%Y")(d.year),
        rate: d.rate,
      };
    });
  };
  const dataCleaned = {
    "Metro Boston": transformData(metroBostonData),
    "Suffolk County": transformData(suffolkData),
    National: transformData(nationalData),
  };
  const allData = Object.values(dataCleaned).flat();

  // Define the dimensions and margins of the graph
  const margin = { top: 20, right: 30, bottom: 30, left: 60 },
    width = 800,
    height = 400,
    usableArea = {
      top: margin.top,
      right: width - margin.right,
      bottom: height - margin.bottom,
      left: margin.left,
    };

  usableArea.width = usableArea.right - usableArea.left;
  usableArea.height = usableArea.bottom - usableArea.top;

  let svg;
  // scales
  const xScale = d3
    .scaleTime()
    .domain(d3.extent(allData.map((d) => d.year)))
    .range([usableArea.left, usableArea.right])
    .nice();
  const yScale = d3
    .scaleLinear()
    .domain(d3.extent(allData.map((d) => d.rate)))
    .range([usableArea.bottom - 20, usableArea.top])
    .nice();
  // axes
  let xAxis, yAxis;
  $: {
    d3.select(xAxis).call(d3.axisBottom(xScale));
    d3.select(yAxis).call(d3.axisLeft(yScale));
  }

  // Define the line
  const valueLine = d3
    .line()
    .x((d) => xScale(d.year))
    .y((d) => yScale(d.rate));
  const colors = d3.scaleOrdinal(d3.schemeTableau10);

  $: {
    for (const [label, data] of Object.entries(dataCleaned)) {
      // line
      const color = colors(label);
      d3.select(svg)
        .append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", color)
        .attr("stroke-width", 1.5)
        .attr("d", valueLine);

      // label
      d3.select(svg)
        .append("text")
        .attr("x", margin.left + usableArea.width)
        .attr("y", yScale(data[data.length - 1].rate))
        .attr("text-anchor", "left")
        .style("font-size", "16px")
        .style("fill", color)
        .text(label);
    }

    // title
    d3.select(svg)
      .append("text")
      .attr("x", margin.left + usableArea.width / 2)
      .attr("y", 0)
      .attr("text-anchor", "middle")
      .style("font-size", "20px")
      .text("Homeownership Rate Over Time");
  }
</script>

<svg viewBox="0 0 {width} {height}" bind:this={svg}>
  <g transform="translate(0, {usableArea.height})" bind:this={xAxis} />
  <g transform="translate({usableArea.left}, 0)" bind:this={yAxis} />
</svg>

<style>
  svg {
    overflow: visible;
    margin: 2em auto;
  }
</style>
