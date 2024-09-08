from django.contrib import admin
from .models import Enquiry, Equipment, Plan, Member

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'emailid', 'age', 'gender')
    search_fields = ('name', 'emailid', 'contact')
    list_filter = ('gender',)

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'unit', 'date', 'description')
    search_fields = ('name', 'description')
    list_filter = ('date',)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'duration')
    search_fields = ('name', 'amount')
    list_filter = ('duration',)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'emailid', 'age', 'gender', 'plan', 'joindate', 'expiredate', 'initialamount')
    search_fields = ('name', 'emailid', 'contact')
    list_filter = ('plan', 'joindate', 'expiredate')
    date_hierarchy = 'joindate'
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'contact', 'emailid', 'age', 'gender')
        }),
        ('Membership Details', {
            'fields': ('plan', 'joindate', 'expiredate', 'initialamount')
        }),
    )
admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Member, MemberAdmin)
