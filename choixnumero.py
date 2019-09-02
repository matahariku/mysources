def main():
  print("devine numero entre 1 et 100")
  numerorandom = 50 #par example
  
  devine = input("votre devine: ") #input command
  devine = int(devine) # input il faut en numero ou integer
  
  if devine == numerorandom:
    print("votre devine est vrai!!")
  else:
    print("votre devine est vaux !!")
 
 if __name__ == "__main__":
    main()
