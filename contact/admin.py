from django.contrib import admin
from .models import Contact, Membership

# Register your models here.

admin.site.register (Contact)

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname','father_name','gender','passport_number','passport_fin_number','born','place_of_birth','actual_residence','home_phone_number','phone_number','email','areas_of_activity','work_time','establishment', 'adress', 'facility_site','facility_phone_number','facility_mail','project','project_part','purpose','created_at', 'updated_at')
    list_filter = ('name', 'surname','father_name','gender','passport_number','passport_fin_number','born','place_of_birth','actual_residence','home_phone_number','phone_number','email','areas_of_activity','work_time','establishment', 'adress', 'facility_site','facility_phone_number','facility_mail','project','project_part','purpose','created_at', 'updated_at')
    search_fields = ('name', 'surname','father_name','gender','passport_number','passport_fin_number','born','place_of_birth','actual_residence','home_phone_number','phone_number','email','areas_of_activity','work_time','establishment', 'adress', 'facility_site','facility_phone_number','facility_mail','project','project_part','purpose','created_at', 'updated_at')
admin.site.register (Membership, MembershipAdmin)