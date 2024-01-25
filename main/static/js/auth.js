
    $(document).ready(function () {
        $("#submitBtn").click(function (event) {
            event.preventDefault(); // Prevent default form submission

            var username = $("#username").val();
            var password = $("#password").val();

            var formData = new FormData();
            formData.append('username', username);
            formData.append('password', password);

            $.ajax({
                url: "https://bitbo-standard-dep-dd2462e5a0a8.herokuapp.com/login/sign-in",
                type: "POST",
                data: formData,
                processData: false,
                contentType: false,
                success: function (response) {
                    // Store the token securely in localStorage
                    localStorage.setItem('token', response.access_token);

                    // Redirect to the home page
                    window.location.href = "/services/";
                },
                error: function (error) {
                    console.error("Error during login:", error.responseJSON.detail);
                    // Display the error message
                    $("#errorMessage").removeClass('d-none');
                }
            });
        });
    });
