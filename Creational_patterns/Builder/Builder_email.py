class EmailMessage():
    def __init__(self):
        self.sender=""
        self.recepient=""
        self.subject=""
        self.body=""
        self.attachments=[]
    def __str__(self):
         return f"Email Message\nSender: {self.sender}\nRecipient: {self.recepient}\nSubject: {self.subject}\nBody: {self.body}\nAttachments: {self.attachments}"

class EmailMessageBuilder():
    def __init__(self):
        self.message=EmailMessage()
    def set_sender(self,sender):
        self.message.sender=sender
        return self
    
    def set_recepient(self,recipient):
        self.message.recepient=recipient
        return self
    
    def set_subject(self,subject):
        self.message.subject=subject
        return self
    def set_body(self,body):
        self.message.body=body
        return self
    def set_attachment(self,attachment):
        self.message.attachments.append(attachment)
        return self
    def get_email(self):
        return self.message

builder=EmailMessageBuilder()
builder.set_sender("sender@gmail.com").set_recepient("receiver@gmail.com").set_subject("Hello buddy").set_body("Thie ie an example meaning.").set_attachment("image.jpg").set_attachment("file.txt")
print(builder.get_email())
