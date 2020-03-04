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


class ProjectApplication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    requested_amount = models.IntegerField()

    def __str__(self):
        return self.project.name

    class Meta():
        ordering = ['-id']


class ProjectAssignment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client_id = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    date_assigned = models.DateTimeField(auto_now=True)
    date_completed = models.DateField(null=True)
    revoke = models.BooleanField(default=False)

    def __str__(self):
        return self.project.name + '| to' + self.user.username


class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    note = models.CharField(max_length=250)
    creatd_on = models.DateTimeField(auto_now=True)
    read = models.BooleanField(default=False)
    read_on = models.DateTimeField(null=True)
    link = models.CharField(max_length=250)

    def countunread(self):
        return self.objects.filter(read=False)
