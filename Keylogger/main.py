def printFields(fieldList):
  for field in fieldList:
    print("(" + str(fieldList.index(field)) + ") " + field)

def optionsMenu():
  print("-------------------------------")
  print("Wisper Options:")
  print("(1) Add personal information field")
  print("(2) Remove an information field")
  print("(3) Retrieve all stored information field")
  print("(4) Run Wisper")
  print("(5) Print all matches")
  print("(X) Quit")
  print("-------------------------------")
  print()

def typesMenu():
  print("-------------------------------")
  print("(1) Social Security Number")
  print("(2) E-Mail")
  print("-------------------------------")

def main():
  print("Welcome to Wisper!")
  
  personalFields = [[] for i in range(2)]
  file = open("database.txt", 'w+')
  
  while True:
    optionsMenu()
    option = input("Enter option:")
    
    if option == '1':
      typesMenu()
      
      inputOption = input("Enter type:")
      field = input("Enter field:")
      
      if inputOption == '1' and len(field.replace('-', '').replace(' ', '')) == 9 and field.replace('-', '').replace(' ', '').isnumeric():
        personalFields[0] = personalFields[0] + [field.replace('-', '').replace(' ', '')]
      elif inputOption == '2' and '@' in field:
        personalFields[1] = personalFields[1] + [field]
      else:
        print("Invalid input (either type or field).")
        
    elif option == '2':
      typesMenu()
      
      inputOption = input("Enter type:")
      if inputOption == '1':
        printFields(personalFields[0])
      elif inputOption == '2':
        printFields(personalFields[1])
        
      indexRemove = input("Enter index of field to remove:")
      
      try:
        del personalFields[int(inputOption)-1][int(indexRemove)]
      except:
        print("Outside of range, or incorrect input.")
      
    elif option == '3':
      for section in personalFields:
        printFields(section)
        
    elif option == '4':
      print("Wisper started. Press ESC to disable Wisper.")
      
    elif option == '5':
      print("Printing all matches of personal data...")
      
    elif option == 'X' or option == 'x':
      print("Exiting program. Thank you for using Wisper!")
      break
    else:
      print("Incorrect option chosen.")
    
    print()
  
  for section in range(0, len(personalFields)):
    for field in range(0, len(personalFields[section])):
      file.write(personalFields[section][field])
      if field < len(personalFields[section]) - 1:
        file.write(" ")
    if section < len(personalFields) - 1:
      file.write('\n')
    
  file.close()
  
main()
