#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
class_fuse

Use this script if you want to group test values together


Created on Tue Oct 23 11:30:05 2018

@author: fernandotal
"""

# TODO maybe merge with ETL_excel_files

import pandas as pd
import os
import etl_excel_files as etl
import config




def main():
    """
    This is the main method
    """
    # create the year path folders for manipulation
    
    # TODO Clear this big hack
    # TODO alternative, add a list of disciplines with fusing
    chumbado = './padronized/EAD0652' # Windows style?
    
    year_folder_list = [os.path.join(chumbado, x)
                        for x in os.listdir(chumbado)]
    
    # Find the files from the same year and exam
    for year_folder in year_folder_list:
        # list files of that year that are of the same type
        for file_type in config.JOIN_ACTIVITIES:
            file_end = file_type + '.csv'
            group_list = etl.find_files(year_folder, file_end)
            # Fuse classes
            dataframe_list = [pd.read_csv(_) for _ in group_list]
            all_dataframe = pd.concat(dataframe_list, ignore_index=True)
            # export to csv in the right folder
            directory =os.path.join(year_folder, 'all')
            os.makedirs(directory, exist_ok=True)
            file_dir = os.path.join(directory, file_end)
            all_dataframe.to_csv(file_dir, index=False)
            [os.remove(_) for _ in group_list]

if __name__ == '__main__':
    main()
