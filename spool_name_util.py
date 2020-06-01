import platform, os
from datetime import datetime
import time
import re
from spool_content_util import *

class Spool_Name_Util():
    def __init__(self, file):
        self.file = file
        self.content = None

    def make_filename(self):
        content_util = Spool_Content_Util(self.file)
        self.content = content_util.read_content(10)
        try:
            report_name = self.get_report_name()
        except:
            report_name = 'unknown'
        try:
            report_date = self.get_report_date()
        except:
            report_date = self.get_create_date()
        filename = report_name + '_' + report_date + '_' + self.file.split('/')[-1].split('.')[0]
        self.file, self.content = None, None
        return filename

    def get_report_name(self):
        report_name = self.content[2][:-1].strip()
        return report_name

    def get_report_date(self):
        report_date = self.content[0][:14].strip()
        tokens = ['-', '\.', '/']
        for token in tokens: report_date = re.sub(token, '_', report_date)
        return report_date

    def get_create_date(self):
        if platform.system() == 'Windows':
            create_date = os.path.getctime(self.file)
        else:
            stat = os.stat(self.file)
            try:
                create_date = stat.st_birthtime
            except AttributeError:
                create_date = stat.st_mtime
        create_date = datetime.strptime(time.ctime(create_date), '%a %b %d %H:%M:%S %Y').strftime('%Y_%m_%d')
        return create_date