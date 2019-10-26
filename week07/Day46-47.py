class library:
    def __init__(self, book, shilf):
        self.book = book 
        self.shilf = shilf
        print(self.book, self.shilf)
book = library("sss", 45)
print(book)
shilf = library("ssss", 45)
print(shilf)
print(library)
print(book)


class SciencSection(library):
    def __init__(self, book, shilf):
        super().__init__(book, shilf)

        self.name = "physics book"
Scienc = SciencSection(20, 40)   
print(Scienc.book, Scienc.shilf, Scienc.cname) 
