
// Upload File Functionality
document.getElementById('uploadFileBtn').addEventListener('click', function() {
    const fileContent = prompt("Enter file content:");
    const fileName = prompt("Enter file name:");

    fetch('https://your-api-gateway-url.amazonaws.com/prod/UploadToS3Function', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ file_content: fileContent, file_name: fileName })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.body;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Get the collapsible menu and toggle button
const collapsibleMenu = document.getElementById("collapsibleMenu");
const toggleBtn = document.getElementById("toggleBtn");

// Add an event listener for the toggle button
toggleBtn.addEventListener("click", () => {
    console.log("Changed")
    collapsibleMenu.classList.toggle("collapsed");
});

