# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:16:08 2017

@author: jeeva
"""

import xlrd
import matplotlib.pyplot as plt
import numpy as np
import math

def airborne_mag():
    workbook = xlrd.open_workbook('2015MagProfile.xlsx', on_demand = True)
    worksheet = workbook.sheet_by_name('2015MagProfile02')

    location_val = [] ## location values: 100, 105, 110, ....
    mag_intensity = [] ## given total magnetic intensity at each point
    total_mag_val = [] ## array to store the T.M.I values after computing for airborne magnetic
    y_distance = 100 ## vertical distance o
    
    ## parse the excel values
    for i in range(1, 184):
        location_val.append(worksheet.cell(i, 0).value)
        mag_intensity.append(worksheet.cell(i, 1).value)
        #print(worksheet.cell(i, 0).value, worksheet.cell(i, 1).value)
    #print(location_val)
    
    ## compute the total magnetic intensity for each location
    for i in range(len(location_val)):
        
        total_mag_intensity = 0
        curr_mag_val = mag_intensity[i] - 53500
        
        for k in range(len(location_val)):
            
            x_distance = abs(location_val[i] - location_val[k])
            radius = ((x_distance ** 2) + (y_distance ** 2))**(1/2)
            theta = np.arctan(x_distance / y_distance)
            total_mag_intensity += (curr_mag_val / (radius ** 3)) * ((1 + (3 * ((np.cos(theta))**2)))**(1/2))
  
        total_mag_intensity += 53500
        print(location_val[i], total_mag_intensity)
        total_mag_val.append(total_mag_intensity)
        
        
        ##print(total_mag_intensity)

    #plt.plot(location_val, mag_intensity, '-')
    #print(sum(total_mag_val))
    plt.plot(location_val, total_mag_val, '-')
    plt.show()

    return 0

if __name__ == "__main__":
   airborne_mag()