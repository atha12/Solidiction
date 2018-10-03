<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "voting";
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
} 

session_start();
$username = $_SESSION['username'];

$query = "SELECT state FROM users WHERE user_id = '$username'";

$result = mysqli_query($conn,$query);
$state = 0;

while($row=mysqli_fetch_assoc($result)){
	$state = $row["state"];
	break;
}

if($state == 2){
	header("Location: /voting/charts.html");
}
elseif($state = 1){
	header("Location: /voting/votingballot.html");
}
else{
		$query = "UPDATE users SET state=1 WHERE user_id='$username'";

	if (mysqli_query($conn,$query)) {
		header("Location: /voting/votingballot.html");
	}
	else {
		echo mysqli_error($conn);
	}
}



mysqli_close($conn);



?>