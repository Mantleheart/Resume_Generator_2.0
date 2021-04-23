
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#Import statements
import sys
import Printer
import util
from PySide6.QtWidgets import QApplication, QWidget, QScrollArea,QLabel, QPushButton, QGridLayout, QGroupBox, QDialog, QHBoxLayout, QVBoxLayout, QProgressDialog, QFileDialog, QTextEdit, QComboBox
from PySide6.QtGui import QIcon
from PySide6 import QtCore
from datetime import date

#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

#Main class for application
#Extends the QWidget class



class App(QWidget):
    def __init__(self):
        
        #init
        super(App, self).__init__()
        
        #▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        #parameters for the resume generation.
        self.params = {
        "White": 1.0,
        "Black": 1.0,
        "Hispanic": 1.0,
        "Asian": 1.0,
        "GenderRatio": 0.5,
        "TestSection": '',
        "TestMode": 2,
        "WorkPath": "",
        "BeginYear":"",
        "EndYear":"",
        "BeginMonth":"",
        "EndMonth":"",
        "BeginYearEdu":"",
        "EndYearEdu":"",
        "BeginMonthEdu":"",
        "EndMonthEdu":""
        }
        #▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       
        #Dictionaries for UI buttons
        
        self.testModes = {
        "Before": 1,
        "After": 2,
        "Replace":3
        }
        
        self.testSections = {
        "Address": 1,
        "Education": 2,
        "Work History": 3,
        "Skills": 4
        }
        #▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        #Window sizing for application
        self.title = "COEHP Resume Generator"
        self.left = 10
        self.top = 10
        self.width = 100
        self.height = 300
        
        #▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        #Window is created here
        self.makeUI()
        
        
    #▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    #Function creates window and adds widgets
    
    def makeUI(self):
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.createLayout()
        
        windowLayout = QGridLayout()

        windowLayout.addWidget(self.box0,1,1,1,1)
        windowLayout.addWidget(self.box4,0,0,1,1)
        windowLayout.addWidget(self.box6,1,0,1,1)
        windowLayout.addWidget(self.box7,0,1,1,1)
        windowLayout.addWidget(self.box5,3,0,1,2)
        windowLayout.addWidget(self.box8,2,0,1,2)
        
        windowLayout.setAlignment(QtCore.Qt.AlignTop)
        
        self.setLayout(windowLayout)
        self.show()

    #▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    #All QGroupBoxes for features are added here.
    def createLayout(self):
        self.box0 = QGroupBox("Timeframe")
        self.box4 = QGroupBox("Test Data")
        self.box6 = QGroupBox("Output Directory")
        self.box5 = QGroupBox("")
        self.box7 = QGroupBox("Demographic Settings")
        self.box8 = QGroupBox("Resume Layout")

        #Demographic Settings

        self.wPercent = QTextEdit("0.25")
        self.bPercent = QTextEdit("0.25")
        self.aPercent = QTextEdit("0.25")
        self.hPercent = QTextEdit("0.25")
        self.gPercent = QTextEdit("0.5")
        self.wLabel = QLabel("White %");
        self.bLabel = QLabel("Black %");
        self.aLabel = QLabel("Asian %");
        self.hLabel = QLabel("Hispanic %");
        self.gLabel = QLabel("       Gender Ratio");

        self.wPercent.setFixedSize(100,30)
        self.bPercent.setFixedSize(100,30)
        self.aPercent.setFixedSize(100,30)
        self.hPercent.setFixedSize(100,30)
        self.gPercent.setFixedSize(100,30)
 

        #Resume Layout Settings

        self.testSectionLabel1 = QLabel("Test Location")
        self.testSectionLabel2 = QLabel("Section")
        self.testSectionLabel3 = QLabel("Location of Content")
        self.sectionSelect = QComboBox()
        self.sectionSelect.addItems(["Address","Education","Work History","Skills"])
        self.sectionSelect.setFixedSize(300,30)

        self.modeSelect = QComboBox()
        self.modeSelect.addItems(["Before","After","Replace"])
        self.modeSelect.setFixedSize(300,30)
        

        #Academic Year

        #First Semester
        self.monthBegin = QComboBox()
        self.monthBegin.addItems(["January","February","March","April","May","June","July","August","September","November","December"])
        self.monthBegin.setFixedSize(100,30)
        
        self.yearBeginLabel = QLabel("First Semester")
        self.yearBegin = QComboBox()
        self.yearBegin.setFixedSize(100,30)
        
        for year in range(1970, 2050):
            self.yearBegin.addItem(str(year))
        
        #Last Semester
        self.monthEnd = QComboBox()
        self.monthEnd.addItems(["January","February","March","April","May","June","July","August","September","November","December"])
        self.monthEnd.setFixedSize(100,30)
            
        self.yearEnd= QComboBox()
        self.yearEndLabel = QLabel("Semester of Graduation")
        for year in range(1970, 2050):
            self.yearEnd.addItem(str(year))
        self.yearEnd.setFixedSize(100,30)

        #Earliest relevant employment
        self.monthWorkBegin = QComboBox()
        self.monthWorkBegin.addItems(["January","February","March","April","May","June","July","August","September","November","December"])
        self.monthBegin.setFixedSize(100,30)
        
        self.yearWorkBeginLabel = QLabel("Earliest Possible Date of Employment")
        self.yearWorkBegin = QComboBox()
        self.yearWorkBegin.setFixedSize(100,30)
        
        for year in range(1970, 2050):
            self.yearWorkBegin.addItem(str(year))
        
        #Latest relevant employment
        self.monthWorkEnd = QComboBox()
        self.monthWorkEnd.addItems(["January","February","March","April","May","June","July","August","September","November","December"])
        self.monthWorkEnd.setFixedSize(100,30)
            
        self.yearWorkEnd= QComboBox()
        self.yearWorkEndLabel = QLabel("Latest Possible Date of Employment")
        for year in range(1970, 2050):
            self.yearWorkEnd.addItem(str(year))
        self.yearWorkEnd.setFixedSize(100,30)

        currentYear = date.today().year
        index = currentYear - 1970
        self.yearEnd.setCurrentIndex(index)
        self.yearBegin.setCurrentIndex(index)
        self.yearWorkBegin.setCurrentIndex(index)
        self.yearWorkEnd.setCurrentIndex(index)




        #Output Directory
        self.dirLabel = QLabel("Output Directory")
        self.currentDir = QTextEdit()
        self.currentDir.setText("Not Selected")
        self.currentDir.layout()
        self.currentDir.setFixedSize(300,30)
        self.currentDir.setReadOnly(True)
        self.outputName = QTextEdit()
        
        self.outputLabel = QLabel("Output Folder Name")
        self.outputName.setText("None written")
        self.outputName.setToolTip("Type in the name of the new Folder you would like to make for your Resume batch. \n Otherwise, this will use the current timestamp.")
        self.outputName.setFixedSize(300,30)
        #Select ouput folder button

        self.outputButton = QPushButton('Select Output Directory')
        self.outputButton.setToolTip("Click here to tell the generator where to put this batch of Resumes when it is finished.")
        self.outputButton.clicked.connect(lambda: self.openDir(self.currentDir))
        self.currentTest = QTextEdit()
        self.currentTest.setText("SportsCollegeList.csv")

        #Output Directory
        self.workLabel = QLabel("Output Directory")
        self.currentWork = QTextEdit()
        self.currentWork.setText("SportsCollegeList.csv")
        self.currentWork.layout()
        self.currentWork.setFixedSize(300,30)
        self.currentWork.setReadOnly(True)

        #Select work datafolder button
        self.workButton = QPushButton('Select Work Data (.CSV)')
        self.workButton.setToolTip("Click here to select a source file for the employment information in this Resume Batch.")
        self.workButton.clicked.connect(lambda: self.openDir(self.currentWork))

        #Select School Data

        self.workLabel = QLabel("Output Directory")
        self.currentSchool = QTextEdit()
        self.currentSchool.setText("Not Selected")
        self.currentSchool.layout()
        self.currentSchool.setFixedSize(300,30)
        self.currentSchool.setReadOnly(True)

        #Select work datafolder button
        self.schoolButton = QPushButton('Select Work Data (.CSV)')
        self.schoolButton.clicked.connect(lambda: self.openDir(self.currentWork))

        #Select test data
        
        self.testLabel = QLabel("Output Directory")
        self.currentTest = QTextEdit()
        self.currentTest.setText("SportsCollegeList.csv")
        self.currentTest.layout()
        self.currentTest.setFixedSize(300,30)
        self.currentTest.setReadOnly(True)
        self.testButton = QPushButton('Select Test Data (.CSV)')
        self.testButton.clicked.connect(lambda: self.openDir(self.currentTest))
        
        #Generate Resumes button
        self.begin = QPushButton('Generate Resumes')
        self.begin.clicked.connect(lambda: self.beginTask(self.currentTest.toPlainText()))
        
        
        layout = QGridLayout()
        self.box0.setLayout(layout)
        layout.addWidget(self.yearBeginLabel,0,0,1,2)
        layout.addWidget(self.monthBegin,1,0,1,1)
        layout.addWidget(self.yearBegin,1,1,1,1)
        layout.addWidget(self.yearEndLabel,2,0,1,2)
        layout.addWidget(self.monthEnd,3,0,1,1)
        layout.addWidget(self.yearEnd,3,1,1,1)
        
        layout.addWidget(self.yearWorkBeginLabel,4,0,1,2)
        layout.addWidget(self.monthWorkBegin,5,0,1,1)
        layout.addWidget(self.yearWorkBegin,5,1,1,1)
        layout.addWidget(self.yearWorkEndLabel,6,0,1,2)
        layout.addWidget(self.monthWorkEnd,7,0,1,1)
        layout.addWidget(self.yearWorkEnd,7,1,1,1)
        
        layout1 = QGridLayout()
        self.box8.setLayout(layout1)
        layout1.addWidget(self.testSectionLabel1, 0,0,1,1)
        layout1.addWidget(self.testSectionLabel3, 1,0,1,1)
        layout1.addWidget(self.sectionSelect,0,1,1,1)
        layout1.addWidget(self.modeSelect,1,1,1,1)
        
        layout2 = QGridLayout()
        self.box7.setLayout(layout2)
        layout2.addWidget(self.wLabel,0,0,1,1)
        layout2.addWidget(self.bLabel,1,0,1,1)
        layout2.addWidget(self.hLabel,0,2,1,1)
        layout2.addWidget(self.aLabel,2,0,1,1)
        layout2.addWidget(self.wPercent,0,1,1,1)
        layout2.addWidget(self.bPercent,1,1,1,1)
        layout2.addWidget(self.hPercent,0,3,1,1)
        layout2.addWidget(self.aPercent,2,1,1,1)
        layout2.addWidget(self.gLabel,3,1,1,1)
        layout2.addWidget(self.gPercent,3,2,1,2)
        
        layout = QGridLayout()
        self.box5.setLayout(layout)
        layout.addWidget(self.begin,0,0,1,2)

        
        layout3 = QGridLayout()
        layout3.addWidget(self.testButton,0,0,1,2)
        layout3.addWidget(self.currentTest,1,0,1,2)
        self.box4.setLayout(layout3)

        layout4 = QGridLayout()

        layout4.addWidget(self.outputButton,0,0,1,2)
        layout4.addWidget(self.currentDir,1,0,1,2)
        layout4.addWidget(self.outputLabel,2,0,1,2)
        layout4.addWidget(self.outputName,3,0,1,2)
        self.box6.setLayout(layout4)
    #▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    #
    def openDir(self, target):
        fileName = QFileDialog()
        filenames = list()
        if fileName.exec_():
            fileNames = fileName.selectedFiles()
            target.setText(fileNames[0])
    #▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    #
    def beginTask(self, path):
        self.beginGen(path)
 
        
    def beginGen(self,path):
    
        self.params["White"] = self.wPercent.toPlainText()
        self.params["Black"] = self.bPercent.toPlainText()
        self.params["Hispanic"] = self.hPercent.toPlainText()
        self.params["Asian"] = self.aPercent.toPlainText()
        self.params["GenderRatio"] = self.gPercent.toPlainText()
        self.params["TestMode"] = str(self.modeSelect.currentText())
        self.params["TestSection"] = str(self.sectionSelect.currentText())
        self.params["BeginYear"] = str(self.yearWorkBegin.currentText())
        self.params["EndYear"] = str(self.yearWorkEnd.currentText())
        self.params["BeginMonth"] = str(self.monthWorkBegin.currentText())
        self.params["EndMonth"] = str(self.monthWorkEnd.currentText())
        self.params["workPath"] = "work.csv"
        self.params["BeginYearEdu"] = str(self.yearBegin.currentText())
        self.params["EndYearEdu"] = str(self.yearEnd.currentText())
        self.params["BeginMonthEdu"] = str(self.monthBegin.currentText())
        self.params["EndMonthEdu"] = str(self.monthEnd.currentText())
    
        print(self.params)
        Printer.begin(self.currentDir.toPlainText(),path, self.outputName.toPlainText(), self.params)
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

#main function calls
app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
    
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    

