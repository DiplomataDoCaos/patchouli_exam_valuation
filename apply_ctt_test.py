#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply ctt test

Created on Sun Oct 21 17:46:54 2018

@author: fernandotal

Objective: Apply the Central Theory of Testes - CTT
(Teoria Central dos Testes - TCT in portuguese)
"""

import pandas as pd
import os
import etl_excel_files as etl
import config
import math


def group_measure(data_frame, percentile):
    """
    Determines the extreme size of the top and botton groups

    Recieves:
    - Data_frame for measure
    - Percentile of gathering (float)
    Returns
    - number of entries
    Obs: the number of entries is rounded up
    """
    lenght = len(data_frame)
    group_size = math.ceil(lenght * percentile)

    return(group_size)


def select_groups(data_frame, selection_size):
    """
    Selects the upper and lower_groups from a exam
    """

    upper_group = data_frame.iloc[0:selection_size].copy()
    lower_group = data_frame.iloc[-selection_size:].copy()

    return(upper_group, lower_group)


def main():
    """
    Main method: Check top docstring
    """
    file_path_list = etl.find_files(config.PADRONIZED_FOLDER, '.csv')
    for file_path in file_path_list:
        meta_dict = {}
        folder_path, temp = os.path.split(file_path)
        meta_dict['name'], meta_dict['selection'] = temp.split('-')
        meta_dict['selection'] = meta_dict['selection'][:-4]
        # TODO the rest with split
        folder_path, meta_dict['class'] = os.path.split(folder_path)
        folder_path, meta_dict['year'] = os.path.split(folder_path)
        folder_path, meta_dict['discipline'] = os.path.split(folder_path)

        data_frame = pd.read_csv(file_path) # TODO check encoding
        data_frame = data_frame.sort_values(data_frame.columns[0])

        group_size = group_measure(data_frame, config.PERCENTILE)

        upper_group, lower_group = select_groups(data_frame, group_size)
        
        discrimination_rate = upper_group.mean()/lower_group.mean()

        # discrimination_rate = discrimination_rate.rename(
        #       meta_dict['selection'])
        # TODO Needs to save the value, it's not working
        # Don't be too confident yet, needs to use the right groups yet

        discrimination_rate = discrimination_rate.apply("{0:.2f}".format)
        discrimination_rate = discrimination_rate.apply(float)
        # TODO check if this truncates or rounds the number

        data_frame_result = pd.concat([
                upper_group.mean(),
                lower_group.mean(),
                discrimination_rate],
                axis=1)
        data_frame_result.columns = ['upper_group_difficulty',
                          'lower_group_mean',
                          'discrimination_rate']

        # TODO classify questions difficulty

        directory = os.path.join(
                config.RESULTS_FOLDER,
                meta_dict['discipline'],
                meta_dict['year'],
                meta_dict['class'],
                '')
        os.makedirs(directory, exist_ok=True)
        file_name = (meta_dict['name']+'-result-'
                     + meta_dict['selection'] + '.csv')
        file_dir = os.path.join(directory, file_name)
        data_frame_result.to_csv(file_dir, index=True)


if __name__ == '__main__':
    main()