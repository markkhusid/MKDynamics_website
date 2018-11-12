<!DOCTYPE html>

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-58919029-1', 'auto');
  ga('send', 'pageview');

</script>

<html>

<head>
  <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
  <meta name="robots" content="nofollow" />
  
  <title>
    MK Dynamics - Exploring PHP
  </title>
  
  <link href="../css/styles.css" type = "text/css" rel = "stylesheet" />
  
</head>

<body>


  <h1> 
    <big> <big> MK Dynamics </big> </big>
  </h1>


  <h2>
    Exploring PHP
  </h2>

  <div id="nav">
    <ul>
      <li> <a href="../index.php">Home</a> </li>
    </ul>
  </div>
  
  <hr />
  
  <img src="../images/spacey.jpg" alt ="Space" class = "align-center medium" />

  <div id="content">
    <h3>
    	Using PHP to control the Arduino
    </h3>
    
    <p> <b> Arduino Code </b> <br>  
      The following code is uploaded to an Arduino UNO R3.  It listens to the serial port and <br>
      activates a digital I/O pin based on the number it received from the serial port.  If it received <br>
      a "1", then it illuminates the first LED, if it receives a "2", then it illuminated the second LED, <br>
      if it receives a "3", it illuminates the third LED.<br>
      The code is shown below:<br><br><br>
      
      <iframe
	  src = "code_arduino/PHP_Control_of_Arduino.ino.txt"
	  width = "550"
	  height = "300"
	  frameborder = "1"
	  scrolling = "yes">
      </iframe><br>
    </p>
    
    <p> <b>PHP Code</b><br>
      The following PHP is run within an HTML page.  It opens the serial port and sends data to the Arduino. <br>
      <iframe
	  src = "code_arduino/PHP_code_to_control_arduino.txt"
	  width = "550"
	  height = "300"
	  frameborder = "1"
	  scrolling = "yes">
      </iframe><br>
    </p>
  </div>
  
  <?PHP
    echo "This is coming out of PHP, and is being interpreted by the PHP processor...<br>";
        
    $comPort = "/dev/ttyACM0"; /*change to correct com port */
    $fp =fopen("/dev/ttyACM0", "w") or die("Can't open port!!");
    
    $count = 1;
    while ($count <=5)
    {
      echo "Now outputting a 1 onto the serial port...<br>";
      fwrite($fp,1);
      
      echo "Now outputting a 2 onto the serial port...<br>";
      fwrite($fp,2);
      
      echo "Now outputting a 3 onto the serial port...<br>";
      fwrite($fp,3);
      ++$count;
    }
    
    /*echo fgetc($fp);*/
    fclose($fp);
  ?>  
  
  
</body>

</html>
  

    
    
<!--
  

    <p> <b> Arduino Code </b> <br>
      <a href="../code/AnalogInput_3_level_LED_blinker.ino" target="_top">Arduino Code that Reads ADC Input and Sends Data over Serial Bus</a><br>
    </p>

    <!--<p> <b> Click this link to run the script (not working yet): </b> <br>
      <a href="../cgi-bin/pyscript.py">/cgi-bin/pyscript.py</a>
    </p>
    
    <p> <b> Print Output File of Calcuation Program </b> <br>
      <a href="../code/fortran_output.txt" target="_top">Report Energy Produced</a><br>
    </p>
    
    <hr />
    
    <h3>
    Links
    </h3>
    <p> <b> Links to Scientific/Mathematics Software </b> <br>
      <a href="http://www.scilab.org" target="_top">Link to SciLAB</a><br>
      <a href="http://www.gnuplot.info" target="_top">Link to GNUPlot</a><br>
      <a href="http://www.fftw.org" target="_top">Link to FFTW's Main Website</a><br>
      <a href="http://www.gnu.org/software/octave" target="_top">Link to GNU Octave</a><br>
      <a href="http://www.scilab.org/scilab/features/xcos" target="_top">Link to Xcos (FOSS version of popular control systems modelling software)</a><br>
      <a href="http://maxima.sourceforge.net/" target="_top">Link to Maxima (Computer Algebra System)</a><br>
    </p>
    
    <p> <b> Links to CAD/CAM Software </b> <br>
      <a href="http://librecad.org/cms/home.html" target="_top">Link to LibreCAD</a><br>
    </P>
    
    <p> <b> Links to Text Editors Suitable for Programming </b> <br>
      <a href="https://www.kde.org/applications/utilities/kate" target="_top">Link to KATE Advanced Text Editor</a><br>
    </p>
    
    <p> <b> Links to Programming and Development Environments </b> <br>
      <a href="http://netbeans.org" target="_top">Link to NetBeans IDE </a><br>
      <a href="http://eclipse.org" target="_top">Link to Eclipse Luna IDE</a><br>
      <a href="http://arduino.cc/en/main/software" target="_top">Link to Arduino IDE</a><br>
    </p>
    
    <p> <b> Miscellaneous Links </b> <br>
      <a href="http://arduino.cc/en/Main/ArduinoBoardTre" target="_top">One totally awesome Arduino board with built-in Linux Single Board Computer</a><br>
    </p>
  </div>
-->  
