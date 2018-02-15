import re
from PyQt4.QtGui import *

#This class takes care of the search/replace functions required for the system.
class Replacer():
    
    #Parse takes care of doing the actual replace. The output text is stored
    #in a class variable.
    def parse(self, template, answer, ui):
        try:
            #Regex to find the first number of rows specified by the user as a header
            matchText = r"([^\n]*\n){" + str(template.numHeaderRows) + "}"
            match = re.match(matchText, template.templateText)
            #The header is the part before the end of the match...
            self.header = template.templateText[0:match.end()]
            #and the replaceable text is the part after the header.
            self.replaceableText = template.templateText[match.end():]
            
            
            #Initialize the output, in case the header is excluded by the user
            self.output = ""
            #If the user has not excluded the header from the output, write it to the
            #output variable
            if not template.excludeHeader:
                self.output = self.header
            
            
            #For each line in the answer file:
            for a in answer.answers:
                #Grab the contents of the template (sans header)
                workText = self.replaceableText
                #For each variable, run the search/replace
                for subFrom, subTo in a.items():
                    workText = workText.replace(template.delim + subFrom + template.delim, subTo)
                #Append the replaced text to the output
                self.output = self.output + workText
        except AttributeError:
            QMessageBox.warning(ui, "No Template", "The template is not valid. Please select a template file and click Parse Template.")
            self.output = ""
        
    #Preview function to do the parse without writing the file
    def preview(self, template, answer, ui):
        parse(self, template, answer, ui)
    
    #Write function does the parse, then outputs the file
    def write(self, template, answer, ui):
        self.parse(template, answer, ui)
        with open(self.outFileName, "w") as outFile:
            outFile.write(self.output)
        QMessageBox.information(ui, "Finished", "The output was written successfully.")