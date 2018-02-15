import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from templateRepeater import TemplateRepeater

if __name__ == '__main__':

    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'templateRepeater' )

    # create widget
    w = TemplateRepeater()
    w.setWindowTitle( 'templateRepeater' )
    w.show()

    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )
    

    # execute application
    sys.exit( app.exec_() )
