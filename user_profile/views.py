from django.shortcuts import render, redirect, get_object_or_404
from .forms import FreelancerForm, ClientForm
from .models import UserProfile
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

# from django.
# profile_completed = models.BooleanField(default=False)
#     account_type = models.CharField(choices=ACCOUNT_TYPE, max_length=2)
#     mobile = models.IntegerField()
#     skills = models.CharField(choices=SKILLS_CHOICE, max_length=2)
#     about = models.TextField()
#     region = models.CharField(choices=REGION_CHOICE, max_length=2)
#     experience = models.CharField(choices=EXPERIENCE, max_length=2)
#     profile_image = models.ImageField(upload_to='profiles/')


@login_required
def index(request):

    context = {}
    try:
        user = UserProfile.objects.get(user=request.user)
        if user.profile_completed:
            if user.account_type == 'FL':
                request.session['account_type'] = 'freelance'

            if user.account_type == 'CL':
                request.session['account_type'] = 'client'

            return redirect('/dashboard/')
    except UserProfile.DoesNotExist:
        pass

    if request.method == 'POST':
        if request.POST['account'] == 'freelance':
            user = UserProfile(
                user=request.user,
                account_type='FL'
            )
            user.save()
            request.session['account_type'] = 'freelance'
            return redirect('/profile/freelancer/')

        elif request.POST['account'] == 'client':
            user = UserProfile(
                user=request.user,
                account_type='CL'
            )
            user.save()
            request.session['account_type'] = 'client'
            return redirect('/profile/client/')
        else:
            context = {
                'error_message': 'Please choose an account type'
            }
    return render(request, 'user_profile/index.html', context)

# user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     profile_completed = models.BooleanField(default=False)
#     account_type = models.CharField(choices=ACCOUNT_TYPE, max_length=2)
#     mobile = models.IntegerField(default=0)
#     skills = models.CharField(choices=SKILLS_CHOICE, max_length=2)
#     about = models.TextField()
#     region = models.CharField(choices=REGION_CHOICE, max_length=2)
#     experience = models.CharField(choices=EXPERIENCE, max_length=2)
#     profile_image = models.ImageField(upload_to='profiles/')


def freelancer_page(request):
    user = UserProfile.objects.get(user=request.user)

    if user.profile_completed:
        if user.account_type == 'FL':
            request.session['account_type'] = 'freelance'

        if user.account_type == 'CL':
            request.session['account_type'] = 'client'

        return redirect('/dashboard/')

    if request.method == 'POST':
        form = FreelancerForm(
            request.POST, request.FILES, instance=user)
        if form.is_valid():
            # data = request.POST.copy()
            # user.about = data.get('about')
            # user.mobile = data.get('mobile')
            # user.skills = data.get('skills')
            # user.region = data.get('region')
            # user.experience = data.get('experience')
            # # user.profile_image = data.
            # user.profile_completed = True
            instance = form.save(commit=False)
            instance.user = request.user
            instance.profile_completed = True
            instance.save()
            return redirect('/dashboard/')
    else:
        form = FreelancerForm()

    return render(request, 'user_profile/freelancer.html', context={'form': form})


def client_page(request):
    user = UserProfile.objects.get(user=request.user)
    if user.profile_completed:
        if user.account_type == 'FL':
            request.session['account_type'] = 'freelance'

        if user.account_type == 'CL':
            request.session['account_type'] = 'client'

        return redirect('/dashboard/')
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.profile_completed = True
            instance.save()
            return redirect('/dashboard/')
    else:
        form = ClientForm()

    return render(request, 'user_profile/client.html', context={'form': form})
