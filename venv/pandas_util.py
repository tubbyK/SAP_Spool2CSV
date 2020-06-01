from datetime import datetime
import pandas as pd
import glob, os
from tkinter import Tk, filedialog
import ctypes

def display_settings():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

# append name of data source to columns
def rename_cols(df, name):
    old_cols = df.columns.to_list()
    new_cols = [name + '.' + col for col in old_cols]
    df_cols = dict(zip(old_cols, new_cols))
    df.rename(columns=df_cols, inplace=True)

def count_occurances(df, col_to_count):
    df_value_counts = pd.Series(df[col_to_count].values.ravel()).dropna().value_counts()
    return df_value_counts

def search(df, column, value):
    df_result = df[df[column]==value]
    return df_result

# fillna according to dtype 
def fillna_by_dtype(df, col):
    # check dtype
    na_value = None
    if pd.api.types.is_numeric_dtype(df[col]):
        na_value = 0
    elif pd.api.types.is_string_dtype(df[col]):
        na_value = ''
    else:
        # date
        na_value = datetime(year=1990, month=1, day=1)
    df[col].fillna(na_value, inplace=True)
    return df

def get_filenames():
    user32 = ctypes.windll.user32
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    geometry_str = f'1x1+{int(width/5)}+{int(height/5)}'
    root = Tk()
    root.geometry(geometry_str)
    root.call('wm', 'attributes', '.', '-topmost', True)
    files = filedialog.askopenfilenames() # show an "Open" dialog box and return the path to the selected file
    root.destroy()
    return files

def load_df(files=None, usecols=None, parse_dates=None, encoding=None, delimiter=None):
    if files is None: files = get_filenames()
    df_ = [pd.read_csv(file, usecols=usecols, parse_dates=parse_dates,
                       encoding=encoding, delimiter=delimiter, low_memory=False,) 
                         for file in files]
    return pd.concat(df_, ignore_index=True)

def get_folder():
    root = Tk()
    root.withdraw()
    fld = filedialog.askdirectory()
    return fld

def load_folder(fld=None, usecols=None, parse_dates=None, encoding=None, delimiter=None):
    if fld is None:
        fld = get_folder()
        files = glob.glob(os.path.join(fld, "*.csv"))
    df_ = [pd.read_csv(file, usecols=usecols, parse_dates=parse_dates,
                       encoding=encoding, delimiter=delimiter, low_memory=False,) 
                         for file in files]
    return pd.concat(df_, ignore_index=True)