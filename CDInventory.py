#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# MMezistrano, 2020-Mar-01, Completed TODOs, added and organized code, removed write_file function
# MMezistrano, 2020-Mar-01, Added docstrings, removed some comments to clean code
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor: # TODO/DONE add functions for processing here
    
    @staticmethod
    def delete_cd():
        """ Function to delete CD based on user input.
        
        Args: 
            None.
        
        Returns:
            None.
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        IO.show_inventory(lstTbl)

class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()
    
    @staticmethod
    def save_inventory(file_name):
        """ Function to save new inventory to text file.
        
        Args: 
            file_name (string): name of file where inventory will be saved.
        
        Returns: 
            None.
        """
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()

# -- PRESENTATION (Input/Output) -- #

class IO: # TODO/DONE add I/O functions as needed
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
            
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
    
    @staticmethod
    def add_cd():
        """Allows user to input new CD into the inventory; also appends CD to list.
        
        Args:
            None.
        
        Returns:
            None.
            
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        #Append to list  
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        IO.show_inventory(lstTbl)
        
# 1. When program starts, read in the currently saved Inventory
import os.path
from os import path
if path.exists(strFileName):
    FileProcessor.read_file(strFileName, lstTbl) # Without this, code didn't work the first time
else:
    pass

# 2. start main loop
while True:
    IO.print_menu() # Display Menu to user and get choice
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    if strChoice == 'x': # process exit first
        break
    
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    
    # 3.3 process add a CD
    elif strChoice == 'a': # Ask user for new ID, CD Title and Artist
        IO.add_cd() # TODO/DONE move IO code into function
        # Add item to the table
        # TODO/DONE move processing code into function: HAD TO LUMP THIS WITH IO OTHERWISE WAS IN WRONG ORDER.
        continue  
    
    # 3.4 process display current inventory
    elif strChoice == 'i': 
        IO.show_inventory(lstTbl)
        continue  
    
    # 3.5 process delete a CD
    elif strChoice == 'd': # TODO/DONE move processing code into function
        IO.show_inventory(lstTbl) # Display Inventory to user
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        DataProcessor.delete_cd() # Search thru table and delete CD
        continue  
    
    # 3.6 process save inventory to file
    elif strChoice == 's': # TODO/DONE move processing code into function
        IO.show_inventory(lstTbl) # Display current inventory; ask user for confirmation to save
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y': # Process choice
            FileProcessor.save_inventory(strFileName) # save data
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  
    
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')




