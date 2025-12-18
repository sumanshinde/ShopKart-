from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User , Shipping_Address

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display=["email","first_name","last_name","contact_number","is_staff","is_active","date_joined"]

    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "contact_number")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "contact_number", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )

    search_fields = ("email", "first_name", "last_name")  # ✅ no "username"

    readonly_fields = ("date_joined", "last_login")
    
    
@admin.register(Shipping_Address)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "address_line1", "landmark", "city", "state", "pincode")
 

admin.site.register(User,UserAdmin)