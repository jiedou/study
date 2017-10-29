class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature
 
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
 
    def get_temperature(self):
        print("Getting value")
        return self._temperature
 
    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value:",value)
        self._temperature = value
 
    temperature = property(get_temperature,set_temperature)
	
a=Celsius(1)
print(a.get_temperature())
print(a.temperature)
a.temperature=1
print(a.temperature)