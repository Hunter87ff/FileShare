function sel(obj){return document.querySelector(obj);}

function loader(percentage) {

    const progressBar = sel('#progressbr');

    progressBar.style.width = percentage + '%';

    sel(".btn").innerText = "Uploaded " + percentage + '%';}

const fileInput = sel('.upload-input');

fileInput.addEventListener('change', (event) => {

  const file = event.target.files[0];

  const formData = new FormData();

  formData.append('file', file);

  const xhr = new XMLHttpRequest();

  xhr.open('POST', '/fsend', true);

  xhr.upload.addEventListener('progress', (event) => {

    if (event.lengthComputable) {

      const uploaded = event.loaded;

      const total = event.total;

      const progress = Math.round((uploaded / total) * 100);

      loader(progress)}});

      

  xhr.onload = () => {

    sel(".btn").innerText="Send File";

    alert('Upload complete!');};

  xhr.send(formData);

});
