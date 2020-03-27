<html>
	<head>
		<title></title>
	</head>
	<body>
		<?php
		    session_start();
		?>
		<form action="dispatcher.php" method="get" >
		<p align="center"><br>
		USERNAME: <br>
		<input type="text" name="username" maxlength="20">
		</p><br>
		<p align="center">
			<p align="center">Scegli la modalita di gioco</p><br>
			<p align="center">Con carte</p><br>
			<p align = "center">
			<input type="submit" name="unoVsUnoConCarte" value="1 VS 1"  style="width:200px;" style="height:200px;" />&nbsp;
			<input type="submit" name="unoVsComputerConCarte" value="1 VS COMPUTER"  style="width:200px;" style="height:200px;"/>&nbsp;
			</p>
			<p align="center">Senza carte</p><br>
			<p align = "center">
			<input type="submit" name="unoVsUnoSenzaCarte" value="1 VS 1"  style="width:200px;" style="height:200px;"/>&nbsp;
			<input type="submit" name="unoVsComputerSenzaCarte" value="1 VS COMPUTER"  style="width:200px;" style="height:200px;"/>&nbsp;
			</p>
		</form>
		</p>
		<hr/>
		
	</body>
</html>