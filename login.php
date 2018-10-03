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
if (isset($_POST['user_name']) && isset($_POST['password'])) {
	if(!empty($_POST['user_name']) && !empty($_POST['password']))
	{
		$user_name = $_POST['user_name'];
		$password = ($_POST['password']);
		$query = "SELECT user_id FROM users WHERE user_id='$user_name' AND password='$password'";
		$result = mysqli_query($conn, $query);
		if (mysqli_num_rows($result) > 0) {
			$_SESSION['username']=$user_name;
			header("Location: /voting/verification.html");
		}
		else {
			echo "Invalid login";
		}
		// echo "<br> &nbsp <a href='/WD/templates/home.html'>Home</a>";
		mysqli_close($conn);
	}
}


?>