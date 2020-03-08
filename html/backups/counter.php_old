<?php
//                echo "[*] Now setting count_my_page to hitcounter.txt <br><br>";
                $count_my_page = ("hitcounter.txt");

//                echo "[\/]The value of count_my_page is $count_my_page <br><br>";

//                echo "[*] Now assigning hits to be the file with filename $count_my_page <br><br>";

                $hits = file($count_my_page);

//                echo "[*] The variable hits is an array. <br><br>";
//                echo "[\/] The first element of the hits array now contains $hits[0] <br><br>";

//                echo "[*] Now incrementing the first element of the hits array <br><br>";

                $hits[0] = $hits[0] + 1;

//                echo "[\/] The first element of the hits array was incremented.  It is now $hits[0] <br><br>";

//                echo "[*] Assinging a file pointer and opening $count_my_page. <br><br>";

                $fp = fopen($count_my_page , "w");

//                echo "[\/] The file pointer is $fp <br><br>";

//                echo "[*] Saving the value in the first element of the hits array into the file. <br><br>";

                fputs($fp , "$hits[0]");

//                echo "[*] Closing file... <br><br>";

                fclose($fp);

//                echo "[\/] The website hit counter is now ---> $hits[0] <br><br>";
                echo "<h2> Total page hits: $hits[0] </h2>";
?>

