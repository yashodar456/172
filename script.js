const tips = [
    "Turn off lights when not in use.",
    "Plant more trees to absorb CO₂.",
    "Use public transportation whenever possible.",
    "Reduce plastic usage and recycle waste.",
    "Save water by fixing leaks promptly.",
    "Use energy-efficient appliances."
];

function showTip() {
    const randomIndex = Math.floor(Math.random() * tips.length);
    document.getElementById("tip").textContent = tips[randomIndex];
}