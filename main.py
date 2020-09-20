import csv
import os
import sys
import camelot
from PyQt5 import QtWidgets
import design

class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadFileButton.clicked.connect(self.browse_folder)

    def browse_folder(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите папку")
        if directory:
            tables = camelot.read_pdf(directory[0], pages='1,2,3,4')
            tables.export('export.csv', f='csv', compress=False)
            self.readFiles()
            self.deleteFiles()


    def readFiles(self):
        with open('export-page-1-table-2.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            # print(list(reader))
            for row in reader:
                print(row)

        with open('export-page-2-table-1.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            # print(list(reader))
            for row in reader:
                print(row)

        with open('export-page-3-table-2.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            # print(list(reader))
            for row in reader:
                print(row)

        with open('export-page-4-table-1.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            # print(list(reader))
            for row in reader:
                print(row)

    def deleteFiles(self):
        os.remove('export-page-1-table-2.csv')
        os.remove('export-page-2-table-1.csv')
        os.remove('export-page-3-table-2.csv')
        os.remove('export-page-4-table-1.csv')
        os.remove('export-page-1-table-1.csv')
        os.remove('export-page-3-table-1.csv')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':
    main()