<script>
  import * as d3 from "d3";
  import * as Plot from "@observablehq/plot";

  import { metroBostonData } from "../data/homeOwnership/metroB.js";
  import { suffolkData } from "../data/homeOwnership/suffolkC.js";
  import { nationalData } from "../data/homeOwnership/national.js";

  let div;
  const parseYear = d3.timeParse("%Y");
  let data = [
    ["Metro Boston", metroBostonData.objects],
    ["Suffolk County", suffolkData.objects],
    ["National", nationalData.objects],
  ].flatMap(([Area, values]) =>
    values.map((d) => ({
      Area,
      Year: parseYear(d.year),
      Rate: d.rate,
    }))
  );

  data = data.filter((value) => value.Year > new Date(2007, 12));


  $: {
    div?.firstChild?.remove(); // remove old chart, if any

    div?.append(
      Plot.plot({
        style: "overflow: visible; width: 100%; height: 500px; font-size: 13px; font-family: 'Times New Roman', Times, serif;",
        grid: true,
        marks: [
          Plot.axisX({ label: "Year" }),
          Plot.axisY({ label: "Home Ownership Rate (%)" }),
          Plot.lineY(data, {
            x: "Year",
            y: "Rate",
            stroke: "Area",
            tip: {
              format: {
                Area: true,
                x: "%Y",
                y: (d) => d3.format(".1%")(d / 100),
              },
              fontSize: 12,
            },
          }),
          Plot.text(
            data,
            Plot.selectLast({
              x: "Year",
              y: "Rate",
              z: "Area",
              text: "Area",
              textAnchor: "start",
              fill: "Area",
              fontSize: 12,
              dx: 10,
            })
          ),
        ],
      })
    );
  }
</script>

<div bind:this={div} role="img"></div>
