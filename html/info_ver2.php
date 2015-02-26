<?php

$verz="1.0";
$comPort = "/dev/ttyACM0"; /*change to correct com port */

if (isset($_POST["rcmd"])) {
  $rcmd = $_POST["rcmd"];
switch ($rcmd) {
  
  case Low:
    $fp =fopen($comPort, "w");
    fwrite($fp, 49); /* this is the number that it will write */
    fclose($fp);
    break;
  
  case Mid:
    $fp =fopen($comPort, "w");
    fwrite($fp, 50); /* this is the number that it will write */
    fclose($fp);
    break;
  
  case Hi:
    $fp =fopen($comPort, "w");
    fwrite($fp, 51); /* this is the number that it will write */
    fclose($fp);
    break;
  
  default:
  die('Crap, something went wrong. The page just puked.');
}

}
?>

<html>
<body>

<center><h1>Arduino from PHP Example</h1><b>Version <?php echo $verz; ?></b></center>

<form method="post" action="<?php echo $PHP_SELF;?>">
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<input type="submit" value="Low" name="rcmd">
<input type="submit" value="Mid" name="rcmd">
<input type="submit" value="Hi" name="rcmd">
<br />
<br />
<br />
<br />
<br />
<br />

</form>
</body>
</html>