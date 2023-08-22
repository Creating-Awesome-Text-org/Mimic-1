const endpoint_root = "http://127.0.0.1:8000";

function handleFileUpload() {
    const fileInput = document.getElementById("fileInput");

    // Remove existing event listener, if any
    fileInput.removeEventListener("change", handleFileInputChange);

    fileInput.multiple = true;
    fileInput.click();

    fileInput.addEventListener("change", handleFileInputChange);
}

function handleFileInputChange(event) {
    const files = event.target.files;

    if (files.length > 0) {
        const formData = new FormData();

        // Clear any existing files in the formData
        formData.delete("files");

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
}

function handleDirectoryUpload() {
    const directoryInput = document.getElementById("directoryInput");

    // Remove existing event listener, if any
    directoryInput.removeEventListener("change", handleDirectoryInputChange);

    directoryInput.click();

    directoryInput.addEventListener("change", handleDirectoryInputChange);
}

function handleDirectoryInputChange(event) {
    const files = event.target.files;

    if (files.length > 0) {
        const formData = new FormData();

        // Clear any existing files in the formData
        formData.delete("files");

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
}
