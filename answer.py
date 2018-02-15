import csv
from PyQt4.QtGui import *

#This class provides methods for operating on an answer file
class Answer():
    
    #The parse function creates a list of dictionaries that contain
    #the search, replace strings from the file.
    def parse(self, ui):
        #Initialize a list of answers (each answer is a dict of search / 
        #replace pairs)
        self.answers = []
        #Open the file and begin reading as a csv
        try:
            with open(self.path) as ansFile:
                ansReader = csv.reader(ansFile, delimiter=',')
                #Read the header row, which contains the names of the variables.
                
                try:
                    self.header = next(ansReader)
                except StopIteration:
                    QMessageBox.warning(ui, "File Empty", "The selected file appears to be empty!")
                    self.headerPretty = []
                    return()
                #We want to be able to display the list in an alphabetically
                #ordered fashion, but don't want to upset the order of the variables
                #(which would scramble which search string corresponds to each replace
                #string); so we make a sorted (pretty) list for display only
                #without disturbing the variable list.
                self.headerPretty = sorted(list(set(self.header)))
                
                #Sentinel values to detect if any operations are found
                rowSentinel = None
                varSentinel = None
                #Loop through each row in the file
                for row in ansReader:
                    #Update the sentinel
                    rowSentinel = True
                    #Initialize a dict to hold the search / replace pairs
                    rowDict = {}
                    #For each field in the row
                    for i, ans in enumerate(row):
                        #Update the sentinel
                        varSentinel = True
                        #Add an entry with a key of the corresponding header (variable)
                        #value, and a value of the current answer
                        rowDict[self.header[i]] = ans
                    #If the sentinel is unchanged, warn the user that no variables were
                    #found in the file.
                    #When finished, add this row to the list of answers.
                    self.answers.append(rowDict)
                if (rowSentinel is None) or (varSentinel is None):
                    QMessageBox.warning(ui, "No Variables In File", "File has no variables or no rows!")
        except FileNotFoundError:
            QMessageBox.warning(ui, "File Not Found", "No file selected, or selected file was not found!")
            self.headerPretty = []
            return()