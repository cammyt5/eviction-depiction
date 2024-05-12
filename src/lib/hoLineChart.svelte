<script>
  import * as Plot from "@observablehq/plot";

  import { metroBostonData } from "../data/homeOwnership/metroB.js";
  import { suffolkData } from "../data/homeOwnership/suffolkC.js";
  import { nationalData } from "../data/homeOwnership/national.js";

  let div;
  const data = [
    ["Metro Boston", metroBostonData.objects],
    ["Suffolk County", suffolkData.objects],
    ["National", nationalData.objects],
  ].flatMap(([Area, values]) => values.map((d) => ({ Area, ...d })));

  $: {
    div?.firstChild?.remove(); // remove old chart, if any

    div?.append(
      Plot.plot({
        style: "overflow: visible;",
        grid: true,
        marks: [
          //Plot.ruleY([0]),  // start y-axis at 0
          Plot.lineY(data, {
            x: "year",
            y: "rate",
            stroke: "Area",
            tip: true,
          }),
          Plot.text(
            data,
            Plot.selectLast({
              x: "year",
              y: "rate",
              z: "Area",
              text: "Area",
              textAnchor: "start",
              dx: 10,
            })
          ),
        ],
      })
    );
  }
</script>

<div bind:this={div} role="img"></div>
