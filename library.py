def greet():
    print("Hello World!!")

def temperature_conversion():
    temperature_in_celsius = input('What is the temperature in celsius? ')

    temperature_in_fahrenheit = (float(temperature_in_celsius) * 1.8) + 32

    print(f'{temperature_in_celsius} degree celsius is equivalent to'
          f' {temperature_in_fahrenheit} degree fahrenheit.')