function displayPredictionHeading(prediction, emotion, personality, toxicity, bias, contradiction, entailment) {
    // Remove existing prediction heading if present
    const existingHeading = document.querySelector('.prediction-heading');
    if (existingHeading) {
        existingHeading.remove();
    }

    // Remove existing corner headings and paragraphs if present
    const existingCornerElements = document.querySelectorAll('.corner-heading, .corner-paragraph');
    existingCornerElements.forEach(element => element.remove());

    // Create the central prediction heading
    const heading = document.createElement('h2');
    heading.className = 'prediction-heading';
    heading.textContent = prediction === 1 ? "Likely Manipulative" : "Likely Not Manipulative";
    heading.style.textAlign = 'center';
    heading.style.color = prediction === 1 ? 'red' : 'green';
    heading.style.marginBottom = '10px';

    // Insert the prediction heading above the container
    const container = document.querySelector('.container');
    container.parentNode.insertBefore(heading, container);

    // Helper function to create corner or side headings and paragraphs
    function createCornerElement(headingText, paragraphText, position) {
        const cornerContainer = document.createElement('div');
        cornerContainer.style.position = 'absolute';
        cornerContainer.style.maxWidth = '200px'; // Limit width for layout
        cornerContainer.style.fontSize = '0.9em';
        cornerContainer.style.color = 'black'; // Set text color to black

        // Get the container's position and dimensions
        const containerRect = container.getBoundingClientRect();

        // Position the corner or side element based on the specified position
        switch (position) {
            case 'top-left':
                cornerContainer.style.top = `${containerRect.top}px`;
                cornerContainer.style.left = `${containerRect.left - 220}px`; // Offset far left
                break;
            case 'top-right':
                cornerContainer.style.top = `${containerRect.top}px`;
                cornerContainer.style.left = `${containerRect.right + 20}px`; // Offset far right
                break;
            case 'bottom-left':
                cornerContainer.style.bottom = `${window.innerHeight - containerRect.bottom}px`; // Align bottom with container
                cornerContainer.style.left = `${containerRect.left - 220}px`; // Offset far left
                break;
            case 'bottom-right':
                cornerContainer.style.bottom = `${window.innerHeight - containerRect.bottom}px`; // Align bottom with container
                cornerContainer.style.left = `${containerRect.right + 20}px`; // Offset far right
                break;
            case 'left-center':
                cornerContainer.style.top = `${containerRect.top + containerRect.height / 2 - 30}px`; // Center vertically
                cornerContainer.style.left = `${containerRect.left - 220}px`; // Offset to the left
                break;
            case 'right-center':
                cornerContainer.style.top = `${containerRect.top + containerRect.height / 2 - 30}px`; // Center vertically
                cornerContainer.style.left = `${containerRect.right + 20}px`; // Offset to the right
                break;
        }

        // Create the heading for the element
        const cornerHeading = document.createElement('h3');
        cornerHeading.className = 'corner-heading';
        cornerHeading.textContent = headingText;
        cornerHeading.style.margin = '0 0 5px 0';

        // Create the paragraph for the element
        const cornerParagraph = document.createElement('p');
        cornerParagraph.className = 'corner-paragraph';
        cornerParagraph.textContent = paragraphText;
        cornerParagraph.style.margin = '0';
        cornerParagraph.style.color = 'black'; // Explicitly set paragraph text to black

        // Append the heading and paragraph to the container
        cornerContainer.appendChild(cornerHeading);
        cornerContainer.appendChild(cornerParagraph);

        // Append the container to the body
        document.body.appendChild(cornerContainer);
    }

    // Add corner and side headings and paragraphs
    createCornerElement(`Emotion: ${emotion}`, "Represents the emotional tone of the text. Propagandists often use emotive language to induce the reader to react emotionally, not logically.", 'top-left');
    createCornerElement(`Personality: ${personality}`, "Indicates the personality traits inferred from the text. Manipulators will often act extroverted or speak in extremes, leading to high neuroticism scores and low agreeableness and openness scores.", 'top-right');
    createCornerElement(`Toxicity: ${toxicity}`, "Reflects the level of harmful or offensive language. This is often used to persuade by demonizing the enemy, attempting to create an us-vs-them mentality.", 'bottom-left');
    createCornerElement(`Bias: ${bias}`, "Measures the presence of bias or one-sided perspectives. Indicates if the text is more right-leaning, left-leaning, or neutral.", 'bottom-right');
    createCornerElement(`Contradiction: ${contradiction}`, "Detects contradictions present in the text. Contradictory statements can be used to confuse or manipulate readers.", 'left-center');
    createCornerElement(`Entailment: ${entailment}`, "Represents the logical connections and valid conclusions drawn from the text.", 'right-center');
}
