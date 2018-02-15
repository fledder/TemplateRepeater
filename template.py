import re
from PyQt4.QtGui import *

#Class that represents a template file and parses variable strings from it
class Template():
    
    #Parse function to open the file, read the contents, and determine the
    #variables it contains
    def parse(self, ui):
        #Get the contents of the file
        try:
            with open(self.path) as templateFile:
                self.templateText = templateFile.read()
        except FileNotFoundError:
            QMessageBox.warning(ui, "File Not Found", "No file selected, or selected file was not found!")
            self.tagsUnique = []
            return()
        #Initialize a list of tags
        tags = []
        #Build a regex to find anything bounded by a delimiter. Use capturing 
        #groups to strip the delimiters.
        searchString = "(" + self.delim + ")([^`]*)(" + self.delim + ")"
        #Loop through the found items
        for m in re.finditer(searchString, self.templateText):
            #Add only captured group 2 (the variable name without delimiters)
            #to the list of tags.
            tags.append(m.group(2))
        #By converting to a set, duplicates are removed; it is then converted
        #back to a list to be able to sort it alphabetically.
        self.tagsUnique = sorted(list(set(tags)))