from django.db import models

class Product(models.Model):
    
    list_cate = [
        ("phone","phone"),
        ("tab","tab"),
        
    ]
    
    name = models.CharField(max_length=50,verbose_name="Title")
    content = models.TextField(default="Add A Content", null=True, blank=True, verbose_name="Description")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="photos/%y/%m/%d")
    active = models.BooleanField(default = True)
    category = models.CharField(max_length=50, null=True, blank=True, choices=list_cate)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ' Product'
        ordering = ["name"]