class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id
    
    def perkenalan(self):
        print(f"Nama saya {self.nama_depan} {self.nama_belakang} dengan nomor ID {self.nomor_id}.")

class Pelajar:
    def __init__(self):
        self.mata_kuliah_diambil = []
    
    def enrol(self, mata_kuliah):
        self.mata_kuliah_diambil.append(mata_kuliah)
        print(f"Telah mendaftar mata kuliah {mata_kuliah}.")
    
    def daftar_mata_kuliah(self):
        return self.mata_kuliah_diambil

class Pengajar:
    def __init__(self):
        self.matkul_diajar = []
    
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)
        print(f"Mata kuliah {mata_kuliah} telah ditambahkan ke dalam daftar mata kuliah yang diajar.")
        
    def daftar_mata_kuliah_ajar(self):
        return self.matkul_diajar

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        Orang.__init__(self, nama_depan, nama_belakang, nomor_id)
        Pelajar.__init__(self)
        Pengajar.__init__(self)

# Membuat objek dengan nama uswatun menggunakan kelas Asdos
uswatun = Asdos("Uswatun", "Hasanah", "456456")

# Memanggil method enrol dan memberikan argument “Big Data”
uswatun.enrol("Big Data")

# Memanggil method mengajar dan memberikan argument “Kecerdasan Artifisial”
uswatun.mengajar("Kecerdasan Artifisial")

# Output tambahan untuk melihat daftar mata kuliah yang diambil dan diajar
print(f"Mata kuliah yang diambil: {uswatun.daftar_mata_kuliah()}")
print(f"Mata kuliah yang diajar: {uswatun.daftar_mata_kuliah_ajar()}")
