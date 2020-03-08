<?PHP
phpinfo();
$verz="1.0";

$comPort = "/dev/ttyACM0"; /*change to correct com port */

$PHP_SELF="info.php";

$fp =fopen("/dev/ttyACM0", "w") or die("Can't open port!!");
fwrite($fp, 50);
echo fgetc($fp);
fclose($fp);

?>

<HTML>
HTML Running
</HTML>
 
