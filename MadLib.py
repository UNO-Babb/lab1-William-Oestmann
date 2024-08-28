#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  sport = input("Enter a sport: ")
  name = input("Enter a name: ")
  adjective = input("Enter a adjective: ")
  place = input("Enter a place: ")
  number = input("Enter a number: ")
  animal = input("Enter an animal: ")
  #Print the story with the user supplied words.
  print("I love playing",sport, "with my best friend",name + ".","My best friend is very",adjective,"because they love going to the",place + ". During",sport,"I can jump",number,"feet high! A little off topic, but I wish",animal + "s did not exist!")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
