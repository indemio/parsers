import pandas as pd


def pars(xls_file):
    raw_data = pd.read_excel(xls_file, sheet_name='Лист1')
    print(raw_data.head)

def main ():
    pars('C:/Temp/Z_1C_(02052018-06052018)/Z_1C_(01052018).xlsx')

main()