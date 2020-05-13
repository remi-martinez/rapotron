<?php 

	if(!isset($_GET["rapper1"]) || !isset($_GET["rapper2"]))
		die('Error');

	$r1 = $_GET["rapper1"];
	$r2 = $_GET["rapper2"];

	exec("python3 rapotron.py {$r1} {$r2}", $r);
	// echo "<div id='punchline'><blockquote>\"$r[1]\"</blockquote></div>";
	// echo "<div id='auteurs'> - {$r[0]}</div>"; 

	$array = array();
	$array["authors"] = $r[0];
	$array["punchline"] = $r[1];

	die(json_encode($array));
?>