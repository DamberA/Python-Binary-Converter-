#
# Author: Damber Adhikari
#


menu = 0
#easy way to end if menu ==4 gam ends (also keeps looping unless user quits)
while(menu!=4): 
  print ("\n*** Menu ***\n"
  """\n1. Convert to binary
2. Convert to decimal
3. Binary counting
4. Quit\n""")

  #Menus to different different calculation
  menu = 1,2,3,4                                                           

  #Input to see what user chooses
  menu = int(input("What would you like to do [1,2,3,4]? "))               

  if menu == 1:

    decimal = input("\nPlease enter number: ")               
    notdecimal = 0

    #Finding out if user input is string or integer  
    for num in decimal:
      
      #Check string/text
      if not num.isdigit():   
        notdecimal = 1                          

    #If user input something else other than numbers
    if notdecimal == 1:           
      print("Please make sure your number contains digits 0-9 only.")
      decimal = int(input("\nPlease enter number: "))
    else:  
      decimal = int(decimal)
    
    binary = ''
    #calculate decimal to binary. 
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal //2

    #print the converted value
    print ("\nBinary number:",binary)                                      



  elif menu == 2:

    binary = input("\nPlease enter binary number: ")                      
    notbinary = 0
    #Asking user for input
    for num1 in binary:
      #If user input is not 0 or 1 ask till they get it
      if num1 != '0' and num1 != '1':                                     
        notbinary = 1
    
    if notbinary == 1:
        print("Please make sure your number contains digits 0-1 only.")
        binary = input("\nPlease enter binary number: ")
        
    number = 0
    power = 0
    while len(binary) > 0:
        #If user input len is higher than 0 this is readed.
        bits = int(binary[-1])
        number = number + bits * 2 ** power
        power = power + 1
        #Reversing the Binary Output
        binary = binary [:-1]                                               

    # printing the converted value
    print ("\nDecimal number:",number)                                       


    
  elif menu == 3:
    # User input (no int to check if user inputs strings)
    numberofTimes = input("\nPlease enter number: ")                       
    print ()
    notdecimal = 0
    
    for num2 in numberofTimes:
      #Finding out if user input is string or integer
      if not num2.isdigit(): 
        notdecimal = 1
    
    if notdecimal == 1:
      print("Please enter an integer between 0-9")
      #If user input something else other than numbers
      numberofTimes = int(input("\nPlease enter number: "))
    else:  
      numberofTimes = int(numberofTimes)

    #looping to create binary counting of user choice.
    for i in range(numberofTimes):                        
      binary = ''
      decimal = i+1
      while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal //2

      # printing the value (i+1 gives the number for list)
      print ("Decimal",i+1,"Binary number:", binary)                        


  if menu == 4:
        print ("Goodbye.")

  if menu != 1 and menu!=2 and menu!=3 and menu!=4:   
        print ("Invalid choice, please enter either 1, 2, 3 or 4.")

    
        

