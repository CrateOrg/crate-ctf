=================================================================================
Deployment
=================================================================================
Wordpress och mysql som körs i containers.
docker-compose up

# starta om
docker-compose down
docker-compose up -d

=================================================================================
Allmän info
=================================================================================

Plugins som är installerade efter deploy:
  * Add From Server
    För att kunna lägga till filer till wp-content som kommit dit på annat sätt än upload genom wordpress
  * Redirection
    För att kunna göra redirects för att få header-flaggor och "the dogs web" flaggan.

wordpress admin login: admin / VlX4hC&1fGWU!u1M(nN8VLeZ

Hur dumpa databasen:
  docker exec -it wordpress_1_db_1 mysqldump -u wpuser wp_db -p > wp_db.sql

TODO Ändra IP-adress till siten i wordpress (dvs backup borde tas när den väl är driftad)

=================================================================================
Flaggor
=================================================================================
######################
HTML KOMMENTAR
######################
html-kommentar på första "home"-sidan:
  2020ctf{all_TEXT_is_not_visible}

######################
HEADER FLAGS
######################
response header flaggor returneras via vissa sidor.
hello.php innehåller en 200 header:
  X-flag-part-1: 2020ctf{

wp-login.php (som är standard wordpress-filen) innehåller bara en 301 redirect till wp_login.php med header:
  X-flag-part-2: h3aderz_

404.php error 404 med header (bara apache-config, ej wordpress argument-not-found, det är eventuellt TODO)
  X-flag-part-3: r0xx}

######################
THE DOGS WEB
######################
User Agent redirect på hela siten mha Redirection-plugin: .*[Ss][Pp][Aa][Nn][Ii][Ee][Ll].*
Redirect till en uppladdad bild (wordpress/wp-content/uploads/2020/04/white-short-coated-dog-160846.jpg):
   2020ctf{all_browsers_are_not_created_equal}

######################
COMMAND INJECTION
######################
Command injections i kontaktformuläret:
enkelt php-script som gör typ system(echo $msg >> messages), php-filen innehåller även en flagga
  Kopiera .php till text? ?message=piowehjfiowef"%26%26cp%20drop_message.php%20newfile.txt%20%26%26%20echo%20"ff
  %26 = &, i.e. text" && cp drop_message.php newfile.txt && echo "ff

  Embedda base64 av filen till output
  text"%20%26%26%20cat%20drop_message.php%20%7c%20base64%20%26%26%20echo%20ff"

  2020ctf{input_sanitation_is_your_friend}

######################
BACON CIPHER
######################
Text på sidan "about cookies" är modifierad till att innehålla data som är gömd med bacon-skiffer.
Vissa bokstäver är bold, andra inte.
Ta källkoden för texten och
  s/ //g
  s/<b>.<\/b>/1/g
  s/[^1]/0/g
  
  decipher i t.ex. cyberchef: https://gchq.github.io/CyberChef/#recipe=Bacon_Cipher_Decode('Complete','0/1',false)&input=MTAwMTExMDExMDAwMTAwMDExMDExMDAxMTExMDAwMTAwMTExMDExMDAwMTAwMDExMDExMDAxMTExMDAwMDAwMTAxMDAxMTAwMTAxMDExMTAwMTAwMDAxMTAxMDEwMTAwMTExMDAxMDAwMDExMDEwMTAxMDAxMDAwMTAwMTAwMTEwMDAwMTAwMDEwMTEwMTAxMTAwMDAxMDAwMDAwMDAxMDAxMTEwMDExMDE
  
  Denna flagga skiljer sig på format, borde framgå i uppgiften:
  TWENTYTWENTYCTFOINKOINKISMELLBACON

