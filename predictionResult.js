function displayPredictionHeading(prediction) {
   // Remove existing heading if present
    const existingHeading = document.querySelector('.prediction-heading');
    if (existingHeading) {
        existingHeading.remove();
    }

    // Create a new heading element
    const heading = document.createElement('h2');
    heading.className = 'prediction-heading';

    // Set the heading text based on the prediction value
    heading.textContent = prediction === 1 ? "Likely Manipulative" : "Likely Not Manipulative";

    // Add styles to the heading
    heading.style.textAlign = 'center';
    heading.style.color = prediction === 1 ? 'red' : 'green';
    heading.style.marginBottom = '10px';

    // Get the container element
    const container = document.querySelector('.container');

    // Insert the heading above the container
    container.parentNode.insertBefore(heading, container);
}
