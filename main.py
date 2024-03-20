import sys


from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):



    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.addbutton.clicked.connect(self.dodaj)
        self.ui.delbutton.clicked.connect(self.usun_form)
        self.ui.zapis.clicked.connect(self.zapisz_form)

    def dodaj(self):
        nazwa = self.ui.produkt.toPlainText()
        ilosc = self.ui.ilosc.toPlainText()
        if(len(nazwa) <= 50):
            if( len(nazwa) > 1 & (len(ilosc) > 0 )):
                self.ui.lista.addItem("Nazwa: " + nazwa+ ", Ilosc: " + ilosc)
            else:
                self.ui.produkt.setText("Uzupelnij pola")
                self.ui.ilosc.setText("Uzupelnij pola")
        else:
            self.ui.produkt.setText("Tekst jest za długi")
            self.ui.ilosc.setText("Tekst jest za długi")
    def usun_form(self):
        indeks = self.ui.lista.currentIndex()
        #nie wiem jak :(
        deleteitem = self.ui.lista.item(indeks).deleteLater()

    def zapisz_form(self):
        list = self.ui.lista.__len__()
        for i in range(list):
            f = open("zapis.txt")
            f.write(str(self.ui.lista.itemFromIndex(self.ui.lista.currentIndex())))
            f.close()








if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())