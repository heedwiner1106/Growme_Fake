from pyexpat import model
from django.db import models as m

# Create your models here.
class User(m.Model):
    user_name = m.CharField(max_length=50,null=False)
    def __str__(self):
        return self.user_name




class SiteData(m.Model):
    created_user = m.ForeignKey(User, on_delete=m.SET_NULL, null=True)
    site_data = m.TextField(null=True)
    def __str__(self):
        return f'{self.created_user}, {self.site_data}'

