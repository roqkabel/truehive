from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, ProjectApplication, ProjectAssignment, Notification
from .forms import EditProjectModelForm, ProjectApplicationModelForm, FreelanceAccountFormModel, ClientAccountFormModel
from django.conf import settings
from django.contrib.auth.models import User
import datetime
# Create your views here.


def index(request):

    if request.user.userprofile.account_type == 'FL':
        assignments = ProjectAssignment.objects.filter(
            user=request.user).order_by('-id')
    else:
        assignments = ProjectAssignment.objects.filter(
            client_id=request.user.id).order_by('-id')

    context = {
        'project_assignment': assignments
    }
    return render(request, 'dashboard/index.html', context)


def projects_view(request):
    projects = Project.objects.filter(user=request.user)
    context = {
        'projects': projects
    }

    if request.user.userprofile.account_type == 'FL':
        projects = Project.objects.filter(
            category=request.user.userprofile.skills)
        context = {
            'projects': projects
        }
        return render(request, 'dashboard/f_projects.html', context)
    else:
        return render(request, 'dashboard/projects.html', context)


def project_bids(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    bids = ProjectApplication.objects.filter(project=project)
    assignment = ProjectApplication.objects.filter(project=project)
    context = {
        'assignment': assignment,
        'bids': bids,
        'project': project
    }
    return render(request, 'dashboard/bids.html', context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectApplicationModelForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.project = project
            instance.user = request.user
            instance.save()

            """
            NOTIFICATION TO USER
            ---------------------------------------
            eg. Obed sent to bid to your project view.
            """

            message = request.user.username + ' just sent a bid to your project'
            notification = Notification(
                user=project.user,
                note=message,
                read=False,
                link='/dashboard/projects/' + str(project_id) + '/bids/',
            )
            notification.save()

    else:
        form = ProjectApplicationModelForm()

    form = ProjectApplicationModelForm()

    context = {
        'form': form,
        'project': project
    }
    return render(request, 'dashboard/project_detail.html', context)


def projects_create_view(request):

    form = EditProjectModelForm()

    if request.method == 'POST':
        form = EditProjectModelForm(
            request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/dashboard/projects/')
        else:
            form = EditProjectModelForm()

    context = {
        'form': form,
    }
    return render(request, 'dashboard/project_add.html', context)


def project_edit(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = EditProjectModelForm(instance=project)

    if request.method == 'POST':
        form = EditProjectModelForm(
            request.POST, request.FILES, instance=project)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        else:
            form = EditProjectModelForm(instance=project)

    context = {
        'form': form,
        'project': project
    }
    return render(request, 'dashboard/project_edit.html', context)


def project_delete(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return redirect('/dashboard/projects/')

# ACCOUNT VIEWS


def account_edit_view(request):

    if request.user.userprofile.account_type == 'FL':

        form = FreelanceAccountFormModel(instance=request.user.userprofile)

        if request.method == 'POST':
            form = FreelanceAccountFormModel(
                request.POST, request.FILES, instance=request.user.userprofile)
            if form.is_valid():
                form.save()
            else:
                form = FreelanceAccountFormModel(
                    instance=request.user.userprofile)

        context = {
            'form': form,
        }
        return render(request, 'dashboard/f_account.html', context)
    else:
        form = ClientAccountFormModel(instance=request.user.userprofile)

        if request.method == 'POST':
            form = ClientAccountFormModel(
                request.POST, request.FILES, instance=request.user.userprofile)
            if form.is_valid():
                form.save()
        else:
            form = ClientAccountFormModel(
                instance=request.user.userprofile)

        context = {
            'form': form,
        }
        return render(request, 'dashboard/c_account.html', context)


# NOTIFICATION VIEWS


def notifications_view(request):
    notifications = Notification.objects.filter(
        user=request.user).order_by('-id')
    context = {
        'notifications': notifications
    }
    return render(request, 'dashboard/notifications.html', context)


def notification_refs(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    try:
        notification.read = True
        notification.read_on = datetime.datetime.now()
        notification.save()
    finally:
        return redirect(notification.link)

# APPLICATION HANDLERS


def project_assignment(request, project_id, user_id):
    project = get_object_or_404(Project, pk=project_id)
    freelancer = get_object_or_404(User, pk=user_id)

    assignment = ProjectAssignment(
        user=freelancer,
        client_id=request.user.id,
        project=project,
    )

    try:
        assignment.save()
        """ 
             NOTIFICATION TO USER
             ---------------------------------------
             notion: redirect user to dashboard
             """

        message = ' You just got assigned to a project '
        notification = Notification(
            user=freelancer,
            note=message,
            read=False,
            link='/dashboard/projects/%d/' % project_id,
        )
        notification.save()
    finally:
        return redirect('/dashboard/projects/%d/bids/' % project_id)


#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     client_id = models.IntegerField()
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     date_assigned = models.DateTimeField(auto_now=True)
#     date_completed = models.DateField(default=None)
#     revoke = models.BooleanField(default=False)
