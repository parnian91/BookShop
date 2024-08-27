from django.db import models

# Create your models here.

class Authors(models.Model):
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    birth_date = models.DateField()
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True) # valid input: http\https://www.name.domain
    
    @property
    def full_name(self):
        return f"{self.Fname} {self.Lname}"

    # def save(self, *args, **kwargs):
    #     self.__send_email()
    #     return super().save(*args, **kwargs)
    
    # def __send_email(self): ...


    def __str__(self) -> str:
        return f'{self.Fname} {self.Lname}'

class Employees(models.Model): # in view, set the permission class to IsAdminUser
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    birth_date = models.DateField()
    salary = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.Fname} {self.Lname}'

class Books(models.Model): # in view, set the permission class to IsAthenticated
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Authors, on_delete=models.DO_NOTHING)
    genre = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    price = models.CharField(max_length=300)
    publishing_yaer = models.IntegerField()
    discount = models.IntegerField(null=True)
    price_after_discount = models.CharField(max_length=300, null=True)
    
    def __str__(self) -> str:
        return self.title

class Buyers(models.Model): # in view, set the permission class to IsAthenticated
    buyer_fname = models.CharField(max_length=200)
    buyer_lname = models.CharField(max_length=200)
    bought_book = models.ForeignKey(Books, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.buyer_fname} {self.buyer_lname}'
