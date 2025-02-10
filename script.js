document.addEventListener("DOMContentLoaded", function () {
    const downloadBtn = document.getElementById("downloadBtn");
    const videoUrl = document.getElementById("videoUrl");

    if (downloadBtn) {
        downloadBtn.addEventListener("click", function () {
            let url = videoUrl.value.trim();
            if (url === "") {
                alert("Please enter a valid video URL.");
                return;
            }

            // Placeholder function (API Integration needed)
            alert("Downloading: " + url);

            // Here, an API will be integrated to fetch and download the video.
        });
    }
});
