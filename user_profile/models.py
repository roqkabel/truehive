from django.db import models
from django.conf import settings
# Create your models here.

SKILLS_CHOICE = (
    ('WD', 'Web Development'),
    ('GD', 'Graphic Development'),
    ('MA', 'Mobile App Development'),
    ('DM', 'Digital Marketing'),
    ('CW', 'Copy Writing'),
    ('SM', 'Social Media Management')
)
ACCOUNT_TYPE = (
    ('FL', 'Freelancer'),
    ('CL', 'Client'),
)
REGION_CHOICE = (
    ('GA', 'Greater Accra'),
    ('AR', 'Ashanti Region'),
    ('ER', 'Eastern Region'),
    ('VR', 'Volta Region'),
    ('NR', 'Northern Region'),
)

EXPERIENCE = (
    ('BG', 'Beginner'),
    ('IT', 'Intermmediate'),
    ('AD', 'Advanced'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    # user = models.ForeignKey()
    profile_completed = models.BooleanField(default=False)
    account_type = models.CharField(choices=ACCOUNT_TYPE, max_length=2)
    mobile = models.IntegerField(default=0)
    skills = models.CharField(choices=SKILLS_CHOICE, max_length=2)
    about = models.TextField()
    region = models.CharField(choices=REGION_CHOICE, max_length=2)
    experience = models.CharField(choices=EXPERIENCE, max_length=2)
    profile_image = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.user.username
