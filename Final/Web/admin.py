from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, QuoteRequest

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    
    filter_horizontal = ('groups', 'user_permissions') 

admin.site.register(CustomUser, CustomUserAdmin)

class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'project_type', 'location', 'budget', 'created_at')
    list_filter = ('project_type', 'location', 'created_at')
    search_fields = ('name', 'phone', 'location', 'details')

admin.site.register(QuoteRequest, QuoteRequestAdmin)
