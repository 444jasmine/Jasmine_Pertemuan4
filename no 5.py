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

bowo = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)
bowo.enrol("Basis Data")
print(bowo)

