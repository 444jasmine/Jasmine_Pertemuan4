class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}, ID: {self.nomor_id}"

class Mahasiswa(Orang):
    SARJANA = "SARJANA"
    MASTER = "MASTER"
    DOKTOR = "DOKTOR"

    def __init__(self, nama_depan, nama_belakang, nomor_id, jenjang):
        super().__init__(nama_depan, nama_belakang, nomor_id)
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, matkul):
        self.matkul.append(matkul)

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}, ID: {self.nomor_id}, Jenjang: {self.jenjang}, Matkul: {self.matkul}"

orang1 = Orang("Edgina", "Jasmine", "123456")
print(orang1)

mahasiswa1 = Mahasiswa("Az Zahra", "Kartiko", "789012", Mahasiswa.SARJANA)
print(mahasiswa1)

mahasiswa1.enrol("Matematika")
mahasiswa1.enrol("Fisika")
print(mahasiswa1)

