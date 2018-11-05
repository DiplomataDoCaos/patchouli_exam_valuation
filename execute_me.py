#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
execute_me

Created on Tue Oct 23 14:19:06 2018

@author: fernandotal
"""

import pandas as pd
import numpy as np
import os
import config
import etl_excel_files
import apply_ctt_test
import class_fuse
import result_fuse



def main():
    """
    This is the main method
    """
    if config.CONSIDERATED_TRY == 'both':
        config.CONSIDERATED_TRY = 'first'
        etl_excel_files.main()
        config.CONSIDERATED_TRY = 'last'
        etl_excel_files.main()
        config.CONSIDERATED_TRY = 'both'
    else:
        etl_excel_files.main()
    if config.JOIN_CLASSES:
        class_fuse.main()
    apply_ctt_test.main()
    if config.CONSIDERATED_TRY == 'both':
        result_fuse.main()


if __name__ == '__main__':
    main()
