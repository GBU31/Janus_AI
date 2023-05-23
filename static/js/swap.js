const videoUpload = document.querySelector("#video-upload");
const videoName = document.querySelector("#video-name");
const imageUpload = document.querySelector("#image-upload");
const imageName = document.querySelector("#image-name");
const deepFake = document.querySelector("#deep-fake");
const loader = document.querySelector("#loader");
let selectedVideo = videoUpload.files[0];
let selectedImage = imageUpload.files[0];
loader.style.display = "none";
videoUpload.onchange = () => {
  selectedVideo = videoUpload.files[0];
  videoName.innerText = selectedVideo.name;
};

imageUpload.onchange = () => {
  selectedImage = imageUpload.files[0];
  imageName.innerText = selectedImage.name;
};

deepFake.addEventListener("click", () => {
  if (selectedVideo && selectedImage) {
    loader.style.display = "block";
    deepFake.style.display = "none";
    const formData = new FormData();
    formData.append("image", selectedImage);
    formData.append("video", selectedVideo);
    formData.append("filename.avi", selectedVideo);

    fetch("/api", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        loader.style.display = "none";

        if (!response.ok) {
          return response;
        }
        return response.blob();
      })
      .then((blob) => {
        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = url;
        link.download = "output.avi";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
        deepFake.style.display = "block";
      })
      .catch((error) => {
        loader.style.display = "none";
        console.error("Error:", error);
        deepFake.style.display = "block";
      });
  }
});