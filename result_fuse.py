#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fuse_result

fuses the first and last results and show the discrimination diference

Created on Tue Oct 23 14:13:22 2018

@author: fernandotal
"""

import pandas as pd
# import numpy as np
import os
import etl_excel_files
import config


def main():
    """
    This is the main method
    """
    first_list = etl_excel_files.find_files(config.RESULTS_FOLDER, 'first.csv')
    last_list = etl_excel_files.find_files(config.RESULTS_FOLDER, 'last.csv')
    for index in range(len(first_list)):
        first_file = first_list[index]
        last_file = last_list[index]
        
        data_frame_first = pd.read_csv(first_file, index_col = 0)
        data_frame_last = pd.read_csv(last_file, index_col = 0)

        
        data_frame_first.columns = [i + '_first' for i
                                    in list(data_frame_first.columns)]
        data_frame_last.columns = [i + '_last' for i
                                   in list(data_frame_last.columns)]
        
        data_frame_final = pd.concat([data_frame_first, data_frame_last],
                                     axis =1)
        
        data_frame_final['discrimination_diference'] = (
                data_frame_final['discrimination_rate_last']
                - data_frame_final['discrimination_rate_first'])

        folder, file_name = os.path.split(first_file)
        folder = folder + '/'
        new_file_name = file_name[:-9] + 'final.xlsx'
        data_frame_final.to_excel(folder + new_file_name, index=True)
        
        #os.remove(first_list[index])
        #os.remove(last_list[index])


if __name__ == '__main__':
    main()
