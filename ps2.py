import xlrd
import matplotlib.pyplot as plt
import numpy as np
import math


def readExcelData():
    workbook = xlrd.open_workbook('Bosumtwi_res_logs.xls', on_demand = True)
    worksheet = workbook.sheet_by_name('BCDP_O8A_COMP')

    depth = [] ## depth values
    rs_values = [] 
    rd_values = []     
    
    ## parse the excel values
    for i in range(38, 3912):
        depth.append(worksheet.cell(i, 0).value)
        rs_values.append(worksheet.cell(i, 1).value)
        rd_values.append(worksheet.cell(i, 2).value)
        #print(worksheet.cell(i, 0).value, worksheet.cell(i, 1).value, worksheet.cell(i, 2).value)

    
    plt.plot(depth, rs_values)
    plt.ylim([-20, 150])
    plt.xlim([210, 460])
    plt.show()
    
def solveAB():

    y = np.array([math.log(5), math.log(20), math.log(45), math.log(250), math.log(900), math.log(3000)])

    x = np.array([1, 5, 10, 22, 27, 32])

    A = np.vstack([x, np.ones(len(x))]).T

    b, a = np.linalg.lstsq(A, y)[0]

    print("A: ", a, "| B: ", b)

if __name__ == "__main__":
    readExcelData()
