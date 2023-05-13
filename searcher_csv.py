import pandas as pd

def csv_parse(name):
    file = pd.read_csv('prom.csv', sep=',')
    # reuslt = file[file['NAME']==name]
    # reuslt = file.loc[file['NAME']==name]
    # for i in reuslt:
    #     print (i)
    # return([reuslt])
    for i in file.itertuples():
        if i[1].find(name) !=-1:
            return list(i)
