# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Mark McDuffie,12.7.19,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
#import files
if __name__ == "__main__":
    from DataClasses import Employee as E
    from ProcessingClasses import FileProcessor as FP
    from IOClasses import EmployeeIO as EIO
else:
    raise Exception("This file was not created to be imported")
# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
fileName = 'EmployeeData.txt'
lstTable = []
lstFile = FP.read_data_from_file(fileName)
for line in lstFile:
    lstTable.append(E(line[0],line[1],line[2].strip()))

while True:
    # Show user a menu of options
    EIO.print_menu_items()
    # Get user's menu option choice
    userChoice = EIO.input_menu_options()
    # Show user current data in the list of employee objects
    if userChoice == '1':
        EIO.print_current_list_items(lstTable)
    # Let user add data to the list of employee objects
    elif userChoice == '2':
        lstTable.append(EIO.input_employee_data())
    # let user save current data to file
    elif userChoice == '3':
        FP.save_data_to_file(fileName, lstTable)
    # Let user exit program
    elif userChoice == '4':
        break
    else:
        raise Exception("Only enter values from 1-4.")
# Main Body of Script  ---------------------------------------------------- #