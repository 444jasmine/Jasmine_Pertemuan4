class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def perkenalan(self):
        print(f"Nama saya {self.nama} dan saya berumur {self.umur} tahun.")

class Pelajar:
    def __init__(self, jurusan):
        self.jurusan = jurusan
    
    def belajar(self):
        print(f"Saya belajar di jurusan {self.jurusan}.")

class Pengajar:
    def __init__(self):
        self.matkul_diajar = []
    
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)
        print(f"Mata kuliah {mata_kuliah} telah ditambahkan ke dalam daftar mata kuliah yang diajar.")
        
    def daftar_mata_kuliah(self):
        return self.matkul_diajar

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama, umur, jurusan):
        Orang.__init__(self, nama, umur)
        Pelajar.__init__(self, jurusan)
        Pengajar.__init__(self)

# Contoh penggunaan kelas Asdos
asdos1 = Asdos("Budi", 22, "Teknik Informatika")
asdos1.perkenalan()
asdos1.belajar()
asdos1.mengajar("Algoritma dan Struktur Data")
asdos1.mengajar("Pemrograman Berorientasi Objek")
print(asdos1.daftar_mata_kuliah())  # Output: ['Algoritma dan Struktur Data', 'Pemrograman Berorientasi Objek']
