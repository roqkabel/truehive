from django.db import models
from django.conf import settings
# Create your models here.

SKILLS_CHOICE = (
    ('WD', 'Web Development'),
    ('GD', 'Graphic Design'),
    ('MA', 'Mobile App Development'),
    ('DM', 'Digital Marketing'),
    ('CW', 'Copy Writing'),
    ('SM', 'Social Media Management')
)

PAYMENT_METHOD = (
    ('MM', 'Mobile Money'),
    ('CD', 'Bank / Credit Card')
)


class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    about = models.TextField()
    category = models.CharField(choices=SKILLS_CHOICE, max_length=2)
    duration = models.DateField()
    date_posted = models.DateTimeField(auto_now=True)
    price_range = models.IntegerField()
    photo = models.ImageField(upload_to='projects/')
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=2)

    def __str__(self):
        return self.name

    class Meta():
        ordering = ['-id']
