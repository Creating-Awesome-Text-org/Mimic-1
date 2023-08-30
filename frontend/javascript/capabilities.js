document.getElementById("box1").addEventListener("click", function() {
  window.location.href = "qa.html";
});

document.getElementById("box2").addEventListener("click", function() {
  window.location.href = "credentials.html";
});

document.getElementById("box3").addEventListener("click", function() {
  window.location.href = "generative.html";
});

document.getElementById("box4").addEventListener("click", function() {
  window.location.href = "doc_generation.html";
});

document.getElementById("box5").addEventListener("click", function() {
  window.location.href = "data_upload.html";
});


document.addEventListener('DOMContentLoaded', function() {
    const infoButton = document.querySelector('.info-icon');
    const modalOverlay = document.getElementById('modalOverlay');
    const closeButton = document.getElementById('closeButton');

    infoButton.addEventListener('click', function() {
        modalOverlay.style.display = 'flex';
    });

    closeButton.addEventListener('click', function() {
        modalOverlay.style.display = 'none';
    });
});