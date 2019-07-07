from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Ceo, Score
from .views import UserCreationForm, ScoreForm


# Register your models here.
class MyUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff')
    list_display_links = ('id', 'username')
    ordering = ['id']

    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'password1', 'password2', 'groups')}
        ),
    )

class ScoreAdmin(admin.ModelAdmin):
    model = Score
    extra = 10
    list_display = ('myuser', 'ceo')
    list_display_links = ['ceo']
    ordering = ['id']

    add_form = ScoreForm
    add_fieldsets = (
        (None, {
            'score-fields': ('score_0','score_1','score_3','score_4','score_5','score_6','score_7','score_8','comment'),
            'date' : ('create_date','updated_date'),}
        ),
    )


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Ceo)
admin.site.register(Score, ScoreAdmin)
