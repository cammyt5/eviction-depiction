<svelte:head>
  <script src="https://cdn.plot.ly/plotly-latest.min.js" type="text/javascript"></script>
</svelte:head>

<script>
  import * as d3 from "d3";

  import { onMount } from "svelte";

    export let fname = "";
    export let filter = (fig) => fig;

    let fig, filteredFig = [];
    let plotDiv, plotly;

  onMount(async () => {
    fig = await d3.json(fname);
    plotDiv = document.getElementById(fname);				
      plotly = Plotly;
  });

    $: filteredFig = filter(fig);

    $: {
        plotly?.newPlot(plotDiv, filteredFig.data, filteredFig.layout, {showSendToCloud:false}); 
    }
</script>

<div id={fname}></div>
