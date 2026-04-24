def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def weather_message(city, temperature_celsius):
    temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)

    return (
        f"Weather for {city}: "
        f"{temperature_celsius}°C / {temperature_fahrenheit:.1f}°F"
    )


if __name__ == "__main__":
    print(weather_message("Krakow", 20))
