from django.db import models

# Create your models here.
class BitcoinPrice(models.Model):
	update_date = models.CharField(max_length=100)
	kes = models.FloatField()
	usd = models.FloatField()
	time_added = models.DateTimeField()

	def __str__(self):
		return self.update_date

