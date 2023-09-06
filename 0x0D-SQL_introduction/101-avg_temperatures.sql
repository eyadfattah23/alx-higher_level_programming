-- script that displays the average temperature (Fahrenheit) by city ordered by temperature
SELECT city , AVG(value) AS avg_temp
FROM temperatures
GROUP BY temperatures
ORDER BY temperatures DESC;
