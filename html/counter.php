<?php

	// logging page hits
	$dbfolder = $_SERVER["DOCUMENT_ROOT"]."/hitcounter_db/";
	$dbname = $_SERVER["HTTP_HOST"]."_log.sq3";

	$client_ip = $_SERVER["REMOTE_ADDR"];
	$http_user_agent = $_SERVER["HTTP_USER_AGENT"];
	//echo "Client IP: $client_ip <br>";
	//echo "Client HTTP User Configuration: $http_user_agent <br><br>";

	$user_hash = hash_hmac('sha256', "$client_ip", "$http_user_agent");
	//echo "The sha256 hash of client_ip with http_user_agent is : $user_hash <br>";

	// check if database file exists first
	if(!file_exists($dbfolder.$dbname))
	{
 		//echo ("DB file does not exist, creating new table... <br");
 		$logdb = new PDO("sqlite:".$dbfolder.$dbname);
 		$logdb->exec("CREATE TABLE hits (hash_client_ip VARCHAR(255))");
	}
	else {
 		//echo ("DB file exists, using ".$dbfolder.$dbname."<br>");
 		$logdb = new PDO("sqlite:".$dbfolder.$dbname);
	}

	//echo "Database name: $dbname <br><br>";

	// check if client_ip is already in the hits table
	$query_statement = $logdb->query("SELECT * FROM hits WHERE hash_client_ip='$user_hash'");
	$returned_record = $query_statement->fetchAll();

	//echo "The size of returned_record is ".sizeof($returned_record)."<br>";
	//echo "The contents of returned_record is: <br>";
	//var_dump($returned_record);
	//echo "<br><br><br>";

	// Open files for reading and writing
	$total_count_my_page = ("total_hit_counter.txt");
    $total_hits = file($total_count_my_page);
	$total_fp = fopen($total_count_my_page, "w");

	$unique_count_my_page = ("unique_hit_counter.txt");
	$unique_hits = file($unique_count_my_page);
	$unique_fp = fopen($unique_count_my_page, "w");

	// if a client_ip record is found
	if(sizeof($returned_record) != 0)
	{
		//echo "$user_hash is already in database... <br>";
		//echo "Updating total hit counts only... ";

		// Increment total hit counter
    	$total_hits[0] = $total_hits[0] + 1;

		// Write data to files
		// Need to also write to unique_fp since it was also opened as write
		fputs($total_fp, "$total_hits[0]");
		fputs($unique_fp, "$unique_hits[0]");
	}

	// Else client_ip is not in database
	else {
		//echo  ("$user_hash is a new client... <br>");
		$logdb->exec("INSERT INTO hits (hash_client_ip) VALUES ('$user_hash')");

		// Increment both total and unique hit counters
		//echo "Before increment... <br>";
		//echo $total_hits[0]."<br>";
		//echo $unique_hits[0]."<br>";
		$total_hits[0] = $total_hits[0] + 1;
		$unique_hits[0] = $unique_hits[0] + 1;
		//echo "After increment... <br>";
		//echo $total_hits[0]."<br>";
        //echo $unique_hits[0]."<br>";

		// Write data to files
		fputs($total_fp, "$total_hits[0]");
		fputs($unique_fp, "$unique_hits[0]");
	}

	// Display results on website
	echo "<h2> Total page hits: $total_hits[0] </h2>";
	echo "<h2> Unique page hits: $unique_hits[0] as of 11/24/2018 </h2>";

	// Close files
	fclose($total_fp);
	fclose($unique_fp);

	// Close databse connection
	$logdb = null;
?>
