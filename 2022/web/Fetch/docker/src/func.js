function start() {
  var input = "";
  var fetchButton = document.getElementById("fetchButton");
  var filePath = document.getElementById("filePath");
  var outputDiv = document.getElementById("output");

  fetchButton.addEventListener('click', function() {
    if (filePath.value.includes("flag")) {
      outputDiv.textContent = "";
    }
    else {
      fetch("index.php?fetch=" + filePath.value).then(
        function(r) {
          if (r.status == 200) {
            r.text().then(function(t){
              output.textContent = t;
            });
          }
        });
    }
  });
}
