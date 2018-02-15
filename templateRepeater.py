from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4 import QtGui
from template import *
from answer import *
from replacer import *

( Ui_TemplateRepeater, QMainWindow ) = uic.loadUiType( 'templateRepeaterMainWindow.ui' )

class TemplateRepeater ( QMainWindow ):
    """TemplateRepeater inherits QMainWindow"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_TemplateRepeater()
        self.ui.setupUi( self )
        self.template = Template()
        self.answer = Answer()
        self.replacer = Replacer()
        #User defined connections, for browse buttons and parse / write buttons
        self.connect(self.ui.templateFilenameBrowse, SIGNAL('clicked()'), SLOT('browseTemplateFile()'))
        self.connect(self.ui.answerFilenameBrowse, SIGNAL('clicked()'), SLOT('browseAnswerFile()'))
        self.connect(self.ui.outputFilenameBrowse, SIGNAL('clicked()'), SLOT('browseOutputFile()'))
        self.connect(self.ui.templateParseButton, SIGNAL('clicked()'), SLOT('parseTemplateFile()'))
        self.connect(self.ui.answerParseButton, SIGNAL('clicked()'), SLOT('parseAnswerFile()'))
        self.connect(self.ui.outputPreviewButton, SIGNAL('clicked()'), SLOT('previewOutput()'))
        self.connect(self.ui.outputWriteButton, SIGNAL('clicked()'), SLOT('writeOutput()'))

    def __del__ ( self ):
        self.ui = None
    
    #Slot function that calls the filename dialog to get the template file name
    @pyqtSlot()
    def browseTemplateFile(self):
        self.ui.templateFilenameInput.setText(QtGui.QFileDialog.getOpenFileName())
    
    #Slot function that calls the filename dialog to get the answer file name
    @pyqtSlot()
    def browseAnswerFile(self):
        self.ui.answerFilenameInput.setText(QtGui.QFileDialog.getOpenFileName())
    
    #Slot function that calls the filename dialog to get the output file name
    @pyqtSlot()
    def browseOutputFile(self):
        self.ui.outputFilenameInput.setText(QtGui.QFileDialog.getSaveFileName())
    
    #Slot function that parses the template file and initializes variables in the
    #template class object
    @pyqtSlot()
    def parseTemplateFile(self):
        #Clear the variable list widget
        self.ui.templateVariableList.clear()
        #Get the path to the file
        self.template.path = self.ui.templateFilenameInput.text()
        #Get other details from UI controls
        self.template.delim = self.ui.templateVarDelimiterEntry.text()
        self.template.numHeaderRows = int(self.ui.templateNumHeaderRows.text())
        self.template.excludeHeader = self.ui.templateExcludeHeaderCB.isChecked()
        #Call the class parse function
        self.template.parse(self)
        #Output the found tags to the variable list widget
        for t in self.template.tagsUnique:
            self.ui.templateVariableList.addItem(t)
            
    #Slot function that parses the answer file and initializes variables in the
    #answer class object
    @pyqtSlot()
    def parseAnswerFile(self):
        #Clear the variable list widget
        self.ui.answerVariableList.clear()
        #Get the input file name
        self.answer.path = self.ui.answerFilenameInput.text()
        #Call the class parse method
        self.answer.parse(self)
        #Output the found tags to the variable list widget
        for t in self.answer.headerPretty:
            self.ui.answerVariableList.addItem(t)
            
    #Slot function that previews the output in the text window
    @pyqtSlot()
    def previewOutput(self):
        #Clear the output widget
        self.ui.outputPreviewEdit.clear()
        #Call the class parse function
        self.replacer.parse(self.template, self.answer, self)
        #Send the output to the preview window
        self.ui.outputPreviewEdit.setText(self.replacer.output)
        
    #Slot function that sends the output to the output file
    @pyqtSlot()
    def writeOutput(self):
        #Initialize the output file name variable
        self.replacer.outFileName = self.ui.outputFilenameInput.text()
        #Call the class output function
        self.replacer.write(self.template, self.answer, self)
        
        
        