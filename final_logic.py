from PyQt6.QtWidgets import *
from guifinal import *
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Initialize an object
        """
        super().__init__()
        self.setupUi(self)

        self.radioButton_Evan.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_Meredith.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_Sam.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_Patrick.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_David.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_John.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_James.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_Chris.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_Avery.setGeometry(QtCore.QRect(230, 130, 0, 0))

        self.pushButton_party.clicked.connect(lambda: self.party_select())
        self.pushButton_candidate.clicked.connect(lambda: self.candidate_select())
        self.pushButton_back.clicked.connect(lambda: self.back_select())

        self.selected_color: str = ""
        self.pin: str = None

    def party_select(self):
        """
        Function for selecting a party and entering the user's pin
        """
        pin, ok = QInputDialog.getText(self, 'Input PIN', 'Enter your 4-digit PIN:')
        if ok and self.validate_pin(pin):
            if not self.is_pin_in_csv(pin):
                self.pin = pin

                if self.radioButton_yellow.isChecked():
                    self.selected_color = "Yellow"
                    self.clear_to_vote(self.selected_color)
                    self.radioButton_David.setGeometry(QtCore.QRect(50, 130, 131, 41))
                    self.radioButton_David.setEnabled(True)
                    self.radioButton_John.setGeometry(QtCore.QRect(50, 160, 131, 41))
                    self.radioButton_John.setEnabled(True)
                    self.radioButton_James.setGeometry(QtCore.QRect(50, 190, 131, 41))
                    self.radioButton_James.setEnabled(True)

                elif self.radioButton_purple.isChecked():
                    self.selected_color = "Purple"
                    self.clear_to_vote(self.selected_color)
                    self.radioButton_Meredith.setGeometry(QtCore.QRect(50, 130, 171, 41))
                    self.radioButton_Meredith.setEnabled(True)
                    self.radioButton_Patrick.setGeometry(QtCore.QRect(50, 160, 131, 41))
                    self.radioButton_Patrick.setEnabled(True)
                    self.radioButton_Avery.setGeometry(QtCore.QRect(50, 190, 131, 41))
                    self.radioButton_Avery.setEnabled(True)

                elif self.radioButton_orange.isChecked():
                    self.selected_color = "Orange"
                    self.clear_to_vote(self.selected_color)
                    self.radioButton_Chris.setGeometry(QtCore.QRect(50, 130, 131, 41))
                    self.radioButton_Chris.setEnabled(True)
                    self.radioButton_Evan.setGeometry(QtCore.QRect(50, 160, 131, 41))
                    self.radioButton_Evan.setEnabled(True)
                    self.radioButton_Sam.setGeometry(QtCore.QRect(50, 190, 131, 41))
                    self.radioButton_Sam.setEnabled(True)

                else:
                    self.label_error.setText('Please Select a Party before pressing the "Select Party" button.')
            else:
                self.label_error.setText('This PIN is already used. Please enter a different PIN.')
        else:
            self.label_error.setText('Invalid PIN. Please enter a 4-digit number.')

    def candidate_select(self):
        """
        Function for selecting a candidate and sending the selected candidate to the save csv func
        """
        candidate: str = None
        if self.radioButton_David.isChecked():
            candidate = "David"
        elif self.radioButton_John.isChecked():
            candidate = "John"
        elif self.radioButton_James.isChecked():
            candidate = "James"
        elif self.radioButton_Meredith.isChecked():
            candidate = "Meredith"
        elif self.radioButton_Patrick.isChecked():
            candidate = "Patrick"
        elif self.radioButton_Avery.isChecked():
            candidate = "Avery"
        elif self.radioButton_Chris.isChecked():
            candidate = "Chris"
        elif self.radioButton_Evan.isChecked():
            candidate = "Evan"
        elif self.radioButton_Sam.isChecked():
            candidate = "Sam"

        if candidate and self.pin:
            self.save_to_csv(self.selected_color, candidate, self.pin)
            self.label_error.setText(f'You have selected {candidate} from the {self.selected_color} party.')
            self.back_select()

        else:
            self.label_error.setText(f'Please select a candidate before clicking Select Candidate')

    def validate_pin(self, pin: str) -> bool and int:
        """

        :param pin: The 4 digit pin that the user enters
        :return: If the pin is actually a digit and if the length is 4, else it is wrong
        """
        return pin.isdigit() and len(pin) == 4

    def is_pin_in_csv(self, pin: str) -> bool:
        """
        Function for determining if the pin entered has already been used to vote
        :param pin: The 4 digit pin that the user enters
        :return: Will return true if the pin is in the reader but false if it isn't or the file doesn't exist
        """
        try:
            with open('voting_results.csv', mode='r') as results:
                reader = csv.reader(results)
                for row in reader:
                    if row[2] == pin:
                        return True
        except FileNotFoundError:
            return False
        return False

    def save_to_csv(self, color: str, candidate: str, pin: str):
        """
        Function for saving the color, candidate and pin number to the output csv file
        :param color: The current party color of the selected candidate
        :param candidate: The current candidate the user selected
        :param pin: The 4 digit pin that the user enters
        """
        with open('voting_results.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([color, candidate, pin])

    def back_select(self):
        """
        Function for returning the user to the starting ui position
        """
        self.radioButton_Evan.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_Meredith.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_Sam.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_Patrick.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_David.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_John.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_James.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_Chris.setGeometry(QtCore.QRect(230, 130, 0, 0))
        self.radioButton_Avery.setGeometry(QtCore.QRect(230, 130, 0, 0))

        self.radioButton_David.setChecked(False)
        self.radioButton_John.setChecked(False)
        self.radioButton_James.setChecked(False)
        self.radioButton_Meredith.setChecked(False)
        self.radioButton_Patrick.setChecked(False)
        self.radioButton_Avery.setChecked(False)
        self.radioButton_Chris.setChecked(False)
        self.radioButton_Evan.setChecked(False)
        self.radioButton_Sam.setChecked(False)

        self.radioButton_Avery.setEnabled(False)
        self.radioButton_Patrick.setEnabled(False)
        self.radioButton_Meredith.setEnabled(False)
        self.radioButton_Sam.setEnabled(False)
        self.radioButton_Chris.setEnabled(False)
        self.radioButton_Evan.setEnabled(False)
        self.radioButton_John.setEnabled(False)
        self.radioButton_James.setEnabled(False)
        self.radioButton_David.setEnabled(False)

        self.radioButton_yellow.setGeometry(QtCore.QRect(50, 130, 131, 41))
        self.radioButton_purple.setGeometry(QtCore.QRect(50, 160, 131, 41))
        self.radioButton_orange.setGeometry(QtCore.QRect(50, 190, 131, 41))

        self.pushButton_party.setEnabled(True)
        self.pushButton_back.setEnabled(False)
        self.pushButton_candidate.setEnabled(False)

        self.label_second.setGeometry(QtCore.QRect(70, 20, 341, 20))
        self.label_top.setText('Welcome to the Voting Menu!')
        self.label_second.setText('Please select a political party to begin')

    def clear_to_vote(self, color: str):
        """
        Function for clearing the page to take the user to the voting page
        :param color: The current party page the user is under
        """
        self.radioButton_yellow.setGeometry(QtCore.QRect(50, 130, 0, 0))
        self.radioButton_purple.setGeometry(QtCore.QRect(50, 160, 0, 0))
        self.radioButton_orange.setGeometry(QtCore.QRect(50, 190, 0, 0))
        self.pushButton_candidate.setEnabled(True)
        self.pushButton_back.setEnabled(True)
        self.pushButton_party.setEnabled(False)
        self.label_error.setText("")
        self.label_top.setText(f'Welcome to the {color} menu!')
        self.label_second.setGeometry(QtCore.QRect(45, 20, 341, 20))
        self.label_second.setText("Please select a candidate or back to party menu.")
