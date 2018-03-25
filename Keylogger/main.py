import keylog

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
  print("(X) Quit")
  print("-------------------------------")
  print()

def typesMenu():
  print("-------------------------------")
  print("(1) Social Security Number")
  print("(2) Credit Card Number")
  print("-------------------------------")

def main():
  print("Welcome to Wisper!")
  
  personalFields = [[] for i in range(2)]
  
  while True:
    optionsMenu()
    option = input("Enter option:")
    
    if option == '1':
      typesMenu()
      
      inputOption = input("Enter type:")
      field = input("Enter field:")
      
      if inputOption == '1' and len(field.replace('-', '').replace(' ', '')) == 9 and field.replace('-', '').replace(' ', '').isnumeric():
        personalFields[0] = personalFields[0] + [field.replace('-', '').replace(' ', '')]
      elif inputOption == '2' and len(field.replace(' ', '')) == 16 and field.replace(' ', '').isnumeric():
        personalFields[1] = personalFields[1] + [field.replace(' ', '')]
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
      try:
          keylog.start_wisper()
      except:
          filek.close()

      
    elif option == 'X' or option == 'x':
      print("Exiting program. Logs generated; check the logs/matches.txt folder. Thank you for using Wisper!")
      break
    else:
      print("Incorrect option chosen.")
    
    print()
	
  scannedInput = open("logs/info_log.txt", "r").read()
  lines = scannedInput.splitlines()
  
  bigString = ""
  for line in lines:
    bigString = bigString + line.split(',')[0]
  
  finalLog = open("logs/matches.txt", "w")
  
  for section in personalFields:
    for field in section:
      while field in bigString:
        if personalFields.index(section) == 0:
          finalLog.write("A provided SSN was input at " + lines[bigString.find(field)].split(',')[1] + ", at time " + lines[bigString.find(field)].split(',')[2] + '\n')
          bigString = bigString.replace(field, "", 1)
        if personalFields.index(section) == 1:
          finalLog.write("A provided credit card number was input at " + lines[bigString.find(field)].split(',')[1] + ", at time " + lines[bigString.find(field)].split(',')[2] + '\n')
          bigString = bigString.replace(field, "", 1)
   
		  
  remove = open("logs/info_log.txt", "r+")
  remove.truncate()
  
main()
