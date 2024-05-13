<script>
  import * as d3 from "d3";

  import { onMount } from "svelte";

  export let fname = "";
  export let filter = (_, __) => {};
  export let filter_layout = (_, __) => {};
    // export let modify_layout = (layout) => layout;

  let fig,
    originalData = [];
  let plotDiv, plotly;

  onMount(async () => {
    fig = await d3.json(fname);
    plotDiv = document.getElementById(fname);
    originalData = JSON.parse(JSON.stringify(fig.data));
    const Plotly = await import("plotly.js-dist-min");
    Plotly.newPlot(plotDiv, fig.data, fig.layout, { showSendToCloud: false });
    plotly = Plotly;
  });

  $: {
    filter(fig?.data, originalData);
    filter_layout(fig?.layout);
    plotly?.redraw(plotDiv);
  }
</script>

<div id={fname}></div>
