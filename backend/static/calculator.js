async function calculate() {
    try {
        console.log("Starting calculation...");
        
        // Get input values
        const baseYield = parseFloat(document.getElementById('baseYield').value);
        const rewardYield = parseFloat(document.getElementById('rewardYield').value);
        const baseExpected = parseFloat(document.getElementById('baseExpected').value) / 100;
        const rewardExpected = parseFloat(document.getElementById('rewardExpected').value) / 100;

        console.log("Input values:", {baseYield, rewardYield, baseExpected, rewardExpected});

        // Call backend API
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                base_yield: baseYield,
                reward_yield: rewardYield,
                base_expected_yield: baseExpected,
                reward_expected_yield: rewardExpected
            })
        });

        console.log("API response status:", response.status);
        const results = await response.json();
        console.log("API results:", results);
        console.log("Total expected yield value exists:", 'total_expected_yield_percentage' in results);
        console.log("Total expected yield value:", results.total_expected_yield_percentage);

        // Format all percentage values consistently
        results.total_expected_yield_percentage = (results.total_expected_yield_percentage * 100).toFixed(2);
        console.log("Formatted value:", results.total_expected_yield_percentage);

        // Display results
        const resultsDiv = document.getElementById('results');
        if (!resultsDiv) {
            throw new Error("Results div not found");
        }
        
        resultsDiv.innerHTML = `
        <div class="result-item"><strong>TVL:</strong> ${results.tvl}</div>
        <div class="result-item"><strong>Base Tranche Thickness:</strong> ${results.base_tranche_percent}%</div>
        <div class="result-item"><strong>Reward Tranche Thickness:</strong> ${results.reward_tranche_percent}%</div>
        <div class="result-item"><strong>Base Actual Yield:</strong> ${results.base_actual_yield}</div>
        <div class="result-item"><strong>Reward Actual Yield:</strong> ${results.reward_actual_yield}</div>
        <div class="result-item"><strong>Total Actual Yield:</strong> ${results.total_actual_yield}</div>
        <div class="result-item"><strong>Base Actual Tranche Yield:</strong> ${results.base_actual_tranche_yield}%</div>
        <div class="result-item"><strong>Reward Actual Tranche Yield:</strong> ${results.reward_actual_tranche_yield}%</div>
        <div class="result-item"><strong>Total Actual Tranche Yield:</strong> ${results.total_actual_tranche_yield}%</div>
        <div class='result-item"><strong>Total Expected Yield Percentage:</strong> ${results.total_expected_yield_percentage}%</div>
    `;
    } catch (error) {
        console.error("Calculation error:", error);
        const resultsDiv = document.getElementById('results');
        if (resultsDiv) {
            resultsDiv.innerHTML = `<div class="error">Error: ${error.message}</div>`;
        }
    }
}
