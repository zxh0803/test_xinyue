# coding=utf-8
import xlrd

class Read_Excel():
    '''封装Excel的数据，生成列表'''
    def __init__(self,path,tableindex=0):
        self.data = xlrd.open_workbook(path)   #打开Excel
        self.table = self.data.sheet_by_index(tableindex)  #根据索引找table
        self.keys =self.table.row_values(0)    #获取Excel的第一行数据作为dict的key
        self.rows = self.table.nrows    #获取table的总行数
        self.cols = self.table.ncols    #获取table的总列数

    def dict_data(self):
        if self.rows <= 1:
            print "总行数小于1"
        else:
            r = []
            j = 1
            for i in range(self.rows-1):
                s = {}
                values = self.table.row_values(j)
                for x in range(self.cols):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r

if __name__ == '__main__':
    path = r"C:\Users\zxh\Desktop\loginuser.xlsx"
    tableindex = 0
    data = Read_Excel(path,tableindex)
    print data.dict_data()
