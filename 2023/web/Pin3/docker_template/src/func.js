var strInputPw = "Input password";
var strCorrect = "CORRECT!";
var strWrong = "WRONG!";

async function verifyPin(pin) {
  const rsp = await fetch('api/checkpin', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: "pin=" + pin
  });
  if (rsp.status == 200) {
    const data = await rsp.json();
    return data.auth;
  }
  else {
    return null;
  }
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
      if (input.length >= 5) {
        verifyPin(input).then(auth => {
          if (!auth) {
            pincode.className += " wrong";
            pincode.textContent = strWrong;
            document.body.style.background = "red";
          }
          else {
            pincode.textContent = strCorrect;
            document.body.style.background = "limegreen";
            setTimeout(function () {
              fetch("api/getflag", {
                headers: {
                  'auth': auth
                }
              }).then( r => 
              {
                  if (r.status == 200) {
                    r.json().then(j => {
                      flagDiv.textContent = j.flag
                    });
                  }
              });
            }, 100);
          }
        });
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
