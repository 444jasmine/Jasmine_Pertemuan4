class Pengajar:
    def __init__(self):
        self.matkul_diajar = []
    
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)
        print(f"Mata kuliah {mata_kuliah} telah ditambahkan ke dalam daftar mata kuliah yang diajar.")
        
    def daftar_mata_kuliah(self):
        return self.matkul_diajar

pengajar1 = Pengajar()
pengajar1.mengajar("Matematika")
pengajar1.mengajar("Fisika")
print(pengajar1.daftar_mata_kuliah())  