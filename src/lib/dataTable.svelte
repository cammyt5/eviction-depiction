<script>
  import * as d3 from "d3";

  export let data;

  data.rows.forEach((row, index) => {
    row.rank = index + 1;
  });

  const columnTitles = data.columnTitles;
  let rows = data.rows.filter((row) => row.highlight);

  let showFullList = false;
  let sortDirection = null;
  let sortByColumn = "Home Ownership Rate";
  $: {
    if (showFullList) {
      rows = data.rows;
    } else {
      rows = data.rows.filter((row) => row.highlight);
    }

    if (sortDirection !== null) {
      // Sort rows based on the current sort criteria
      if (sortByColumn === "City") {
        rows.sort((a, b) => {
          if (sortDirection === "asc") {
            return a.city.localeCompare(b.city);
          } else {
            return b.city.localeCompare(a.city);
          }
        });
      } else if (sortByColumn === "Home Ownership Rate") {
        rows.sort((a, b) => {
          if (sortDirection === "asc") {
            return a.rate - b.rate;
          } else {
            return b.rate - a.rate;
          }
        });
      } else if (sortByColumn === "Population") {
        rows.sort((a, b) => {
          if (sortDirection === "asc") {
            return a.population - b.population;
          } else {
            return b.population - a.population;
          }
        });
      }
    }
  }

  function toggleFullList() {
    showFullList = !showFullList;
  }

  function handleSort(title) {
    if (title === sortByColumn) {
      // Toggle sort direction
      sortDirection = sortDirection === "asc" ? "desc" : "asc";
    } else {
      // Reset sort direction
      sortDirection = null;
    }
    sortByColumn = title;
  }
</script>

<div id="checkbox">
  <label>
    <input type="checkbox" on:change={toggleFullList} />
    Show full list
  </label>
</div>

<table>
  <!-- Table header -->
  <thead>
    <tr>
      <th />
      {#each columnTitles as title}
        <th
          class:selected={sortByColumn === title}
          on:click={() => handleSort(title)}
        >
          {title}

          {#if sortByColumn === title}
            {sortDirection === "asc" ? "▲" : "▼"}
          {/if}
        </th>
      {/each}
    </tr>
  </thead>

  <tbody>
    <!-- Map rows from data -->
    {#each rows as row}
      <tr class:selected={row.highlight}>
        <td
          class:highlight={row.highlight}
          class:highlight-boston={row.city === "Boston"}
        >
          {row.rank}
        </td>
        <td
          class:highlight={row.highlight}
          class:highlight-boston={row.city === "Boston"}
        >
          {row.city}
        </td>
        <td
          class:highlight={row.highlight}
          class:highlight-boston={row.city === "Boston"}
        >
          {row.rate + "%"}
        </td>
        <td
          class:highlight={row.highlight}
          class:highlight-boston={row.city === "Boston"}
        >
          {row.population.toLocaleString()}
        </td>
      </tr>
    {/each}
  </tbody>
</table>

<style>
  #checkbox label,
  input {
    cursor: pointer;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.5em 0;
  }

  th {
    text-align: left;
    padding: 8px;
  }
  th:hover {
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Add a shadow effect when hovering */
    cursor: pointer;
  }
  th.selected {
    background-color: #f0f0f0; /* Change the background color for the selected column header */
  }

  td {
    padding: 8px;
    border-top: 1px solid #dddddd;
  }
  .highlight {
    font-weight: bold;
    color: #3b8dbd;
  }
  .highlight-boston {
    font-weight: bold;
    color: black; /* Change the color to black */
  }
</style>
