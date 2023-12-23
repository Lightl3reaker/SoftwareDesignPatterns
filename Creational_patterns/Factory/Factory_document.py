from abc import ABC,abstractclassmethod

class Document(ABC):
    @abstractclassmethod
    def createdoc(self):
        pass

class ReportDocument(Document):
    def createdoc(self):
        return f"Created a report document."
class LetterDocument(Document):
    def createdoc(self):
        return f"Created a letter document."
class InvoiceDocument(Document):
    def createdoc(self):
        return f"Created a invoice document."
        
class DocumentCreator(ABC):
    @abstractclassmethod
    def connectdoc(self):
        pass
    def getdoc(self):
        doc=self.connectdoc()
        return doc.createdoc()

class ReportDocCreator(DocumentCreator):
    def connectdoc(self):
        return ReportDocument()
class LetterDocCreator(DocumentCreator):
    def connectdoc(self):
        return LetterDocument()
class InvoiceDocCreator(DocumentCreator):
    def connectdoc(self):
        return InvoiceDocument()

doc1=ReportDocCreator()
doc2=LetterDocCreator()
doc3=InvoiceDocCreator()
print("doc1 --> "+doc1.getdoc())
print("doc2 --> "+doc2.getdoc())
print("doc3 --> "+doc3.getdoc())