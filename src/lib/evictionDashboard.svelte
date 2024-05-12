<script>
    export let selectedValue = "";
    import { onMount } from "svelte";
    import data from "../data/map2/map2.json";

    let averageEvictionRateAll = 0;
    let averageEvictionRateSelected = 0;

    function calculateAverages() {
        // Calculate average eviction rate for all neighborhoods
        const totalEvictionRateAll = data.data.reduce((sum, neighborhood) => sum + neighborhood.properties.eviction_rate, 0);
        averageEvictionRateAll = totalEvictionRateAll / data.data.length;

        // Calculate average eviction rate for neighborhoods where selectedValue=true
        const filteredNeighborhoods = data.data.filter(neighborhood => {
        return neighborhood.properties[selectedValue] === true;
        });
        const totalEvictionRateSelected = filteredNeighborhoods.reduce((sum, neighborhood) => sum + neighborhood.properties.eviction_rate, 0);
        averageEvictionRateSelected = filteredNeighborhoods.length > 0 ? totalEvictionRateSelected / filteredNeighborhoods.length : 0;
    }

</script>
<div class="dashboard">
    <h3>Eviction Stats</h3>
    <p>Areas with a "{selectedValue}": <span style="color: {averageEvictionRateSelected > averageEvictionRateAll ? 'red' : 'green'}">{averageEvictionRateSelected.toFixed(2)}%</span></p>
    <p>All other areas: <span style="color: black">{averageEvictionRateAll.toFixed(2)}%</span></p>
</div>
<style>
    .dashboard {
      background-color: #f9f9f9;
      padding: 10px;
      border: 1px solid #ddd;
      border-radius: 5px;
    }
</style>