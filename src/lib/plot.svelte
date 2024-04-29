<svelte:head>
  <script src="https://cdn.plot.ly/plotly-latest.min.js" type="text/javascript"></script>
</svelte:head>

<script>
  import * as d3 from "d3";

  import { onMount } from "svelte";

    export let fname = "";
    export let filter = (_, __) => {};

    let fig, originalData = [];
    let plotDiv, plotly;

  onMount(async () => {
    fig = await d3.json(fname);
    plotDiv = document.getElementById(fname);				
      originalData = JSON.parse(JSON.stringify(fig.data));
      Plotly.newPlot(plotDiv, fig.data, fig.layout, {showSendToCloud:false});
      plotly = Plotly;
  });

    $: {
        filter(fig?.data, originalData);
        plotly?.redraw(plotDiv); 
    }
</script>

<div id={fname}></div>
