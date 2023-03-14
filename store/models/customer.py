from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=400)

    def register(self):
        self.save()    

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False    

    # check email macth or not
    def isExit(self):
        if Customer.objects.filter(email = self.email):
           return True
        
        return False
       
    