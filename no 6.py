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

class Mahasiswa:
    SARJANA = "SARJANA"
    MASTER = "MASTER"
    DOKTOR = "DOKTOR"

    def __init__(self, nama_depan, nama_belakang, nomor_id, jenjang):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, matkul):
        self.matkul.append(matkul)

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}, ID: {self.nomor_id}, Jenjang: {self.jenjang}, Matkul: {self.matkul}"

class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_id, status_karyawan)
        self.matkul_diajar = []

    def mengajar(self, matkul):
        self.matkul_diajar.append(matkul)

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}, ID: {self.nomor_id}, Status Karyawan: {self.status_karyawan}, Matkul Diajar: {self.matkul_diajar}"

bowo = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)
bowo.enrol("Basis Data")
print(bowo)

rizki = Dosen("Rizky", "Setiabudi", "456789", Karyawan.TETAP)
rizki.mengajar("Statistik")
print(rizki)
