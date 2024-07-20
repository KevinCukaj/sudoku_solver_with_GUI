#!/usr/bin/python3 
# in order to use PyQt6, give the command "sudo apt install python3-pyqt6"
import sudoku_solver
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
	QApplication,
	QGridLayout,
	QLabel,
	QLineEdit,
	QPushButton,
	QWidget,
)


class Window(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle("Sudoku Solver")
		width = 400
		height = 300
		self.setFixedSize(width, height)


		self.inputs = []

		for i in range(9):
			for j in range(9):
				self.cell=QLineEdit(parent=self)
				self.cell.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
				self.cell.setInputMask('0')
				self.inputs.append(self.cell)

		layout = QGridLayout()	
		for i in range(9):
			for j in range(9):
				layout.addWidget(self.inputs[(i*9)+j], i, j)

		self.solve_btn = QPushButton(parent=self, text="Solve")
		self.reset_btn = QPushButton(parent=self, text="Reset")
		self.solve_btn.setStyleSheet("background-color: #234f23; color: #fff;")

		self.solve_btn.clicked.connect(self.solve)
		self.reset_btn.clicked.connect(self.reset)
		
		self.label = QLabel(parent=self, text="")

		layout.addWidget(self.solve_btn, 3, 11)
		layout.addWidget(self.reset_btn, 4, 11)
		layout.addWidget(self.label, 5, 11)

		#layout.addWidget(paste_button, 1, 1)
		self.setLayout(layout)

	def copy(self):
		self.source_line_edit.selectAll()
		self.source_line_edit.copy()

	def paste(self):
		self.dest_line_edit.clear()
		self.dest_line_edit.paste()

	def solve(self):
		M=[[None for i in range(9)] for j in range(9)]
		for i in range(9):
			for j in range(9):
				if self.inputs[(i*9)+j].text() != "":
					M[i][j]=int(self.inputs[(i*9)+j].text())
#		print(M)
		S=sudoku_solver.sudoku(M)
		if S == False:
			lineEdit = QLineEdit()
#			for i in range(9):
#				for j in range(9):
#					self.inputs[(i*9)+j].setText("0")
			self.label.setText("Not solvable")
		else:
			for i in range(9):
				for j in range(9):
					self.inputs[(i*9)+j].setText(str(S[i][j]))
	
	def reset(self):
		for i in range(9):
			for j in range(9):
				self.inputs[(i*9)+j].setText("")
		self.label.setText("")

app = QApplication([])
window = Window()
window.show()
app.exec()