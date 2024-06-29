class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}, ID: {self.nomor_id}"

class Karyawan(Orang):
    TETAP = "TETAP"
    TDK_TETAP = "TDK_TETAP"

    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_id)
        self.status_karyawan = status_karyawan

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}, ID: {self.nomor_id}, Status Karyawan: {self.status_karyawan}"

# Contoh penggunaan kelas Karyawan
orang1 = Orang("Edgina", "Jasmine", "123456")
print(orang1)

karyawan1 = Karyawan("Kim", "Taehyung", "456789", Karyawan.TETAP)
print(karyawan1)

karyawan2 = Karyawan("Jeon", "Jungkook", "987654", Karyawan.TDK_TETAP)
print(karyawan2)
