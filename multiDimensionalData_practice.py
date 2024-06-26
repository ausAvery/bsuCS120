#CITIES = ("Indianapolis", "New York", "Tokyo", "London")

#distance = (
#    (0, 648, 6476, 4000),
#    (648, 0, 6760, 3470),
#    (6476, 6760, 0, 5956),
#    (4000,3470,5956,0)
#    )

distance = {
  "Indianapolis": {
    "Indianapolis": 0,
    "New York": 648,
    "Tokyo": 6467,
    "London": 4000 },
  "New York": {
    "Indianapolis": 648,
    "New York": 0,
    "Tokyo": 6760,
    "London": 3470 },
  "Tokyo": {
    "Indianapolis": 6476,
    "New York": 6760,
    "Tokyo": 0,
    "London": 5956 },
  "London": {
    "Indianapolis": 4000,
    "New York": 3470,
    "Tokyo": 5956,
    "London":0}
}


def getCity(title):
  """ returns a valid city name """
  keepGoing = True
  cityNames = distance.keys()
  while (keepGoing):
    print(title)
    print ("  (cities I know):")
    for theCity in cityNames:
      print (f"    {theCity}")

    city = input("City name: ")
    if city in cityNames:
      keepGoing = False
    else:
      print("That is not a correct input. Please try again")

  return city

def main():
    """ gets two cities, determines distance between them """

    fromCity = getCity("Traveling from...")
    toCity = getCity("Traveling to...")
    result = distance[fromCity][toCity]

    print (f"Distance from {fromCity} to {toCity} is {result} miles")

main()