class Dokument:
    def create(self):
        raise NotImplementedError("Metoda create() musi byt prepisana")
class PDFDokument(Dokument):
    def create(self):
        return "Vytvaram PDF dokument"
class WordDokument(Dokument):
    def create(self):
        return "Vytvaram Word dokument"

class TXTDocument(Dokument):
    def create(self):
        return ("Vytvratam TXT")

class Factory:
    def create_dokument(self, type):
        if type == "PDF":
            return PDFDokument()
        elif type == "word":
            return WordDokument()
        elif type == "txt":
            return TXTDocument()
        else:
            raise ValueError("Neznamy typ")

factory = Factory()
pdf = factory.create_dokument("PDF")
print(pdf.create())

word = factory.create_dokument("word")
print(word.create())

txt = factory.create_dokument("txt")
print(txt.create())