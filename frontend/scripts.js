document.getElementById("prediction-form").addEventListener("submit", function(event) {
    event.preventDefault();

    // Fetch input values
    const length1 = parseFloat(document.getElementById("length1").value);
    const length2 = parseFloat(document.getElementById("length2").value);
    const length3 = parseFloat(document.getElementById("length3").value);
    const height = parseFloat(document.getElementById("height").value);
    const width = parseFloat(document.getElementById("width").value);

    // Make prediction request
    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            length1: length1,
            length2: length2,
            length3: length3,
            height: height,
            width: width
        })
    })
    .then(response => response.json())
    .then(data => {
        // Display prediction result
        document.getElementById("prediction-result").innerText = "Predicted Weight: " + data.weight.toFixed(2) + " grams";
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
