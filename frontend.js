function storeInput() {
    const inputText = document.getElementById('user-input').value;
    console.log(inputText);

    const loadingBar = document.querySelector('.loading-bar');
    const completeMessage = document.querySelector('.complete-message');
    const button = document.querySelector('button'); // Add button reference here

    // Show loading bar
    loadingBar.style.display = 'block';
    completeMessage.style.display = 'none';

    // Simulate loading
    setTimeout(() => {
        loadingBar.style.display = 'none';
        completeMessage.style.display = 'block';

        // Check the input text for color conditions
        if (inputText.toLowerCase().includes("red")) {
            document.body.style.backgroundColor = "#ab3044";
            button.style.backgroundColor = "#6b1e2b";
            completeMessage.style.color = "#6b1e2b";
            updateSparkleColor("red");
        } else if (inputText.toLowerCase().includes("green")) {
            document.body.style.backgroundColor = "#30ab69";
            button.style.backgroundColor = "#1e6b42";
            completeMessage.style.color = "#1e6b42";
            updateSparkleColor("green");
        } else {
            document.body.style.backgroundColor = ""; // Keep default background
            button.style.backgroundColor = "#8c00ff"; // Reset button color
            completeMessage.style.color = "#8c00ff"; // Reset message color
            updateSparkleColor("default");
        }
    }, 2000);
}

document.addEventListener('mousemove', (event) => {
    const sparkle = document.createElement('div');
    sparkle.className = 'sparkle';
    sparkle.style.left = `${event.pageX}px`;
    sparkle.style.top = `${event.pageY}px`;
    document.body.appendChild(sparkle);

    setTimeout(() => {
        sparkle.remove();
    }, 700);
});

function updateSparkleColor(color) {
    const style = document.createElement('style');
    style.id = 'sparkle-color';

    if (color === "red") {
        style.innerHTML = `.sparkle { background: radial-gradient(circle, white, #6b1e2b); box-shadow: 0 0 8px rgba(255, 0, 0, 0.8); }`;
    } else if (color === "green") {
        style.innerHTML = `.sparkle { background: radial-gradient(circle, white, #1e6b42); box-shadow: 0 0 8px rgba(0, 255, 0, 0.8); }`;
    } else {
        style.innerHTML = `.sparkle { background: radial-gradient(circle, white, #8c00ff); box-shadow: 0 0 8px #d4a0ff; }`;
    }

    const existingStyle = document.getElementById('sparkle-color');
    if (existingStyle) {
        existingStyle.replaceWith(style);
    } else {
        document.head.appendChild(style);
    }
}