<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);

    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $file = fopen("subscribers.txt", "a");
        fwrite($file, $email . "\n");
        fclose($file);
        echo "<script>alert('Thank you for subscribing!'); window.location.href='index.html';</script>";
    } else {
        echo "<script>alert('Please enter a valid email address.'); window.history.back();</script>";
    }
} else {
    header("Location: index.html");
    exit();
}
?>
