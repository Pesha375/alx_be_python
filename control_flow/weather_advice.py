weather_condittion = ("sunny", "cold", "rainy")

weather_condittion = input("What is the weather like today? (sunny, rainy, cold): ")

if weather_condittion == "sunny":
    print("Wear a t-shirt and sunglasses")
elif weather_condittion == "rainy":
    print("Don't forget your umbrella and a rain coat")
elif weather_condittion == "cold":
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Sorry, I don't have a recommendation for this weather")