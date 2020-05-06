"""LifeManager Admin Configuration

The `****Admin` classes are used to personalize the view of the Administration page for the model ***
Examples:
    1. list_filter:  add a filter for the specified field of the model

"""


from django.contrib import admin
#Truncator for the function apercu_entry
from django.utils.text import Truncator
from .models import Project, Status, Task, Journal



#Personalisation of the rendering of project models in administration page
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'members')

    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (name, members)
        ('General', {
            'classes': ['collapse', ],
            'fields': ('name', 'members')
        }),

    )

#Personalisation of the rendering of journals models in administration page
class JournalAdmin(admin.ModelAdmin):
    list_display = ('author', 'date', 'task', 'apercu_entry')
    list_filter = ('author', 'task',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('entry', 'author', 'task')
#The content of the entry of the journal is truncated for brevity's sake
    def apercu_entry(self, journal):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.
        """
        return Truncator(journal.entry).chars(40, truncate='...')


# Registration of the projects
admin.site.register(Project, ProjectAdmin)
admin.site.register(Status)
admin.site.register(Task)
admin.site.register(Journal, JournalAdmin)
