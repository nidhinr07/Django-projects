
/* =====================================
   SHOW / HIDE PASSWORD
===================================== */

document.querySelectorAll(".toggle-password").forEach(button => {

    button.addEventListener("click", function () {

        const targetId = this.dataset.target;
        const passwordInput = document.getElementById(targetId);
        const icon = this.querySelector("i");

        if (passwordInput.type === "password") {

            passwordInput.type = "text";
            icon.classList.replace("bi-eye", "bi-eye-slash");
            this.setAttribute("aria-label", "Hide password");

        } else {

            passwordInput.type = "password";
            icon.classList.replace("bi-eye-slash", "bi-eye");
            this.setAttribute("aria-label", "Show password");

        }

    });

});


/* =====================================
   PASSWORD MATCH VALIDATION
===================================== */

document.getElementById("registerForm").addEventListener("submit", function (event) {

    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    if (password !== confirmPassword) {

        event.preventDefault();

        alert("Passwords do not match. Please try again.");

        document.getElementById("confirmPassword").focus();

    }

});
