const button_rectangle = document.getElementById("Rectangle_12");
const upload_text = document.getElementById("UPLOAD");

const fileInput = document.getElementById("fileInput");

button_rectangle.addEventListener("click", function () {
  fileInput.click(); // Trigger the file input when the button is clicked
});

fileInput.addEventListener("change", function () {
  const selectedFile = fileInput.files[0];
  if (fileInput.files.length === 0) {
    alert("Please select a file");
    return;
  }

  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append("uploadedFile", file);
  alert("File Success Upload");
});

button_rectangle.addEventListener("mouseover", function () {
  upload_text.style.color = "white";
});

button_rectangle.addEventListener("mouseout", function () {
  upload_text.style.color = "black";
});
