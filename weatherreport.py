def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }


def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather


def testRainy():
    weather = report(sensorStub)
    print(weather)
    assert("rain" in weather)


def testHighPrecipitation():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)

    weather = report(sensorStub)

    # strengthen the assert to expose the bug
    # (function returns Sunny day, it should predict rain)
    assert(len(weather) > 0);


def get_weather(sensor):
    temp = sensor.read_temperature()
    if temp > 40:
        return "Too hot"
    elif temp < 0:
        return "Too cold"
    else:
        return "All is well"


# Weak test (does not expose bug)
class DummySensor:
    def read_temperature(self):
        return 25


assert get_weather(DummySensor()) == "All is well"


# Strong test to expose bug
class EdgeSensor:
    def __init__(self, temp):
        self._temp = temp

    def read_temperature(self):
        return self._temp


def test_get_weather():
    assert get_weather(EdgeSensor(41)) == "Too hot"
    assert get_weather(EdgeSensor(-1)) == "Too cold"
    assert get_weather(EdgeSensor(0)) == "All is well"  # This will fail if the bug is at boundary


test_get_weather()
if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)")
