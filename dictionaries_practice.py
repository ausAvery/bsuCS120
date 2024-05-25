def getStateCap():
    stateCap = {
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Wisconsin": "Madison",
        "Arkansas": "Little Rock",
        "New York": "Albany",
        "Alabama": "Montgomery"
        }
    return stateCap

def main():
    
    stateCap = getStateCap()
    
    print(stateCap)
    
    print()
    
    stateCap["Florida"] = "Tallahassee"
    
    """
        lookup stateCap
        for index/key/name in stateCap
            capital gets stateCap sub state
            print two new variables state and capital
    """
        
    for state in stateCap:
        capital = stateCap[state]
        print(f"The capital of {state} is {capital}.")

    print()

    """
        lookup stateCap
        for stateCap, turn stateCap into a tuple using .items
        assign tuple elements to state & cap repeating
            print table of state & cap
    """
    for state, cap in stateCap.items():
        print(f"{state:15} {cap:15}")
        
    print()
    
    """
        lookup stateCap
        if Alabama is in the keys of stateCap
            print "I know about Alabama."
            cap gets Value of Key "Alabama"
            print "The capital is {cap}"
    """
    
    if "Alabama" in stateCap.keys():
        print("I know about Alabama.")
        cap = stateCap["Alabama"]
        print(f"The capital is {cap}.")
    
    print()
    
    """
        lookup stateCap and get Values using .values()
        for Value in stateCap create a tuple called capital, sort the tuple
        print tuple
    """
    
    for capital in sorted(stateCap.values()):
        print(capital)
         
main()
    