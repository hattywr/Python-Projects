import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtCore import QXmlStreamWriter, QFile

class BudgetApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface
        self.setWindowTitle('Budget App')

        self.paycheck_label = QLabel('Paycheck Amount:')
        self.paycheck_amount = QLineEdit()

        self.housing_label = QLabel('Housing:')
        self.housing_amount = QLineEdit()

        self.transportation_label = QLabel('Transportation:')
        self.transportation_amount = QLineEdit()

        self.entertainment_label = QLabel('Entertainment:')
        self.entertainment_amount = QLineEdit()

        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.save_budget)

        # Use a grid layout to position the widgets
        layout = QGridLayout()
        layout.addWidget(self.paycheck_label, 0, 0)
        layout.addWidget(self.paycheck_amount, 0, 1)
        layout.addWidget(self.housing_label, 1, 0)
        layout.addWidget(self.housing_amount, 1, 1)
        layout.addWidget(self.transportation_label, 2, 0)
        layout.addWidget(self.transportation_amount, 2, 1)
        layout.addWidget(self.entertainment_label, 3, 0)
        layout.addWidget(self.entertainment_amount, 3, 1)
        layout.addWidget(self.save_button, 4, 1)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.load_budget()

    def save_budget(self):
        # Create an XML file and write the budget data to it
        file = QFile('budget.xml')
        file.open(QFile.WriteOnly | QFile.Text)
        writer = QXmlStreamWriter()
        writer.setDevice(file)
        writer.writeStartDocument()
        writer.writeStartElement('Budget')
        writer.writeTextElement('Paycheck', self.paycheck_amount.text())
        writer.writeTextElement('Housing', self.housing_amount.text())
        writer.writeTextElement('Transportation', self.transportation_amount.text())
        writer.writeTextElement('Entertainment', self.entertainment_amount.text())
        writer.writeEndElement()
        writer.writeEndDocument()
       
