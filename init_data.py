import os
os.environ["DJANGO_SETTINGS_MODULE"] = "TimeManagement.settings"

from django.conf import settings
from django.contrib.auth.models import User

from Organizer import models as organizer_models
from Overhead import models as overhead_models

# Create various user types
overhead_models.UserType(name='Administrator', system_name='admin').save()
overhead_models.UserType(name='User', system_name='normal').save()
overhead_models.UserType(name='Project Manager', system_name='pm').save()

# Create user for John Doe
user = User.objects.create_user('user',
                                'user@gmail.com',
                                'password')
user.first_name = 'John'
user.last_name = 'Doe'
user.save()
user_profile = overhead_models.UserProfile()
user_profile.user = user
user_profile.name = 'John'
user_profile.type = overhead_models.UserType.objects.filter(system_name='admin').first()
user_profile.save()

organizer_models.ProjectPriority(name='Eventually', sort_order=0).save()
back_burner_priority = organizer_models.ProjectPriority(name='Back Burner', sort_order=1)
back_burner_priority.save()
organizer_models.ProjectPriority(name='Low Priority', sort_order=2).save()
normal_priority = organizer_models.ProjectPriority(name='Normal Priority', sort_order=3)
normal_priority.save()
organizer_models.ProjectPriority(name='Elevated Priority', sort_order=4).save()
organizer_models.ProjectPriority(name='Past Due', sort_order=5).save()
organizer_models.ProjectPriority(name='Lingering', sort_order=6).save()

organizer_models.TaskSeverity(name='Eventually', sort_order=0).save()
organizer_models.TaskSeverity(name='Back Burner', sort_order=1).save()
low_severity = organizer_models.TaskSeverity(name='Low Priority', sort_order=2)
low_severity.save()
normal_severity = organizer_models.TaskSeverity(name='Standard', sort_order=3)
normal_severity.save()
organizer_models.TaskSeverity(name='Elevated Priority', sort_order=4).save()
organizer_models.TaskSeverity(name='PMs are Angry', sort_order=5).save()
organizer_models.TaskSeverity(name='Gating', sort_order=6).save()
organizer_models.TaskSeverity(name='Client is Angry', sort_order=7).save()

default_client = organizer_models.Client()
default_client.name = 'Default'
default_client.abbreviation = 'default'
default_client.save()
cmpny_client = organizer_models.Client()
cmpny_client.name = 'Company'
cmpny_client.abbreviation = 'cmpny'
cmpny_client.save()

default_project = organizer_models.Project()
default_project.name='Default'
default_project.client=default_client
default_project.priority=normal_priority
default_project.save()
internal_project = organizer_models.Project(name='Internal Toolset', client=cmpny_client, priority=back_burner_priority)
internal_project.save()

task = organizer_models.Task()
task.title = 'Answer Email'
task.project = default_project
task.severity = normal_severity
task.user = user
task.save()
task = organizer_models.Task()
task.title = 'Script Configurable Options'
task.project = internal_project
task.severity = low_severity
task.user = user
task.save()

dashboard = organizer_models.Dashboard(user_id=None)
dashboard.save()
organizer_models.DashboardPanel(dashboard=dashboard, type='CreateTaskPanel', sort_order=10).save()
organizer_models.DashboardPanel(dashboard=dashboard, type='AllTasksPanel', sort_order=20).save()
