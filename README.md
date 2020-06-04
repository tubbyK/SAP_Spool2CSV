# SAP_Spool2CSV
Tool to convert SAP spool txt files to csv by extracting report name, headers and data then writing to csv format.


[Overview] SAP GUI has a useful feature to write spools to local file directly. This lets us download reports in the background (step by step guide in HOW TO USE section) which is a lot less prone to interruptions as compared to opening spool and exporting as spreadsheet.

However, spool files downloaded this way is in a text format which is not easy to clean up by hand.

This utility script automates clean up of spool files, generates csv file and appends report name and date to filename.


[Example]
from SAP_Spool2CSV import *
S = Spool2CSV()
S.run()


[HOW TO Get Spool Txt Files]
1. Goto System > Own Spool Request (results from SQVI are placed here)
2. Select reports to download (tip: right click a spool and choose select all to check all)
3. Select Spool Request from top left > Forward > Export as Text
4. Choose directory and SAP GUI will immediately start writing to it. The SAP session (SAP window) that is exporting will become unresponsive as it writes.

As a parting note, in my experience many small files are more handy and writes faster than a big one.
