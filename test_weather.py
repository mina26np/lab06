from weather import celsius_to_fahrenheit, weather_message


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212


def test_weather_message_contains_city():
    message = weather_message("Krakow", 20)

    assert "Krakow" in message
    assert "20°C" in message
