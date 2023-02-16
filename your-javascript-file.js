// Get the buttons and the div element
var hideButton = document.getElementById("hide-button");
var showButton = document.getElementById("show-button");
var aboutYourself = document.getElementById("about-yourself");

// Hide the information when the hide button is clicked
hideButton.addEventListener("click", function() {
  aboutYourself.style.display = "none";
});

// Show the information when the show button is clicked
showButton.addEventListener("click", function() {
  aboutYourself.style.display = "block";
});
