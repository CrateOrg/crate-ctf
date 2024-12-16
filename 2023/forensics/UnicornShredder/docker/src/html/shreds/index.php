<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shred bucket</title>
</head>
<body>

<ul>
<?php

$dir = "."; // Current directory
$images = glob($dir . "/*.{jpg,jpeg,gif,png}", GLOB_BRACE); // Search for image files

// Sort images based on write timestamp
usort($images, function($a, $b) {
    return filemtime($b) - filemtime($a);
});

foreach($images as $image) {
    echo "<a href='{$image}'>{$image}</a><br>";
}

?>
</ul>

</body>
</html>
