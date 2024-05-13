<script>
    export let selectedValue = "";
    export let dictionary = {};
    import { onMount } from "svelte";
    import data from "../data/map2/data.json";

    let averageEvictionRateAll = 3.46;
    let averageEvictionRateSelected = 0;

    onMount(() => {
        calculateAverages(); // Calculate averages when the component mounts
    });
    $: {
        console.log("selectedVal: ", selectedValue)
        console.log(data[selectedValue])
        calculateAverages();
    }

    function calculateAverages() {
        if (selectedValue === "") {
            return; // Exit function if selectedValue is empty
        }
        // Filter out null or false values for the selected value
        const selectedValueData = data[selectedValue];
        const filteredIndexes = Object.keys(selectedValueData).filter(key => selectedValueData[key] !== null && selectedValueData[key] !== false);

        // Calculate the average eviction rate for selected neighborhoods
        let totalEvictionRateSelected = 0;
        filteredIndexes.forEach(index => {
            totalEvictionRateSelected += data["eviction_rate"][index] * 100;
        });

        // Calculate the average eviction rate
        averageEvictionRateSelected = filteredIndexes.length > 0 ? totalEvictionRateSelected / filteredIndexes.length : 0;
    }

</script>
<div class="dashboard">
    <h3>Eviction Rate Comparison</h3>
    {#if selectedValue === ""}
        <p>Boston overall average eviction rate: <span style="color: black">{averageEvictionRateAll.toFixed(2)}%</span></p>
    {:else}
        <p>Areas with a {dictionary[selectedValue]}: <span style="color: {averageEvictionRateSelected > averageEvictionRateAll ? 'red' : 'green'}">{averageEvictionRateSelected.toFixed(2)}%</span></p>
        <p>All other areas: <span style="color: black">{averageEvictionRateAll.toFixed(2)}%</span></p>
    {/if}
</div>

<style>
    .dashboard {
      background-color: #f9f9f9;
      padding: 10px;
      border: 1px solid #ddd;
      border-radius: 5px;
    }
</style>