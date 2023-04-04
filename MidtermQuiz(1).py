giventemperature = int(input("Temperature: "))
class TemperatureConversion:
    def __init__(self,temp):
        self.__temp = giventemperature

    def Celcius(self):
        print("Celcius: ", (giventemperature-32)*5/9)
        print("Celcius: ", giventemperature-273.15)

    def Farenheit(self):
        print("Farenheit: ", (giventemperature*9/5)+32)
        print("Farenheit: ", (1.8*giventemperature)-459.67)

    def Kelvin(self):
        print("Kelvin: ", giventemperature+273.15)
        print("Kelvin: ", (giventemperature+459.67)/1.8)

celci = TemperatureConversion(giventemperature)
celci.Celcius()
far = TemperatureConversion(giventemperature)
far.Farenheit()
kel = TemperatureConversion(giventemperature)
kel.Kelvin()