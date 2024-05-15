import random
import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPalette, QColor

qtCreatorFile = "sorteo.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# Crear un diccionario vacío
numerosaleatorios = []

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.primer_click = False
        
        # aca va el boton
        self.pushButton_sorteo.clicked.connect(self.sortear)


    def showEvent(self, event):
        print('La ventana se ha cargado. Aquí puedes ejecutar tu código.')
        # Aquí puedes colocar el código que deseas ejecutar al cargar la ventana
        i = 0
        for i in range(10):
            self.tableWidget.insertRow(i)
            self.tableWidget.insertColumn(i)

        Dato=0

        i = 0
        for i in range(10):
            #print(i)
            j = 0
            for j in range(10):
                cell = QtWidgets.QTableWidgetItem(str(Dato))
                self.tableWidget.setItem(i,j,cell)
                Dato=Dato + 1
        for i in range(10):
            self.tableWidget.resizeColumnToContents(i)
        
        
    def sortear(self):
        # verifico que no se repita el numero al azar
        
        encontre = True
        if not self.primer_click:
            print('¡Es la primera vez que se ha pulsado el botón!')
            self.primer_click = True
            numero = random.randint(1, 100)
            numerosaleatorios.append(numero)
            print(numerosaleatorios) 
        else:
            print('Ya se ha pulsado el botón anteriormente.')
            numero = random.randint(1, 100)
            while encontre:
                encontre = False
                for valor in numerosaleatorios:
                    if (valor == numero):
                        encontre = True
                        #dato repetido
                        print("dato repetido")
                        numero = random.randint(1, 100)
                        break
            numerosaleatorios.append(numero)
            print(numerosaleatorios) 

        palette = QPalette()
        palette.setColor(QPalette.Foreground, QColor("red"))
        self.label.setPalette(palette)
        self.label.setText(str(numero))
        columna = numero % 10
        numero = numero // 10
        fila = numero % 10
        #con el 100 devuelve 0 0 
        self.tableWidget.item( fila, columna).setBackground(QtGui.QColor("red"))
        
    def llenar(self):
        i = 0
        for i in range(10):
            self.tableWidget.insertRow(i)
            self.tableWidget.insertColumn(i)

        Dato=0

        i = 0
        for i in range(10):
            #print(i)
            j = 0
            for j in range(10):
                cell = QtWidgets.QTableWidgetItem(str(Dato))
                self.tableWidget.setItem(i,j,cell)
                Dato=Dato + 1
        for i in range(10):
            self.tableWidget.resizeColumnToContents(i)
        


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
