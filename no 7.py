class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, matkul):
        self.matkul.append(matkul)

    def __str__(self):
        return f"Matkul yang diambil: {self.matkul}"

# Contoh penggunaan kelas Pelajar
pelajar1 = Pelajar()
pelajar1.enrol("Matematika")
pelajar1.enrol("Fisika")
print(pelajar1)
