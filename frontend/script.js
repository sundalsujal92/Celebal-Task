function sendRequest() {
    const statusDiv = document.getElementById('status');
    statusDiv.textContent = "Sending request...";

    fetch("http://<APP_TIER_PUBLIC_IP>:5000/log", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: "Button clicked from frontend" })
    })
    .then(response => response.json())
    .then(data => {
        statusDiv.textContent = "✅ Response: " + (data.status || "Success");
    })
    .catch(error => {
        console.error("Error:", error);
        statusDiv.textContent = "❌ Error: " + error.message;
    });
}
