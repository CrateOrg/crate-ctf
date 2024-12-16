const imageInput = document.getElementById('imageInput');
const inputImage = document.getElementById('inputImage');
const shredButton = document.getElementById('shredButton');
const outputImage = document.getElementById('outputImage');
const inputPane = document.getElementById('inputPane');
let selectedfile;
outputImage.onerror = function() {
    console.error('Error loading the image from the provided URL:', outputImage.src);
    };
function scaleImageToFit(imgElement) {
    imgElement.onload = function() {
        // Check the dimensions of the image.
        let width = imgElement.width;
        let height = imgElement.height;
        
        // If either dimension is larger than 1024px, scale it down.
        if (width > 1024 || height > 1024) {
            if (width > height) {
                let scaleRatio = 1024 / width;
                imgElement.width = 1024;
                imgElement.height = height * scaleRatio;
            } else {
                let scaleRatio = 1024 / height;
                imgElement.height = 1024;
                imgElement.width = width * scaleRatio;
            }
        }
    };
}

function displayImage(pane) {
    document.getElementById('uploadLabel').style.display = 'none';
    let image = pane === inputPane ? inputImage : outputImage;
    image.style.display = 'block'; // Ensure the image is visible
    //inputImage.style.display = 'block';
		pane.classList.add('expanded');
}

imageInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            inputImage.src = e.target.result;
						displayImage(inputPane);
						scaleImageToFit(inputImage);
        }
        reader.readAsDataURL(file);
    }
});

shredButton.addEventListener('click', () => {
    if (!imageInput.files[0]) {
        alert('Shredder won\'t start without a file');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', selectedfile);
    
    fetch('upload.php', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
          alert(data.error);
        }
        else {
          outputImage.src = data.output;
          displayImage(outputPane);
          scaleImageToFit(outputImage);
        }
    })
    .catch(err => {
        console.error('Error uploading image:', err);
        alert('Error processing image. Please try again.');
    });
});


// Drag over event to prevent default behavior and provide visual feedback.
inputPane.addEventListener('dragover', (event) => {
    event.preventDefault();
    event.stopPropagation();
    inputPane.classList.add('drag-over');
});

// Drag leave and drop event to remove visual feedback.
inputPane.addEventListener('dragleave', (event) => {
    event.preventDefault();
    event.stopPropagation();
    inputPane.classList.remove('drag-over');
});

// Drop event to handle the dropped file.
inputPane.addEventListener('drop', (event) => {
    event.preventDefault();
    event.stopPropagation();
    inputPane.classList.remove('drag-over');

    // We only consider the first file in case multiple files are dropped.
    const file = event.dataTransfer.files[0];
    if (file) {
        selectedfile = event.dataTransfer.items[0].getAsFile();
        const reader = new FileReader();
        reader.onload = (e) => {
            inputImage.src = e.target.result;
						displayImage(inputPane);
        }
        reader.readAsDataURL(file);
        // Set the input field's files property to the dropped file.
        imageInput.files = event.dataTransfer.files;
    }
});

