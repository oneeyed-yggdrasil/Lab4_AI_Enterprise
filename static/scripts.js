document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('fish-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting normally

        const formData = new FormData(form);

        // Convert form data to JSON object
        const jsonObject = {};
        formData.forEach(function(value, key) {
            jsonObject[key] = value;
        });

        // Send form data to Flask backend as JSON
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonObject)
        })
        .then(response => response.json())
        .then(data => {
            // Display prediction results
            displayPrediction(data.prediction);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    function displayPrediction(prediction) {
        const resultContainer = document.getElementById('prediction-result');
        resultContainer.innerHTML = `Predicted Weight: ${prediction} grams`;
    }
});
