from django.contrib import admin
from .models import Erds,TestCases,TestReports,TestCampaign,ProjectSnapshot

# Register your models here.
# admin.site.register(Erds)
# admin.site.register(TestCases)
# admin.site.register(TestReports)

from reversion.admin import VersionAdmin

@admin.register(Erds)
class ErdsModelAdmin(VersionAdmin):
    pass

@admin.register(TestCases)
class TestCasesModelAdmin(VersionAdmin):
    pass

@admin.register(TestReports)
class TestReportsModelAdmin(VersionAdmin):
    pass

@admin.register(TestCampaign)
class TestReportsModelAdmin(VersionAdmin):
    pass

@admin.register(ProjectSnapshot)
class TestReportsModelAdmin(VersionAdmin):
    pass
