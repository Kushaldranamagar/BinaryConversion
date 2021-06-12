from binaryInput import *
from decimalInput import *

print("{}{}{}{}{}{}}{}}{}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}")
print("{}                                                                                             {}")
print("{}   ||||||  ||     || |||||||  ||    ||      ||||      ||     ||                              {}")
print("{}   ||  ||    ||  ||    ||     ||    ||    ||    ||    ||||   ||                              {}")
print("{}   ||||||      ||      ||     ||||||||   ||      ||   ||  || ||                              {}")
print("{}   ||          ||      ||     ||    ||    ||    ||    ||   ||||                              {}")
print("{}   ||          //      ||     ||    ||      ||||      ||     ||                              {}")
print("{}                                                                                             {}")
print("{}                                                                                             {}")
print("{}                                                                                             {}")
print("{}             |||||||        |||||\\   ||||||||||    |||||||||                                 {}")
print("{}            ||     ||       ||    ||      ||           ||                                    {}")
print("{}            ||     ||       ||    ||      ||           ||                                    {}")
print("{}              || ||         |||||//       ||           ||                                    {}")
print("{}             ||    ||       ||   \\        ||           ||                                    {}")
print("{}            ||      ||      ||    ||      ||           ||                                    {}")
print("{}             ||    ||       ||    ||      ||           ||                                    {}")
print("{}              ||||||        |||||//   |||||||||||  ||||||||||||                              {}")
print("{}                                                                                             {}")
print("{}                                                                                             {}")
print("{}                                                                                             {}")
print("{}              ||     ||||||     ||||||     |||||||   ||||||                                   {}")
print("{}            ||  ||   ||    \\     ||    \\   ||        ||    \\                               {}")
print("{}           ||    ||  ||     ||  ||     ||  |||||||   ||    //                                 {}")
print("{}           ||||||||  ||     ||  ||     ||  ||        ||||//                                  {}")
print("{}           ||    ||  ||    //   ||    //   ||        ||   \\                                  {}")
print("{}           ||    ||  ||||||     ||||||     |||||||   ||    ||                                {}")
print("{}                                                                                             {}")
print("{}                                                                                             {}")
print("{}{}{}{}{}{}}{}}{}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}")




def launch():
    inputc = False
    while(not inputc):
        ready = input("Enter s to start or e to Exit the program:")
        if(ready == "s"):
          inputc = True
        elif(ready == "e"):
            print("Program will end  now...")
            inputc = True
            exit()
        elif(ready ==""):
            print("\nEmpty field found!!please enter either s or e .\n")
            launch()
        else:
            print("\nOnly s or e is valid, Please choose either s or e and try again\n")

print("\n Things to know before using this program: \n")
print("This program uses 8 bit adder for conversion. ")
print("This program takes the input value of 0 or 1 for binary operation ")
print("This program takes the input value of 0,1,2,3,4,5,6,7 for decimal operation")
print("The lower limit is Zero and upper limit is 255 for both operation")


def insert():
    launch()
    inputc = False
    while(not inputc):
        userInsert = input("Which operation do you want to run:\n 1.Binary (B/b) or \n 2.Decimal (D/d)")
        if(userInsert ==""):
            print("Invalid Input")
            print("Empty textfield is found")
            print("Choose either B,b or D,d")
        elif(userInsert =="B" or userInsert =="b"):
            print("Welcome to Binary Operation")
            bfinal_output() #calls from binaryinput for binary conversion
            insert()

        elif(userInsert == "D" or userInsert == "d"):
            dfinal_output() #calls from decimalInput for decimal conversion
            insert()

        else:
            print("Error Input value")
            print("1.invalid character")
            print("2.", userInsert.upper(), "is an invalid character")
            print("3. Choose either B,b or D,d")

def main():
    insert()

main()




