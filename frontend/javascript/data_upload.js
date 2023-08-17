const endpoint_root = "http://127.0.0.1:8000";

function handleFileUpload() {
    const fileInput = document.getElementById("fileInput");

    fileInput.multiple = true;
    fileInput.click();

    fileInput.addEventListener("change", (event) => {
        const files = event.target.files;

        if (files.length > 0) {
            const formData = new FormData();
            for (const file of files) {
                formData.append("files", file);
            }

            fetch(endpoint_root + "/files_upload", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log(data); // Handle response from server
            })
            .catch(error => {
                console.error("Error:", error);
            });
        } else {
            console.log("No files selected.");
        }
    });
}


function handleDirectoryUpload() {
    const directoryInput = document.getElementById("directoryInput");

    directoryInput.click();

    directoryInput.addEventListener("change", async (event) => {
        const files = event.target.files;

        if (files.length > 0) {
            const formData = new FormData();
            for (const file of files) {
                formData.append("files", file);
            }

            fetch(endpoint_root + "/files_upload", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log(data); // Handle response from server
            })
            .catch(error => {
                console.error("Error:", error);
            });
        } else {
            console.log("No files selected.");
        }
    });
}
