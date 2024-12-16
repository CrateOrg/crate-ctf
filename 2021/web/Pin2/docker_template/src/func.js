var strInputPw = "Input password";
var strCorrect = "CORRECT!";
var strWrong = "WRONG!";
var correctHash = "724fbb027396e86ab68c116ad40fb9b6ebba09fb";
var sha1 = CryptoJS.MD5;
var md5 = CryptoJS.SHA1;

function verifyPin(pin) {
    return md5(sha1(pin)).toString() === correctHash;
}

function start() {
  var input = "";
  var numbers = document.querySelectorAll(".number");
  var pincode = document.getElementById("pincode");
  var flagDiv = document.getElementById("flag");
  numbers = Array.prototype.slice.call(numbers);
  pincode.textContent = strInputPw;

  numbers.forEach(function (number, index) {
    number.addEventListener('click', function () {
      number.className += ' grow';
      input += number.textContent;
      pincode.textContent = input;
      if (input.length >= 6) {
        if (!verifyPin(input)) {
          pincode.className += " wrong";
          pincode.textContent = strWrong;
          document.body.style.background = "red";
        }
        else {
          pincode.textContent = strCorrect;
          document.body.style.background = "limegreen";
          setTimeout(function () {
            fetch("CkEiORRyWcQZnJml9TFy_" + input).then(
              function(r) {
                if (r.status == 200) {
                  r.text().then(function(t){
                    flagDiv.textContent = t;
                  });
                }
            });
          }, 900);
        }
        setTimeout(function () {
          pincode.textContent = strInputPw;
          input = "";
        }, 900);
        setTimeout(function () {
          document.body.className = "";
          document.body.style.background = "";
          pincode.className = "pincode";
        }, 1000);
      }
      setTimeout(function () {
        number.className = 'number';
      }, 1000);
    });
  });
}
