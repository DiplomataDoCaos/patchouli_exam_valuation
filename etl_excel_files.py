#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
etl_excel_files

Created on Mon Oct  1 13:26:44 2018

@author: fernandotal

Objective: Pickup the data from excel files of Moodle and Mackenzie and
transform in a padronized structure for analysis use

It executes:
> transform comma to dot, so it can read ecimal points
> remove - and convert in 0
> remove repeated entries from the same studant
> remove unecessary identification information
> remove the precalculated mean at the bottom of the file

Files for use with this code are not providede, as they would reveal personal
information

But feel free to adpt the code for your need of transformation

Version of pack used:
Pandas - 0.23.0

"""

import pandas as pd
import os
import config


def clean(data_frame, file_origin):
    """
    Do the cleaning of the file /TODO Write a better description
    """
    # TODO Find a way to input which columns you want to drop
    if file_origin == 'USP':
        useless_info = config.USELESS_INFO_USP
        identifier = config.IDENTIFIER_USP
    else:
        useless_info = config.USELESS_INFO_MACK
        identifier = config.IDENTIFIER_MACK

    # need to be made generic
    # Removing duplicate submissions
    # Considering last entry as the valid

    data_frame = data_frame.drop_duplicates(identifier,
                                            config.CONSIDERATED_TRY)

    # Cleaning desnecessary information
    data_frame = data_frame.drop(useless_info, axis=1)

    # Removing the means at the botton (it's pre-calculated and I will drop
    # lines)
    data_frame = data_frame.drop(data_frame.index[-1])

    # Getting the original score of each question and providing the new name
    new_name_list, points_list = extract_header_info(data_frame.columns)
    data_frame.columns = new_name_list

    # Removing questions of score 0
    data_frame, points_list = remove_null_questions(data_frame, points_list)

    # Removing empty entries: converting to 0
    data_frame = data_frame.replace('-', "0.00")

    # Convert comma to dot and then to number
    data_frame = data_frame.applymap(lambda x: x.replace(',', '.'))
    data_frame = data_frame.astype('float64')

    # Calculate the new total, using padronized score
    data_frame['total'] = 0
    data_frame = score_normalize(points_list, data_frame)
    for column in data_frame.columns[1:]:
        data_frame['total'] += data_frame[column]

    return (data_frame)  # points list is not necessary anymore


def detect_type(file_name):
    """
    Recieves a file name and decides if it's from Mack or USP
    Returns:
    file_origin: String indicating file origin
    > Can be USP or Mack
    """
    detector = 'EAD'

    if file_name.startswith(detector):
        file_origin = 'USP'
    else:
        file_origin = 'Mack'
    return(file_origin)


def extract_header_info(name_list):
    """
    Decompose the header (column names) of a dataframe
    Recieves: list-like
    Returns:
    list of new names in string
    list of points each question has, already in float format
    OBS: points list doesn't include the points of total!
    """
    new_name_list = []
    points_list = []
    new_name_list.append("total")
    # TODO : Check if the compesation of the total must happen here
    points_list = [1]  # To compesate the lack of the total points
    for name in name_list[1:]:  # TODO Break into extract_score and extractname
        new_name, points = name.split("/")
        new_name = new_name.replace(" ", "")
        new_name = new_name.replace(".", "")
        new_name = new_name.lower()
        new_name_list.append(new_name)
        points = points.replace(',', '.')
        points = float(points)
        points_list.append(points)
    return(new_name_list, points_list)


def extract_name_info(file_name):
    """
    Cleans the name of files coming from standard Moodle (in portuguese ver.)
    Use to make it easier for references in name meta-data

    It extracts the following infos:
    - Discipline of the course
    - Class
    - Year of aplication
    - Exam name

    Input: file_name: String with pure file name, without the path
    return: meta_dict:dictionary with the entries
    """

    meta_list = file_name.split('-')
    meta_dict = {'discipline': meta_list[0],
                 'class': meta_list[1],
                 'year': meta_list[2],
                 'name': meta_list[3]}

    return(meta_dict)


def find_files(base_folder, end_file):
    """Search for the files necessary for work
    BASE_FOLDER = where the files are, used for search

    returns
    file_path_list: List of directories necessary"""

    file_path_list = []
    for f_path, f_folder, f_names in os.walk(base_folder):
        for file in f_names:
            if file.endswith(end_file):
                file_path_list.append(str(os.path.join(f_path, file)))
    file_path_list.sort()
    return(file_path_list)


def remove_null_questions(data_frame, points_list):
    """
    Removes questions that have 0 score from the database

    NOTE: Questions with 0 score are still usefull if
    they have a good amount of answers
    """
    # TODO a version that eliminates questions that are badly anwsered

    # Breakble in null_detector
    list_index = range(len(points_list))

    kill_list = [x for x in list_index if points_list[x] == 0]

    if kill_list:
        points_list = [points_list[x]
                       for x in list_index if x not in kill_list]
        data_frame = data_frame.drop(data_frame.columns[kill_list], 1)

    # TODO AInda não está gerando o points_list novo corretamente
    # Confirm that return is used correctly to mutables

    return(data_frame, points_list)


def score_normalize(points_list, data_frame):
    """
    Normalizes the score so all questions score 1 point each

    Input:
    points_list: List of original points of the question
    data_frame: data_frame with scores to be processed

    Output: Nome (local changes on data_frame)
    """

    multi_list = []
    for point_score in points_list:
        if point_score != 1.0:
            multi = 1.0/point_score
            multi_list.append(multi)
        else:
            multi_list.append(0)

    for index in range(len(multi_list)):
        column = data_frame.columns[index]
        if multi_list[index] != 0:
            data_frame[column] = data_frame[column] * multi_list[index]
            data_frame[column] = data_frame[column].apply("{0:.2f}".format)
            data_frame[column] = data_frame[column].apply(float)
            # TODO check if this truncates or rounds the number

    return (data_frame)


def main():
    """
    Main cycle of the program, see the top docstring
    """
    file_path_list = find_files(config.BASE_FOLDER, "notas.xlsx")
    for file_path in file_path_list:
        folder_path, file_name = os.path.split(file_path)
        # detecting origin so we can identify the rows
        file_origin = detect_type(file_name)
        # Reading file, now it's locked
        data_frame = pd.read_excel(file_path)
        data_frame = clean(data_frame, file_origin)
        meta_dict = extract_name_info(file_name)
        # TODO: Extract this function
        directory = os.path.join(
                config.PADRONIZED_FOLDER,
                meta_dict['discipline'],
                meta_dict['year'],
                meta_dict['class'],
                '')
        os.makedirs(directory, exist_ok=True)
        file_name = meta_dict['name'] + '-' + config.CONSIDERATED_TRY + '.csv'
        file_dir = os.path.join(directory, file_name)
        data_frame.to_csv(file_dir, index=False)


if __name__ == '__main__':
    main()
