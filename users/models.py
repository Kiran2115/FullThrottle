from django.db import models

# Create your models here.
class User(models.Model):
	user_id = models.SlugField(max_length = 200)
	real_name = models.CharField(max_length= 50)
	tz        = models.CharField(max_length =100)
	activity_periods = models.ForeignKey('Activity' , on_delete=models.CASCADE, related_name='activity')

	class Meta:
		db_table = "user"


class Activity(models.Model):
	start_time = models.DateTimeField(null=True, blank=True)
	end_time = models.DateTimeField(null=True, blank=True)

	class Meta:
		db_table = "activity"
