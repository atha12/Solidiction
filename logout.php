<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "voting";
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
} 
//echo "Connected successfully<br>";
session_start();

session_unset()


	if (mysqli_query($conn,$query)) {
		header("Location: /voting/login.html");
	}
	else {
		echo mysqli_error($conn);
	}

mysqli_close($conn);
	



?>