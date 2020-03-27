<?php
    session_start();
	
	
	if(isset($_REQUEST["unoVsUnoConCarte"])){
		header("Location: carteUnoVsUno.php?username=" . $_REQUEST["username"]);
		exit;
    }
	if(isset($_REQUEST["unoVsComputerConCarte"])){
		header("Location: carteUnoVsComputer.php?username=" . $_REQUEST["username"]);
		exit;
    }
	if(isset($_REQUEST["unoVsUnoSenzaCarte"])){
		header("Location: senzaCarteUnoVsUno.php?username=" . $_REQUEST["username"]);
		exit;
    }
	if(isset($_REQUEST["unoVsComputerSenzaCarte"])){
		header("Location: senzaCarteUnoVsComputer.php?username=" . $_REQUEST["username"]);
		exit;
    }
	header("Location: resetta.php");
?>