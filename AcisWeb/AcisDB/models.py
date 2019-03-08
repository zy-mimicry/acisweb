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
    - component
    - project
    """

    erd_id = models.CharField(max_length=20)
    platform = models.CharField(max_length=20)
    category = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    product_priority = models.CharField(max_length=20, null=True)
    author = models.CharField(max_length=20, null=True)
    version = models.CharField(max_length=10)
    HLD = models.TextField(null=True)
    l1_jira = models.CharField(max_length=20, null=True)
    l2_jira = models.CharField(max_length=20, null=True)
    bug_jiras = models.TextField(null=True)
    status = models.CharField(max_length=10, null=True)
    workload = models.CharField(max_length=30, null=True)
    milestone = models.CharField(max_length=40, null=True)
    component = models.CharField(max_length=30, null=True)
    project = models.CharField(max_length=40, null=True)

    def __str__(self):
        display = "< ERD:" + self.erd_id + " platform:" + self.platform + " version:" + self.version + " >"
        return display

class TestCases(models.Model):
    """
    Get items from JIRA new-feature(L2-JIRA-Ticket) Ticket 'test/evidences field'.
    """

    case_name = models.CharField(max_length=50)
    case_age = models.CharField(max_length=20)
    delete_status = models.NullBooleanField()
    F_report_path = models.TextField(null=True)

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
    note = models.TextField(null=True)
    description = models.CharField(max_length=100)  # test_type

    test_case = models.ForeignKey("TestCases", on_delete=models.CASCADE)

    def __str__(self):
        display = "< " + self.fw_version + "_" + self.description + "_" + self.test_date + "_" +  "TestCase_" + str(self.test_case) + " >"
        return display

class TestCampaign(models.Model):
    """
    Each Test triggered by Jenkins server should be a unified form.
    NOTE: This form is used as a jump table and is not associated with other forms.
    """

    platform    = models.CharField(max_length=20)
    fw_version  = models.CharField(max_length=50)
    description = models.TextField()
    test_date   = models.CharField(max_length=30)

    def __str__(self):
        display = "< {}_{}_{} >".format(self.fw_version, self.description, self.test_date)
        return display

class ProjectSnapshot(models.Model):
    """
    Snapshot
    """

    platform = models.CharField(max_length=20)
    date = models.CharField(max_length=30)
    snap = models.BinaryField()
    tag  = models.TextField()

    def __str__(self):
        display = "< {}_{}_{} >".format(self.platform, self.date, self.tag)
        return display

class SlaveStaticInfo(models.Model):
    """
    ACIS Slave node static information that be added manually.
    """
    img_version = models.CharField(max_length=20)
    birthday = models.CharField(max_length=20)
    hostname = models.CharField(max_length=40) # same as node name
    mac_addr = models.CharField(max_length=45)
    remove_status = models.BooleanField()
    dead_date = models.CharField(max_length=25, null=True, blank=True)
    owner = models.CharField(max_length=30)

    def __str__(self):
        display = "< {}_{}_{} >".format(self.hostname, self.img_version, self.owner)
        return display

class DutStaticInfo(models.Model):
    """
    ACIS DUT static information that be added manually.
    """
    usb_ser = models.CharField(max_length=20)
    birthday = models.CharField(max_length=20)
    FSN = models.CharField(max_length=20)
    remove_status = models.BooleanField()
    dead_date = models.CharField(max_length=25, null=True, blank=True)
    slave_mac_addr = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)

    def __str__(self):
        display = "< {}_{}_{}_{} >".format(self.FSN, self.usb_ser, self.slave_mac_addr, self.owner)
        return display

class TestHistory(models.Model):
    """
    ACIS Slave-Node Test History.
    """
    test_date_on_pi = models.CharField(max_length=20)
    hostname = models.CharField(max_length=20)
    slave_mac_addr = models.CharField(max_length=20)
    FSN = models.CharField(max_length=20)
    case_name = models.CharField(max_length=20)
    test_result = models.CharField(max_length=20)

    # mapto TestCampaign item
    test_campaign = models.OneToOneField(TestCampaign, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        display = "< {}: {}/{}/{} >"\
                  "".format(self.test_date_on_pi, self.FSN, self.hostname, self.slave_mac_addr)
        return display
