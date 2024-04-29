<svelte:head>
  <script src="https://cdn.plot.ly/plotly-latest.min.js" type="text/javascript"></script>
</svelte:head>

<script>
  import * as d3 from "d3";

  import { onMount } from "svelte";

    export let fname = "";

    let fig = [];

  onMount(async () => {
    fig = await d3.json(fname);
    let plotDiv = document.getElementById(fname);				
    Plotly.newPlot(plotDiv, fig.data, fig.layout, {showSendToCloud:false}); 
  });
</script>

<div id={fname}></div>
