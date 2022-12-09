let form = document.querySelector("form");

let temp, pressure, humidity, weather, weatherDesc;
let details = document.querySelector(".details");
let weatherd = document.querySelector(".weather");
let input = document.querySelector("input");
let cityName, completeUrl;

form.addEventListener("submit", function (e) {
    e.preventDefault();
    cityName = document.querySelector("input")?.value;
    console.log("istendi");
    console.log(cityName);
    if (!cityName) return;
    document.querySelector(".weather").classList.add("hidden");

    completeUrl = `http://127.0.0.1:5000//api/weather?city=${cityName}`;

    fetch(completeUrl)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            console.log(data);
            temp = data.temp;
            pressure = data["pressure"];
            humidity = data["humidity"];
            weather = data["weather"];

            weatherDesc = data["weatherDesc"];
            console.log(temp);
            console.log(document.querySelector(".weatherT"));

            weatherd.innerHTML = document
                .querySelector(".weatherT")
                .innerHTML.replace("{temp}", temp)
                .replace("{pressure}", pressure)
                .replace("{humidity}", humidity)
                .replace("{weatherDesc}", weatherDesc)
                .replace("{city name}", input.value);
            document.querySelector(".weather").classList.remove("hidden");

            input.value = "";
            console.log(details);
        });
});
