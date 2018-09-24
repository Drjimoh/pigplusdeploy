from django.db import models
from django.utils import timezone


class NewRecord(models.Model):
	farmer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	pigname = models.CharField(max_length=20)
	litter_number = models.CharField(max_length=20) 
	sex = models.CharField(max_length=20)
	pig_weight = models.CharField(max_length=20)
	pig_age = models.CharField(max_length=20)
	breed_type = models.CharField(max_length=50)
	pig_color = models.CharField(max_length=20)
	created_date = models.DateTimeField(default=timezone.now)

	def add_record(self):
		self.created_date = timezone.now()
		self.save()

	def __str__(self):
		return self.pigname

'''income data
dateofincome
typeofincome
amount
add comment

expenditure
dateofexpenditure
type 
amount 
comment
'''

