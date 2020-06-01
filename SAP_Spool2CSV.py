import pandas_util as pdu
from spool_content_util import *
from spool_name_util import *

class Spool2CSV():
    def __init__(self, out_fld=None):
        self.out_fld = pdu.get_folder() if out_fld is None else out_fld

    def run(self):
        # select files and read contents
        self.files = pdu.get_filenames()
        for file in self.files:
            name_util = Spool_Name_Util(file)
            filename = name_util.make_filename()
            content_util = Spool_Content_Util(file)
            content = content_util.process_content()
            self.write_file(content, filename)

    def write_file(self, content, filename):
        filepath = self.out_fld + r'\\' + filename + '.csv'
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(content)
        except:
            with open(filepath, 'w', encoding='latin-1') as f:
                f.writelines(content)

if __name__ == '__main__':
    S = SAP_Spool_Util()
    S.run()