// Get references to the form, input fields, and error messages
var form = document.getElementById("form");
var nameInput = document.getElementById("name");
var emailInput = document.getElementById("email");
var passwordInput = document.getElementById("password");
var nameError = document.getElementById("name-error");
var emailError = document.getElementById("email-error");
var passwordError = document.getElementById("password-error");

// Listen for the submit event on the form
form.addEventListener("submit", function(event) {
  // Prevent the form from submitting
  event.preventDefault();

  // Get the values of the input fields
  var name = nameInput.value;
  var email = emailInput.value;
  var password = passwordInput.value;

  // Validate the input fields
  var isValid = true;

  if (!name) {
    nameError.textContent = "Name is required";
    isValid = false;
  } else {
    nameError.textContent = "";
  }

  if (!email) {
    emailError.textContent = "Email is required";
    isValid = false;
  } else {
    emailError.textContent = "";
  }

  if (!password) {
    passwordError.textContent = "Password is required";
    isValid = false;
  } else {
    passwordError.textContent = "";
  }

  // If all input fields are valid, submit the form
  if (isValid) {
    form.submit();
  }
});
