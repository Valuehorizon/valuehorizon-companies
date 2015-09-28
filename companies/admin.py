from django.contrib import admin
from datetime import *
from companies.models import Sector, IndustryGroup, Industry, SubIndustry
from companies.models import Company, Ownership, Director, Executive, CompanyNameChange




class SectorAdmin(admin.ModelAdmin): 
    search_fields=["name",]
    list_display = ('name', 'symbol', 'custom')
admin.site.register(Sector, SectorAdmin)

class IndustryGroupAdmin(admin.ModelAdmin): 
    search_fields=["name",]
    list_display = ('name', 'symbol', 'sector', 'custom')
admin.site.register(IndustryGroup, IndustryGroupAdmin)

class IndustryAdmin(admin.ModelAdmin): 
    search_fields=["name",]
    list_display = ('name', 'symbol', 'industry_group', 'sector', 'custom')
admin.site.register(Industry, IndustryAdmin)

class SubIndustryAdmin(admin.ModelAdmin): 
    search_fields=["name",]
    list_display = ('name', 'symbol', 'industry', 'custom')
admin.site.register(SubIndustry, SubIndustryAdmin)

class CompanyNameChangeAdmin(admin.ModelAdmin): 
    search_fields=["company__name", "name_before", "name_after"]
    list_display = ('company', 'date', 'name_before', 'name_after')
    list_filter=['date']
admin.site.register(CompanyNameChange, CompanyNameChangeAdmin)

class CompanyAdmin(admin.ModelAdmin): 
    search_fields=["name",]
    prepopulated_fields = { 'slug_name': ['name'] }
    list_filter=['country', 'is_auditor']
    list_display = ('name', 'country', 'company_type', 'sub_industry')
admin.site.register(Company, CompanyAdmin)

class OwnershipAdmin(admin.ModelAdmin): 
    search_fields=["name",]
admin.site.register(Ownership, OwnershipAdmin)



# People
class DirectorAdmin(admin.ModelAdmin): 
    search_fields=["company__name", "person__first_name", "person__last_name", "person__other_names"]
admin.site.register(Director, DirectorAdmin)
class ExecutiveAdmin(admin.ModelAdmin): 
    search_fields=["company__name", "person__first_name", "person__last_name", "person__other_names"]
admin.site.register(Executive, ExecutiveAdmin)
class DirectorInline(admin.TabularInline):
    model = Director
class ExecutivesInline(admin.TabularInline):
    model = Executive
