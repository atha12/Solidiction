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
$username = $_SESSION['username'];
$query = "UPDATE users SET state=2 WHERE user_id='$username'";

	if (mysqli_query($conn,$query)) {
		header("Location: /voting/voting.html");
	}
	else {
		echo mysqli_error($conn);
	}

mysqli_close($conn);
	



?>