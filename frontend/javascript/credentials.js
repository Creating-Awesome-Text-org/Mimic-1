const endpoint_root = "http://127.0.0.1:8000";

function submitCredentials() {
    const form = document.getElementById("credentialForm");
    const formData = new FormData(form);

    fetch(endpoint_root + '/credentials', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(formData)),
        headers: {'Content-Type': 'application/json'}})
        .then(response => response.json())
        .then(data => {console.log(data);
            })
        .catch(error => {console.error('Error:', error);
                // Handle Incorrect Keys Here
            });
}