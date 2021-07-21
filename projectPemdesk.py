import sys
from PyQt5 import QtCore, QtWidgets, QtSql
from PyQt5.QtWidgets import *
from datetime import date


class MainWindow(QtWidgets.QWidget):

    update_table = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Input Pesanan Pembeli')
        self.setMinimumWidth(850)
        self.setMinimumHeight(650)
        self.setStyleSheet("background-color: rgb(238, 255, 235);")
        layoutUtama = QVBoxLayout()
        layout = QtWidgets.QGridLayout()
        self.setLayout(layoutUtama)

        layoutUtama.addLayout(layout)

        lbl1 = QLabel("Aplikasi Antrian Kedai Kopi")
        lbl1.setStyleSheet("font-size:24px; font-family: Times new roman;")
        lbl1.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lbl1, 0, 0, 1, 6)

        lblnm = QLabel("Nama Pembeli : ")
        lblnm.setStyleSheet("font-size: 14px;")
        self.leNamaBeli = QLineEdit()
        self.leNamaBeli.setStyleSheet("background-color: white;")
        layout.addWidget(lblnm, 1, 0)
        layout.addWidget(self.leNamaBeli, 1, 1)

        lblnm = QLabel("Tanggal : ")
        lblnm.setStyleSheet("font-size: 14px;")
        self.letgl = QLineEdit()
        self.letgl.setStyleSheet("background-color: white;")
        layout.addWidget(lblnm, 1, 4)
        layout.addWidget(self.letgl, 1, 5)
        today = date.today()
        d4 = today.strftime("%d-%m-%Y")
        self.letgl.setText(d4)


        lbl = QLabel("Klik + atau - untuk menambah atau mengurangi jumlah pesanan")
        layout.addWidget(lbl, 2, 0, 1, 4)

        lblMenu = QLabel("Menu")
        lblMenu.setStyleSheet("font-Weight: bold; font-size: 17px;")
        lblMenu.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lblMenu, 3, 0)
        lblHarga = QLabel("Harga")
        lblHarga.setStyleSheet("font-Weight: bold; font-size: 17px;")
        lblHarga.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lblHarga, 3, 1)
        lblJumlah = QLabel("Jumlah")
        lblJumlah.setStyleSheet("font-Weight: bold; font-size: 17px;")
        lblJumlah.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lblJumlah, 3, 4)
        lblsubtotal = QLabel("Sub-Total Harga")
        lblsubtotal.setStyleSheet("font-Weight: bold; font-size: 17px;")
        lblsubtotal.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lblsubtotal, 3, 5)

        lblnmMKN = QLabel("Kopi")
        lblnmMKN.setStyleSheet("font-size: 14px;")
        lblnmMKN.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lblnmMKN, 4, 0)
        lblnmMKN = QLabel("Rp. 5.000")
        lblnmMKN.setStyleSheet("font-size: 14px;")
        lblnmMKN.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lblnmMKN, 4, 1)
        self.tamb1 = QPushButton("+")
        self.krng1 = QPushButton("-")
        layout.addWidget(self.tamb1, 4, 2)
        layout.addWidget(self.krng1, 4, 3)
        self.lblStatus1 = QLabel("0")
        self.lblStatus1.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.lblStatus1, 4, 4)
        self.lblStatus1har = QLabel("Rp. 0")
        self.lblStatus1har.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.lblStatus1har, 4, 5)

        lblnmMKN = QLabel("Kopi Susu")
        lblnmMKN.setStyleSheet("font-size: 14px;")
        lblnmMKN.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lblnmMKN, 5, 0)
        lblnmMKN = QLabel("Rp. 7.000")
        lblnmMKN.setStyleSheet("font-size: 14px;")
        lblnmMKN.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lblnmMKN, 5, 1)
        self.tamb2 = QPushButton("+")
        self.krng2 = QPushButton("-")
        layout.addWidget(self.tamb2, 5, 2)
        layout.addWidget(self.krng2, 5, 3)
        self.lblStatus2 = QLabel("0")
        self.lblStatus2.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.lblStatus2, 5, 4)
        self.lblStatus2har = QLabel("Rp. 0")
        self.lblStatus2har.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.lblStatus2har, 5, 5)

        lblnmMKN = QLabel("Teh")
        lblnmMKN.setStyleSheet("font-size: 14px;")
        lblnmMKN.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lblnmMKN, 6, 0)
        lblnmMKN = QLabel("Rp. 4.000")
        lblnmMKN.setStyleSheet("font-size: 14px;")
        lblnmMKN.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lblnmMKN, 6, 1)
        self.tamb3 = QPushButton("+")
        self.krng3 = QPushButton("-")
        layout.addWidget(self.tamb3, 6, 2)
        layout.addWidget(self.krng3, 6, 3)
        self.lblStatus3 = QLabel("0")
        self.lblStatus3.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.lblStatus3, 6, 4)
        self.lblStatus3har = QLabel("Rp. 0")
        self.lblStatus3har.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.lblStatus3har, 6, 5)

        lblnmMKN = QLabel("Susu")
        lblnmMKN.setStyleSheet("font-size: 14px;")
        lblnmMKN.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lblnmMKN, 7, 0)
        lblnmMKN = QLabel("Rp. 6.000")
        lblnmMKN.setStyleSheet("font-size: 14px;")
        lblnmMKN.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lblnmMKN, 7, 1)
        self.tamb4 = QPushButton("+")
        self.krng4 = QPushButton("-")
        layout.addWidget(self.tamb4, 7, 2)
        layout.addWidget(self.krng4, 7, 3)
        self.lblStatus4 = QLabel("0")
        self.lblStatus4.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.lblStatus4, 7, 4)
        self.lblStatus4har = QLabel("Rp. 0")
        self.lblStatus4har.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.lblStatus4har, 7, 5)

        lblnmMKN = QLabel("Mie")
        lblnmMKN.setStyleSheet("font-size: 14px;")
        lblnmMKN.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lblnmMKN, 8, 0)
        lblnmMKN = QLabel("Rp. 6.000")
        lblnmMKN.setStyleSheet("font-size: 14px;")
        lblnmMKN.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lblnmMKN, 8, 1)
        self.tamb5 = QPushButton("+")
        self.krng5 = QPushButton("-")
        layout.addWidget(self.tamb5, 8, 2)
        layout.addWidget(self.krng5, 8, 3)
        self.lblStatus5 = QLabel("0")
        self.lblStatus5.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.lblStatus5, 8, 4)
        self.lblStatus5har = QLabel("Rp. 0")
        self.lblStatus5har.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.lblStatus5har, 8, 5)

        layout.addWidget(QLabel(""), 9, 0)
        lblTotalharga = QLabel("Total Harga : ")
        lblTotalharga.setStyleSheet("font-Weight: bold; font-size: 16px;")
        layout.addWidget(lblTotalharga, 10, 0)
        self.lblTotal = QLabel("Rp. 0")
        self.lblTotal.setStyleSheet("font-Weight: bold; font-size: 16px;")
        layout.addWidget(self.lblTotal, 10, 1, 1, 2)
        self.inputButt = QPushButton("Masuk Antrian")
        layout.addWidget(self.inputButt, 10, 3)
        # self.refreshButt = QPushButton("Refresh Tabel")
        # layout.addWidget(self.refreshButt, 10, 4)

        self.tableView = QTableView()
        layout.addWidget(self.tableView, 11, 0, 5, 6)

        lblselesai = QLabel("No.Pesanan Selesai: ")
        lblselesai.setStyleSheet("font-size: 14px;")
        self.leSelesai = QLineEdit()
        self.leSelesai.setStyleSheet("background-color: white;")
        layout.addWidget(lblselesai, 17, 0, 1, 2)
        layout.addWidget(self.leSelesai, 17, 1)
        self.buttSelesai = QPushButton("Pesanan Selesai")
        layout.addWidget(self.buttSelesai, 18, 0)


        self.tamb1.clicked.connect(lambda: self.menu1("+"))
        self.krng1.clicked.connect(lambda: self.menu1("-"))
        self.tamb2.clicked.connect(lambda: self.menu2("+"))
        self.krng2.clicked.connect(lambda: self.menu2("-"))
        self.tamb3.clicked.connect(lambda: self.menu3("+"))
        self.krng3.clicked.connect(lambda: self.menu3("-"))
        self.tamb4.clicked.connect(lambda: self.menu4("+"))
        self.krng4.clicked.connect(lambda: self.menu4("-"))
        self.tamb5.clicked.connect(lambda: self.menu5("+"))
        self.krng5.clicked.connect(lambda: self.menu5("-"))
        self.totMenu1 = 0
        self.totMenu2 = 0
        self.totMenu3 = 0
        self.totMenu4 = 0
        self.totMenu5 = 0

        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName("kedaiKopi.db")
        self.db.open()
        self.readDB()
        self.inputButt.clicked.connect(self.masukAntri)
        self.buttSelesai.clicked.connect(self.pesananSelesai)


    def TotalHarga(self): # menghitung total harga
        self.total = self.totMenu1 + self.totMenu2 + self.totMenu3 + self.totMenu4 + self.totMenu5
        self.lblTotal.setText("Rp. " + str(self.total))

    def menu1(self, tanda):
        self.temp1 = int(self.lblStatus1.text())
        if tanda == "+" : # and temp <= 9:
            self.temp1 = self.temp1 + 1
            self.lblStatus1.setText(str(self.temp1))
        elif tanda == "-" and self.temp1 > 0:
            self.temp1 = self.temp1 - 1
            self.lblStatus1.setText(str(self.temp1))
        elif tanda == "0":
            self.temp1 = 0
            self.lblStatus1.setText(str(self.temp1))
        self.totMenu1 = self.temp1 * 5000
        self.lblStatus1har.setText("Rp. " + str(self.totMenu1))
        self.TotalHarga()

    def menu2(self, tanda):
        self.temp2 = int(self.lblStatus2.text())
        if tanda == "+":
            self.temp2 = self.temp2 + 1
            self.lblStatus2.setText(str(self.temp2))
        elif tanda == "-" and self.temp2 > 0:
            self.temp2 = self.temp2 - 1
            self.lblStatus2.setText(str(self.temp2))
        elif tanda == "0":
            self.temp2 = 0
            self.lblStatus2.setText(str(self.temp2))
        self.totMenu2 = self.temp2 * 7000
        self.lblStatus2har.setText("Rp. " + str(self.totMenu2))
        self.TotalHarga()

    def menu3(self, tanda):
        self.temp3 = int(self.lblStatus3.text())
        if tanda == "+":
            self.temp3 = self.temp3 + 1
            self.lblStatus3.setText(str(self.temp3))
        elif tanda == "-" and self.temp3 > 0:
            self.temp3 = self.temp3 - 1
            self.lblStatus3.setText(str(self.temp3))
        elif tanda == "0":
            self.temp3 = 0
            self.lblStatus3.setText(str(self.temp3))
        self.totMenu3 = self.temp3 * 4000
        self.lblStatus3har.setText("Rp. " + str(self.totMenu3))
        self.TotalHarga()

    def menu4(self, tanda):
        self.temp4 = int(self.lblStatus4.text())
        if tanda == "+":
            self.temp4 = self.temp4 + 1
            self.lblStatus4.setText(str(self.temp4))
        elif tanda == "-" and self.temp4 > 0:
            self.temp4 = self.temp4 - 1
            self.lblStatus4.setText(str(self.temp4))
        elif tanda == "0":
            self.temp4 = 0
            self.lblStatus4.setText(str(self.temp4))
        self.totMenu4 = self.temp4 * 6000
        self.lblStatus4har.setText("Rp. " + str(self.totMenu4))
        self.TotalHarga()

    def menu5(self, tanda):
        self.temp5 = int(self.lblStatus5.text())
        if tanda == "+" :
            self.temp5 = self.temp5 + 1
            self.lblStatus5.setText(str(self.temp5))
        elif tanda == "-" and self.temp5 > 0:
            self.temp5 = self.temp5 - 1
            self.lblStatus5.setText(str(self.temp5))
        elif tanda == "0":
            self.temp5 = 0
            self.lblStatus5.setText(str(self.temp5))
        self.totMenu5 = self.temp5 * 6000
        self.lblStatus5har.setText("Rp. " + str(self.totMenu5))
        self.TotalHarga()

    def masukAntri(self): # memasukkan pesanan pada antrian
        list = [self.lblStatus1.text(), self.lblStatus2.text(), self.lblStatus3.text(), self.lblStatus4.text(),
                self.lblStatus5.text()]
        menu = ["Kopi","Kopi_Susu","Teh","Susu","Mie"]
        cek = 0
        pesanan = ""

        for i in range(len(list)):
            if list[i] == "0":
                cek += 1
            else:
                if list[i] != "0":
                    pesanan += f"{menu[i]}({list[i]}) "

        if self.leNamaBeli.text() == "" or cek == 5:# cek input
            QMessageBox.about(self, "Peringatan", "Nama Pembeli atau Pesanan Harus diisi!")
        else:
            idIn = self.letgl.text()
            nameIn = self.leNamaBeli.text()
            totalHarga = str(self.total)
            status = "Proses Pembuatan"

            query = QtSql.QSqlQuery() # inisialisasi query
            query.prepare("""INSERT INTO pesanan (Nama, Pesanan, Total_Harga, Status, waktu) VALUES (:nameIn, :pesananIn, :totalIn, :statusIn, :idIn )""")

            query.bindValue(":idIn", idIn) # mengganti nilai sesuai input
            query.bindValue(":nameIn", nameIn)
            query.bindValue(":pesananIn", pesanan)
            query.bindValue(":totalIn", totalHarga)
            query.bindValue(":statusIn", status)


            if query.exec_(): # eksekusi query dan cek error
                self.readDB()
                #self.noPesanan += 1
                self.update_table.emit()
                self.leNamaBeli.setText("")

                self.menu5("0")
                self.menu4("0")
                self.menu3("0")
                self.menu2("0")
                self.menu1("0")

            else:
                print("gagal proses query masuk antrian")

    def readDB(self): # method untuk membaca tabel dan menampilkannya di tableview

        model = QtSql.QSqlTableModel()
        model.setTable("pesanan")
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()
        self.tableView.setModel(model)
        self.update_table.emit()

        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

        fnt = self.tableView.font()
        fnt.setPointSize(10)
        self.tableView.setFont(fnt)

    def pesananSelesai(self): # mengganti status pesanan
        if self.leSelesai.text() == "":
            QMessageBox.about(self, "Peringatan", "masukkan nomor pesanan yang sesuai")
        else:
            noIn = self.leSelesai.text() # ambil setiap input user dari line edit

            query = QtSql.QSqlQuery()  # inisialisasi query
            query.prepare("""UPDATE pesanan SET Status='Selesai' WHERE No_Pesanan=:noIn""")

            query.bindValue(":noIn", noIn)  # mengganti nilai sesuai input

            if query.exec_():  # eksekusi query dan cek error
                self.readDB()
                self.leSelesai.setText("")
            else:
                print("edit status gagal")

class MainWindow1(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Antrian Pembeli')
        self.setMinimumWidth(1200)
        self.setMinimumHeight(630)
        layout1 = QtWidgets.QVBoxLayout()
        layout2 = QtWidgets.QVBoxLayout()
        layoutUtama = QGridLayout()
        layoutUtama.addLayout(layout1, 1,1)
        layoutUtama.addWidget(QLabel(""), 1,2)
        layoutUtama.addLayout(layout2, 1,3)
        self.setLayout(layoutUtama)

        lbl1 = QLabel("Antrian Pembeli")
        lbl1.setStyleSheet("font-size:24px;")
        lbl1.setAlignment(QtCore.Qt.AlignCenter)
        layoutUtama.addWidget(lbl1, 0,0,1,4)

        lbl1 = QLabel("Pesanan sedang dalam proses pembuatan : ")
        lbl1.setStyleSheet("font-size:20px;")
        layout1.addWidget(lbl1)

        self.tableViewantri2 = QTableView()
        layout1.addWidget(self.tableViewantri2)

        lbl1 = QLabel("Pesanan dapat diambil di meja kasir : ")
        lbl1.setStyleSheet("font-size:20px;")
        layout2.addWidget(lbl1)

        self.tableViewantri3 = QTableView()
        layout2.addWidget(self.tableViewantri3)

        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName("kedaiKopi.db")
        self.db.open()
        self.updateTable2()
        self.updateTable3()


    def updateTable2(self):
        projectModel = QtSql.QSqlQueryModel()  # inisialisasi query
        projectModel.setQuery("select No_Pesanan, Nama, Status from pesanan where Status = 'Proses Pembuatan'", self.db)  # mengatur query
        self.tableViewantri2.setModel(projectModel)  # menampilkan tabel hasil query
        self.tableViewantri2.show()
        self.updateTable3()

        header = self.tableViewantri2.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        fnt = self.tableViewantri2.font()
        fnt.setPointSize(22)
        self.tableViewantri2.setFont(fnt)


    def updateTable3(self):
        projectModel = QtSql.QSqlQueryModel()  # inisialisasi query
        projectModel.setQuery("select No_Pesanan, Nama, Status from pesanan Where status = 'Selesai' ORDER BY No_Pesanan DESC", self.db)  # mengatur query
        self.tableViewantri3.setModel(projectModel)  # menampilkan tabel hasil query
        self.tableViewantri3.show()

        header = self.tableViewantri3.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        fnt = self.tableViewantri3.font()
        fnt.setPointSize(22)
        self.tableViewantri3.setFont(fnt)


class Controller:

    def __init__(self):
        pass

    def show_main(self):
        self.window = MainWindow()
        self.window1 = MainWindow1()
        self.window.update_table.connect(self.show_main1)
        self.window.show()
        self.window1.show()

    def show_main1(self):
        self.window1.updateTable2()

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()