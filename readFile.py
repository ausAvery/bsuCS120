"""
readFile.py
read the contents of a file
"""
def main():
    file = open("groceries.txt", "r")
#    print("We need,")
    
    for line in file:
        line = line.strip()
        print(f"We need {line}, dude.")
#        print(line + ",")
#    print("and that's it.")
    file.close()

main()