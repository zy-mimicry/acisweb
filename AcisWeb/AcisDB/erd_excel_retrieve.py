import xlrd
from AcisDB.models import Erds

# For "Requirements" sheet
erd_start_row = 1
c_Req_ID = 0
c_Requirement_Category = 1
c_Requirement_Title = 2
c_Description = 4
c_Project = 5
c_Product_Priority = 6
c_author = ''
c_Component = 7  # fw, legato, yocoto?

# For "Title & Revision" sheet
revision_table_column = 1


erd_to_colum_maps = {
    'category': c_Requirement_Category,
    'title': c_Requirement_Title,
    'description': c_Description,
    'product_priority': c_Product_Priority,
    'project': c_Project,
    'component': c_Component,
    'author': c_author
}

def retrieve_latest_erd_from_db(require_erd_id, product):
    erds = Erds.objects.filter(erd_id=require_erd_id, platform=product).order_by('version')
    if len(erds) >= 1:
        return erds[len(erds)-1]
    else:
        return False


def sheet_cell_value(table, row, column):
    if type(row) != int or type(column) != int:
        return ''
    else:
        return table.cell(row, column).value


def erd_values(platform, excel_table, row, version, erd_id):
    erd = {}
    excel_row_data = {}

    erd['PLATFORM'] = platform
    erd['ERD_ID'] = excel_row_data['erd_id'] = erd_id

    for key, value in erd_to_colum_maps.items():
        excel_row_data[key] = sheet_cell_value(excel_table, row, value)
    excel_row_data['version'] = version
    excel_row_data['platform'] = platform
    erd['excel'] = excel_row_data

    return erd


def erd_no_changed(db_latest_erd, table, row):
    description = table.cell(row, c_Description).value.replace(" ", "")
    no_changed = db_latest_erd and db_latest_erd.description == table.cell(row, c_Description).value
    erd_blank = (not db_latest_erd) and (description == '' or description == 'blank' or description == 'NA')
    if no_changed or erd_blank:
        return True
    else:
        return False


def read_excel(excel_file, platform, version):
    """
    For Excel Data:
    >>> [
    >>> ...
    >>> {
    >>>   "PLATFORM" : "",
    >>>   "ERD_ID" : "",
    >>>   "excel" : {
    >>>     'erd_id' : "",
    >>>     'category' : "",
    >>>     'title' : "",
    >>>     'description' : "",
    >>>     'product_priority' : "",
    >>>     'author' : "",
    >>>     'version' : "",
    >>>     'platform' : "",
    >>>     'project': "",
    >>>     'component': ""
    >>> }
    >>> ...
    >>> ]
    """
    all_erds = []
    data = xlrd.open_workbook('AcisDB/erd_release/' + excel_file)
    table = data.sheet_by_name(u'Requirements')

    # Check if the erd version matched.
    revision_table = data.sheet_by_name('Title & Revision')
    erd_revision_list = revision_table.col_values(revision_table_column)
    latest_version_index = erd_revision_list.index('BOTTOM_LINE: DO NOT DELETE')
    if erd_revision_list[latest_version_index - 1] != version:
        raise Exception('ERD version dismatch, expect version %s, actual version %s' % (version, erd_revision_list[latest_version_index - 1]))

    for i in range(erd_start_row, table.nrows):
        erd_id = table.cell(i, c_Req_ID).value.replace(' ', '')

        # if ERD_Req ID likes 02.38.01-02.38.29, we need to split it, and add erd_id from 02.38.01 to 02.38.29 into db
        interval_erd_id_list = erd_id.split('-')

        # read erd from ERD excel table
        # and check if this erd changed in this version, if no changed, no need to add to db again
        if len(interval_erd_id_list) == 1:
            db_latest_erd = retrieve_latest_erd_from_db(erd_id, platform)
            if erd_no_changed(db_latest_erd, table, i):
                continue
            else:
                all_erds.append(erd_values(platform, table, i, version, erd_id))
        elif len(interval_erd_id_list) == 2:
            erd_id_start = int(interval_erd_id_list[0].split('.')[-1])
            erd_id_end = int(interval_erd_id_list[1].split('.')[-1])
            for erd_id_minor_num in range(erd_id_start, erd_id_end+1):
                if erd_id_minor_num < 10:
                    erd_id_string = '.'.join(interval_erd_id_list[0].split('.')[:-1]) + ".0" + str(erd_id_minor_num)
                else:
                    erd_id_string = '.'.join(interval_erd_id_list[0].split('.')[:-1]) + "." + str(erd_id_minor_num)

                db_latest_erd = retrieve_latest_erd_from_db(erd_id_string, platform)
                if erd_no_changed(db_latest_erd, table, i):
                    continue
                else:
                    all_erds.append(erd_values(platform, table, i, version, erd_id_string))
        # in the Bottom line
        elif "BOTTOM_LINE" in table.row_values(i):
            break
        else:
            raise Exception('ERD release excel erd format error! column = %d' % i)
    return all_erds