from django.db import models
#from django
from django.contrib import auth

# Create your models here.
class Admin(models.Model):
	#email = models.CharField(max_length=128)
	username = models.CharField(max_length=256)
	password = models.CharField(max_length=256)
	created_at = models.DateTimeField(blank=True, null=True)
	updated_at = models.DateTimeField(blank=True, null=True)
	is_admin = models.IntegerField(blank=True, null=True)
	is_deleted = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'cms_admin'

class User(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    email = models.CharField(max_length=128, blank=True)
    username = models.CharField(max_length=256, blank=True)
    password = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cms_user'

class Test(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    email = models.CharField(max_length=128, blank=True)
    username = models.CharField(max_length=256, blank=True)
    password = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'        