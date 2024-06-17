document.addEventListener('DOMContentLoaded', function() {
    const weatherInfo = document.getElementById('weather-info');

    fetch('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m')
        .then(response => response.json())
        .then(data => {
            const temperatures = data.hourly.temperature_2m;
            const currentTemperature = temperatures[0];
            weatherInfo.textContent = `La temperatura actual es ${currentTemperature}°C`;
        })
        .catch(error => {
            weatherInfo.textContent = 'No se pudo obtener la temperatura.';
            console.error('Error al obtener los datos del clima:', error);
        });
});
