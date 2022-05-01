from django.db import models
from django.conf import settings


class SetUpModel(models.Model):

  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  schema_choices = (
    ('basket_indices', 'Basket Indices'),
    ('bond', 'Bond'),
    ('cryptocurrencies', 'Cryptocurrencies'),
    ('economy', 'Economy'),
    ('forex', 'Forex'),
    ('futures_indices', 'Futures Indices'),
    ('stock_indices', 'Stock Indices'),
    ('synthetic_indices', 'Synthetic Indices'),
  )
  schema = models.CharField(max_length=50, choices=schema_choices, blank=False)
  Asset_Name = models.CharField(max_length=50, blank=False)

  Image_before = models.ImageField(upload_to='setup_Model/%Y/%m/%d')
  Image_before2 = models.ImageField(upload_to='setup_Model/%Y/%m/%d', null=True, blank=True)
  bias = models.TextField()

  Image_after = models.ImageField(upload_to='setup_Model/%Y/%m/%d', null=True, blank=True)
  Image_after2 = models.ImageField(upload_to='setup_Model/%Y/%m/%d', null=True, blank=True)

  CHOICES = (('Tp', 'Tp'), ('Sl', 'Sl'))
  result = models.CharField(max_length=10, choices=CHOICES, blank=True, null=True)

  be = models.BooleanField("be", default=False)

  Reason_For_be = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.Asset_Name
