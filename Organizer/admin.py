from django.contrib import admin

import models

# Register your models here.
class DashboardAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Dashboard, DashboardAdmin)
class DashboardPanelAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.DashboardPanel, DashboardPanelAdmin)
