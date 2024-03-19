const form = document.getElementById('fish-form');
const predictionElement = document.getElementById('prediction');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const species = document.getElementById('species').value;
  const length1 = parseFloat(document.getElementById('length1').value);
  const length2 = parseFloat(document.getElementById('length2').value);
  const length3 = parseFloat(document.getElementById('length3').value);
  const width = parseFloat(document.getElementById('width').value);

  const data = {
    species,
    length1,
    length2,
    length3,
    width,
  };

  try {
    const response = await fetch('/predict_weight', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });

    const predictionData = await response.json();
    const predictedWeight = predictionData.predicted_weight;

    predictionElement.textContent = `Predicted Weight: ${predictedWeight.toFixed(2)} cm`;

  } catch (error) {
    console.error('Error:', error);
    predictionElement.textContent = 'Error: Failed to predict weight.';
  }
});
