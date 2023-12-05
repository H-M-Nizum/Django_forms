from django.db import models
from datetime import timedelta

# Create your models here.
class studentmodel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.TextField()
    father_nmae = models.CharField(max_length=20, default='father')
    
    # DateField: Store (year, month, and day)
    date_field = models.DateField(default='2023-11-11')
    
    # DateTimeField:
    date_time_field = models.DateTimeField(default='2023-11-11 12:30:30')
    
    # DecimalField: Stores decimal numbers
    decimal_field = models.DecimalField(default=123, max_digits=5, decimal_places=2)
    
    # DurationField: A field type used to store a duration of time
    duration_field = models.DurationField(default=timedelta)
    
    # EmailField: A field type used to store and validate email addresses.
    email_field = models.EmailField(default='aaa@gmail.com')
    
    # FloatField: Stores floating-point numbers.
    float_field = models.FloatField(default=23.34)
    
    
    # IntegerField: Stores integer values.
    integer_field = models.IntegerField(default=23)
    
    # PositiveBigIntegerField: Stores positive large integer values.
    positive_big_integer_field = models.PositiveBigIntegerField(default=1234556576577)
    
    # PositiveIntegerField: Stores positive integer values.
    positive_integer_field = models.PositiveIntegerField(default=34)
    
    # PositiveSmallIntegerField: Stores positive small integer values.
    positive_small_integer_field = models.PositiveSmallIntegerField(default=1)
    
    #SlugField:
    slug_field = models.SlugField(default='fsdfds')
    
    
    
    
    # SmallIntegerField: Stores small integer values.
    small_integer_field = models.SmallIntegerField(default=2)
    
    # TextField:
    text_field = models.TextField(default='i love bangladesh')
    
    # TimeField: 
    time_field = models.TimeField(default=' 11:11:11')
    
    
    # FileField: Represents a file upload.
    # file_field = models.FileField(upload_to='files/')
    
    # # FilePathField: Represents a file path on the file system.
    # file_path_field = models.FilePathField(path='/path/to/files/')
    
    # ImageField: Similar toFileField
    # image_field = models.ImageField(upload_to='images/')
    
    # GenericIPAddressField: Stores an IP address, either IPv4 or IPv6.
    # generic_ip_address_field = models.GenericIPAddressField()
    
     # JSONField: Stores JSON-encoded data
    # json_field = models.JSONField(default={})
    
    
    def __str__(self):
        return f"Roll - {self.roll} > Name - {self.name}"