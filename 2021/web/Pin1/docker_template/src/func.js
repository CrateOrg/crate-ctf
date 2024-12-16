var strInputPw = "Input password";
var strCorrect = "CORRECT!";
var strWrong = "WRONG!";
var correctPin = "159310";

function verifyPin(pin) {
    return pin === correctPin;
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
            fetch("UyX6GGmgzWT52uKQcNfy").then(
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
