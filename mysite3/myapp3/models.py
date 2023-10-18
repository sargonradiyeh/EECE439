from django.db import models
from datetime import date 

class ContactList(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    profession = models.CharField(max_length=100)
    confirmprofession = models.CharField(max_length=100,default="X")
    telnumber = models.IntegerField()
    email = models.EmailField()
    datejoined= models.DateTimeField(default=date.today)
    dateexpired=models.DateTimeField(default=date.today)
    

    def save(self, *args, **kwargs):#forcefuly capitalize the first letter of every "word" in the field
        self.name = self.name.title()
        self.profession = self.profession.title()
        self.confirmprofession = self.confirmprofession.title()
        super(ContactList, self).save(*args, **kwargs)

    def __str__(self):
      return f"{self.telnumber} for {self.name}"


