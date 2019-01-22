from django.db import models

# Create your models here.

class Erds(models.Model):
    """
    From ERD Excel Table items:
    - erd_id
    - category
    - title
    - description
    - product_priority
    - author
    - version
    - platform

    From JIRA Ticket items:
    - l1_jira
    - l2_jira
    - bug_jiras
    - workload
    - milestone
    """

    erd_id = models.CharField(max_length=20)
    platform = models.CharField(max_length=20)
    category = models.CharField(max_length=40)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    product_priority = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    version = models.CharField(max_length=10)
    HLD = models.TextField()
    l1_jira = models.CharField(max_length=20)
    l2_jira = models.CharField(max_length=20)
    bug_jiras = models.TextField()
    status = models.CharField(max_length=10)
    workload = models.CharField(max_length=30)
    milestone = models.CharField(max_length=40)

    def __str__(self):
        display = "< ERD:" + self.erd_id + " platform:" + self.platform + " version:" + self.version + " >"
        return display

class TestCases(models.Model):
    """
    Get items from JIRA new-feature(L2-JIRA-Ticket) Ticket 'test/evidences field'.
    """

    case_name = models.CharField(max_length=50)
    case_age = models.CharField(max_length=20)
    F_report_path = models.TextField()

    erd = models.ForeignKey("Erds", on_delete=models.CASCADE)

    def __str__(self):
        display = "< CaseName:" + self.case_name + " erd_foreignKey:" + str(self.erd) + " >"
        return display


class TestReports(models.Model):
    """
    Get [test_result,fw_version,test_log] items from jenkins build result.
    """

    test_result = models.CharField(max_length=10)
    test_log = models.TextField()
    test_date = models.CharField(max_length=20)
    IR_report_path = models.TextField()
    fw_version = models.CharField(max_length=50)

    test_case = models.ForeignKey("TestCases", on_delete=models.CASCADE)

    def __str__(self):
        display = "< FW version:" + self.fw_version + " TestCase:" + str(self.test_case)+ " >"
        return display
