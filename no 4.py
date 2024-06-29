class Karyawan:
    TETAP = "TETAP"
    TDK_TETAP = "TDK_TETAP"

    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id
        self.status_karyawan = status_karyawan

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}, ID: {self.nomor_id}, Status Karyawan: {self.status_karyawan}"

class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_id, status_karyawan)
        self.matkul_diajar = []

    def mengajar(self, matkul):
        self.matkul_diajar.append(matkul)

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}, ID: {self.nomor_id}, Status Karyawan: {self.status_karyawan}, Matkul Diajar: {self.matkul_diajar}"

# Contoh penggunaan kelas Dosen
dosen1 = Dosen("Michael", "Jordan", "13579", Karyawan.TETAP)
print(dosen1)

dosen1.mengajar("Pemrograman Python")
dosen1.mengajar("Data Science")
print(dosen1)
