weather_today = input("What's the weather like today? (sunny, rainy, cold) ").lower()
if weather_today == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_today == "rainy":
    print("Don't forget umbrella and a raincoat.")
elif weather_today == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have a recommendation for this weather")