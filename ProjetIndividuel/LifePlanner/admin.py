from django.contrib import admin
from .models import Project, Status, Task

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display   = ('name', )
    list_filter    = ('name', )
    search_fields  = ('name', 'members')


    #Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (name, members)
        ('General', {
            'classes': ['collapse', ],
            'fields': ('name','members')
        }),

    )


#Registration of the projects
admin.site.register(Project, ProjectAdmin)
admin.site.register(Status)
admin.site.register(Task)