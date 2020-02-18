from django.shortcuts import render, redirect, get_object_or_404
from .forms import FreelancerForm, ClientForm
from .models import UserProfile
from django.conf import settings
# Create your views here.


# profile_completed = models.BooleanField(default=False)
#     account_type = models.CharField(choices=ACCOUNT_TYPE, max_length=2)
#     mobile = models.IntegerField()
#     skills = models.CharField(choices=SKILLS_CHOICE, max_length=2)
#     about = models.TextField()
#     region = models.CharField(choices=REGION_CHOICE, max_length=2)
#     experience = models.CharField(choices=EXPERIENCE, max_length=2)
#     profile_image = models.ImageField(upload_to='profiles/')

def index(request):
    context = {}
    if request.method == 'POST':
        if request.POST['account'] == 'freelance':
            user = UserProfile(
                user=request.user,
                account_type='FL'
            )
            user.save()
            request.session['account_type'] = 'freelance'
            return redirect('/profile/?account_type=freelancer/')

        elif request.POST['account'] == 'client':
            user = UserProfile(
                user=request.user,
                account_type='CL'
            )
            user.save()
            request.session['account_type'] = 'client'
            return redirect('/profile/?account_type=client/')
        else:
            context = {
                'error_message': 'Please choose an account type'
            }
    return render(request, 'user_profile/index.html', context)


def freelancer_page(request):
    user = get_object_or_404(UserProfile, user=request.user)

    return render(request, 'user_profile/freelancer.html', context={'form': FreelancerForm})


def client_page(request):
    return render(request, 'user_profile/client.html', context={'form': ClientForm})
