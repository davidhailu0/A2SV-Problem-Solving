class Solution:
    def convertTemperature(self, celsius: float) -> List[float]: 
        temperature_in_kelvin = celsius + 273.15

        temperature_in_fahrenheit = celsius * 1.80 + 32.00

        return [round(temperature_in_kelvin,5), round(temperature_in_fahrenheit,5)] 