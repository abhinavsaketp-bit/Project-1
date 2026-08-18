temprature= int(input("what is the temprature?"))
if temprature>30:
    outfit="t-shirt"
    print("it is a hot day and i will wear", outfit)
    print("The temprature for today is", temprature)
else:
    outfit="sweater"
    print("It is a cold day today and i will wear",outfit)
    print("The temprature is", temprature)
is_raining=input("Is it raining? yes if it is or no:")
if is_raining=="yes":
    print("take an umbrala with you")
windspeed=int(input("what is the windspeed?"))
if windspeed>40:
    print("It is a windy day")
else:
    print("it is a calm day")
