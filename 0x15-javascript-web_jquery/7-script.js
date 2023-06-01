document.addEventListener("DOMContentLoaded", function () {
    fetch("https://swapi-api.alx-tools.com/api/people/5/?format=json")
	.then((response) => response.json())
	.then((data) => {
	    $("#character").text(data.name);
	});
});
