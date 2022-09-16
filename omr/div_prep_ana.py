import pandas as pd
import numpy as np
import os
from divide_data import divide_data_by_contrast, divide_data_by_flow_direction
from preprocess import omr_preprocess


def all_file_loop(folder_path):
    '''Loops through all data files, dividing them into flow and contrast,
    preprocessing them and writing them into new/combines files for further analysis'''

    # Putting all csv file paths into one list to loop through
    folder = os.fsencode(folder_path)
    filenames = []
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith('.csv'):
            filenames.append(filename)

    # Looping through all csv files, dividing them and preprocessing
    for f in filenames:
        data_path = os.path.join(folder_path, f)
        data = pd.read_csv(data_path)
        data.columns = ['X_coord', 'Y_coord', 'heading_direction', \
                'cumulative_direction','beat_freq', 'beat_amp', \
                'tail_move?', 'timestamp', 'contrast_level', 'flow_direction']

        # dividing data into flow direction and contrast level
        right, left = divide_data_by_flow_direction(data)
        right_C0, right_C01, right_C1, right_C2, right_C3, right_C5, right_C7, right_C10 = divide_data_by_contrast(right)
        left_C0, left_C01, left_C1, left_C2, left_C3, left_C5, left_C7, left_C10 = divide_data_by_contrast(left)

        # preprocessing all dataframes
        df_list = [right_C01, right_C1, right_C2, right_C3, right_C5, right_C7, right_C10,\
                    left_C01, left_C1, left_C2, left_C3, left_C5, left_C7, left_C10]
        right_C01.name = 'right_C01'
        right_C1.name = 'right_C1'
        right_C2.name = 'right_C2'
        right_C3.name = 'right_C3'
        right_C5.name = 'right_C5'
        right_C7.name = 'right_C7'
        right_C10.name = 'right_C10'
        left_C01.name = 'left_C01'
        left_C1.name = 'left_C1'
        left_C2.name = 'left_C2'
        left_C3.name = 'left_C3'
        left_C5.name = 'left_C5'
        left_C7.name = 'left_C7'
        left_C10.name = 'left_C10'
        for df in df_list:
            preproc = omr_preprocess(df)
            file_name = f'preprocessed_{df.name}.csv'
            preproc.to_csv(os.path.join(folder_path,file_name))



if __name__ == "__main__":
    folder_path = input('Files to preprocess: ')
    all_file_loop(folder_path)
