
    // function redirectToMainPage() {
    //     // Get the URL from the hidden input field and use it to redirect.
    //     const servicesUrl = document.getElementById('services-url').value;
    //     window.location.href = servicesUrl;
    // }
       function validateCredentials() {
            var username = document.getElementById("username").value;
            var password = document.getElementById("password").value;

            // Check if username and password are not empty
            if (username.trim() === "" || password.trim() === "") {
                alert("Field is required!");
                return;
            }

            // // You can add additional checks for the password here
            // if (password !== "password") {
            //     alert("Incorrect password. Please try again.");
            //     return;
            // }

            // If everything is fine, submit the form
            document.getElementById("loginForm").submit();
        }


