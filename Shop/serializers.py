from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Authors, Employees, Books, Buyers

# sepehr:1234
# admin1:admin1@sepehr

class AuthorsSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Authors
        fields = ["full_name", 'Fname', 'Lname', 'birth_date', 'email', 'website', ]

    def get_full_name(self, obj:Authors):
        return obj.full_name

    # def get_count(self, obj):
    #     return 2

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['Fname', 'Lname', 'birth_date', 'salary', 'email']

class BooksSerializer(serializers.ModelSerializer):
    # authors = AuthorsSerializer(many=True, read_only=True)

    class Meta:
        model = Books
        fields = ['title', 'author', 'genre', 'publisher', 'price', 'publishing_yaer', 'discount', 'price_after_discount']

    # def create(self, validated_data): # this is work
    #     author = validated_data.get('author')
    #     cnt =  Books.objects.filter(author=author).count()
    #     if cnt >= 3:
    #         raise ValidationError("The author already has 10 or more books.")
    #     else:
    #         return super().create(validated_data)
    
    # def save(self, **kwargs):
    #     cnt = self.authors.objects.filter(name=self.validated_data['name']).count()
    #     if cnt >= 10:
    #         raise KeyError
    #     else:
    #         return super().save(**kwargs)

class BuyersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyers
        fields = ['buyer_fname', 'buyer_lname', 'bought_book']



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']