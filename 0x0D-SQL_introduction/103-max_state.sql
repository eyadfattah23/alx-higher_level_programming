-- script that displays the max temperature (Fahrenheit) by city ordered by temperature 

SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
