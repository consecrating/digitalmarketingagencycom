<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize inputs
    $name    = trim(filter_input(INPUT_POST, 'name',    FILTER_SANITIZE_STRING));
    $email   = trim(filter_input(INPUT_POST, 'email',   FILTER_SANITIZE_EMAIL));
    $phone   = trim(filter_input(INPUT_POST, 'phone',   FILTER_SANITIZE_STRING));
    $subject = trim(filter_input(INPUT_POST, 'subject', FILTER_SANITIZE_STRING));
    $message = trim(filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING));

    // Validate
    if (empty($name) || empty($email) || empty($phone) || empty($subject) || empty($message) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // On error, redirect back or show simple message
        echo "<script>alert('Please fill all fields correctly.'); window.history.back();</script>";
        exit;
    }

    // Email parameters
    $to         = "help@digitalmarketingagencygoa.com";
    $mailSubject = "Contact Form Submission: " . $subject;
    $body       = "Name: $name\nEmail: $email\nPhone: $phone\nSubject: $subject\n\nMessage:\n$message\n";
    $headers    = "From: no-reply@digitalmarketingagencygoa.com\r\n";
    $headers   .= "Reply-To: $email\r\n";
    $headers   .= "X-Mailer: PHP/" . phpversion();

    // Send email
    if (mail($to, $mailSubject, $body, $headers)) {
        // Success — output modal HTML + JS
        echo '
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <title>Thank You – Rankify Goa</title>
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <style>
            body { margin:0; padding:0; font-family:Arial, sans-serif; }
            .modal-overlay {
                position: fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); display:flex; align-items:center; justify-content:center; z-index:10000;
            }
            .modal-content {
                background: #25D366; color: #fff; padding: 40px; text-align:center; border-radius:8px; max-width:500px; width:90%;
            }
            .modal-content h1 {
                margin-top:0; font-size:28px;
            }
            .modal-content p {
                font-size:16px; line-height:1.5;
            }
            .modal-content button {
                margin-top:20px; padding:12px 24px; background:#fff; color:#25D366; border:none; border-radius:4px; font-size:16px; cursor:pointer;
            }
          </style>
        </head>
        <body>
          <div class="modal-overlay">
            <div class="modal-content">
              <h1>Thank You!</h1>
              <p>Your message has been sent successfully. We will review it and get back to you shortly.</p>
              <button id="closeBtn">Close</button>
            </div>
          </div>
          <script>
            document.getElementById("closeBtn").addEventListener("click", function(){
              window.location.href = "index.html";
            });
          </script>
        </body>
        </html>';
        exit;
    } else {
        // Mail sending failed
        echo "<script>alert('Sorry, an error occurred. Please try again later.'); window.history.back();</script>";
        exit;
    }

} else {
    // Not POST method
    header("Location: contact.html");
    exit;
}
?>
