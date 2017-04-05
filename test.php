<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="fredo.css">
</head>

<body>
<?php
echo "Guardium UpLoads"
?>

<br><br><br>
<a href="http://192.168.1.161/phpmyadmin/" target=_blank>MySQL Admin</a>
<br><br><br>
    Select Files to upload:
<br><br>
<form action="upload.php" method="post" enctype="multipart/form-data">
    Aggregation Archive Log
    <input type="file" name="fileToUpload" id="fileToUpload">
    <input type="submit" value="Upload" name="submit">
</form>
<br><br>
<form action="upload.php" method="post" enctype="multipart/form-data">
    Audit Process Log
    <input type="file" name="fileToUpload" id="fileToUpload">
    <input type="submit" value="Upload" name="submit">
</form>
<br><br>
<form action="upload.php" method="post" enctype="multipart/form-data">
    Little BUM
    <input type="file" name="fileToUpload" id="fileToUpload">
    <input type="submit" value="Upload" name="submit">
</form>
<br><br>
<form action="upload.php" method="post" enctype="multipart/form-data">
    Enterprise S-TAP View
    <input type="file" name="fileToUpload" id="fileToUpload">
    <input type="submit" value="Upload" name="submit">
</form>

<form action="./Uploads/DailySize_2.py" method="post" enctype="multipart/form-data">
    Processing AAL for Sizes
    <input type="submit" value="Submit" name="submit">
</from>
</body>
</html>

