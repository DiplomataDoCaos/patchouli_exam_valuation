#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
class_fuse

Use this script if you want to group multiple avaliations together

Created on Tue Oct 23 11:30:05 2018

@author: fernandotal
"""

# TODO maybe merge with ETL_excel_files

import pandas as pd
import numpy as np
import os


def main():
    """
    This is the main method
    """
    pass


if __name__ == '__main__':
    main()

    # Group selection

    # Group analisys
#    for group in group_list:
#        data_frame = pd.DataFrame()
#        for file_name in group_list:
#
#
#
#
#
#            data_frame = clean(data_frame, file_origin)
#            meta_dict = extract_name_info(file_name)
#            # TODO: Extract this function
#            directory = os.path.join(
#                    config.PADRONIZED_FOLDER,
#                    meta_dict['discipline'],
#                    all_classes,
#                    meta_dict['class'],
#                    '')
#            os.makedirs(directory, exist_ok=True)
#            file_dir = os.path.join(directory, meta_dict['name']+'.csv')
#            data_frame.to_csv(file_dir, index=True)
