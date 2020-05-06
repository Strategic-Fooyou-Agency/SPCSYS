from django.db import models

# Create your models here.


class Product(models.Model):
    bin_name = models.CharField(max_length=20)
    exproduct_name = models.CharField(max_length=15)
    inproduct_name = models.CharField(max_length=15)
    bin_no = models.SmallIntegerField()
    spec_name = models.CharField(max_length=7)
    wld1_max = models.DecimalField(max_digits=4, decimal_places=1)
    wld1_min = models.DecimalField(max_digits=4, decimal_places=1)
    lop1_max = models.SmallIntegerField()
    lop1_min = models.SmallIntegerField()
    vf1_max = models.DecimalField(max_digits=3, decimal_places=2)
    vf1_min = models.DecimalField(max_digits=3, decimal_places=2)
    code = models.CharField(max_length=2)
    vfspec = models.CharField(max_length=3)
    ivspec = models.CharField(max_length=3)
    wdspec = models.CharField(max_length=3)
    prod_no = models.CharField(max_length=3)
    grade = models.CharField(max_length=1)
    process_code = models.CharField(max_length=3)
    lop1_avgmin = models.SmallIntegerField(null=True, blank=True)
    lop1_avgmax = models.SmallIntegerField(null=True, blank=True)
