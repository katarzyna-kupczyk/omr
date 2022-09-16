import pandas as pd

def divide_data_by_flow_direction(data):
    '''Dividing raw data from one fish into 2 dataframes with either left or right OMR flow'''
    data.columns = ['X_coord', 'Y_coord', 'heading_direction', \
                'cumulative_direction','beat_freq', 'beat_amp', \
                'tail_move?', 'timestamp', 'contrast_level', 'flow_direction']
    right = pd.DataFrame(data[data.flow_direction == 1])
    left = pd.DataFrame(data[data.flow_direction == 2])
    zero = pd.DataFrame(data[data.flow_direction == 0])

    return right, left, zero

def divide_data_by_contrast(data):
    '''Dividing raw data from one fish and one flow direction into contrast levels'''
    C_0 = pd.DataFrame(data[data.contrast_level == 0])
    C_01 = pd.DataFrame(data[data.contrast_level == 0.01])
    C_1 = pd.DataFrame(data[data.contrast_level == 0.1])
    C_2 = pd.DataFrame(data[data.contrast_level == 0.2])
    C_3 = pd.DataFrame(data[data.contrast_level == 0.3])
    C_5 = pd.DataFrame(data[data.contrast_level == 0.5])
    C_7 = pd.DataFrame(data[data.contrast_level == 0.7])
    C_10 = pd.DataFrame(data[data.contrast_level == 1])
    return C_0, C_01, C_1, C_2, C_3, C_5, C_7, C_10

def divide_C0(C0):
    C0 = C0.reset_index()
    C0['counter'] = 0
    counter = 0
    first_index = 0
    for i, r in C0[:-1].iterrows():
        if C0.iloc[i+1]['index'] - r['index'] != 1:
            counter +=1
            last_index = r['index']
            C0.loc[first_index:i,'counter'] = counter
            first_index = i+1

    C0_0 = pd.DataFrame(C0[C0.counter == 0]).drop(columns=['counter','index']).reset_index().drop(columns=['index'])
    C0_1 = pd.DataFrame(C0[C0.counter == 1]).drop(columns=['counter','index']).reset_index().drop(columns=['index'])
    C0_2 = pd.DataFrame(C0[C0.counter == 2]).drop(columns=['counter','index']).reset_index().drop(columns=['index'])
    C0_3 = pd.DataFrame(C0[C0.counter == 3]).drop(columns=['counter','index']).reset_index().drop(columns=['index'])
    C0_4 = pd.DataFrame(C0[C0.counter == 4]).drop(columns=['counter','index']).reset_index().drop(columns=['index'])
    C0_5 = pd.DataFrame(C0[C0.counter == 5]).drop(columns=['counter','index']).reset_index().drop(columns=['index'])
    C0_6 = pd.DataFrame(C0[C0.counter == 6]).drop(columns=['counter','index']).reset_index().drop(columns=['index'])
    C0_7 = pd.DataFrame(C0[C0.counter == 7]).drop(columns=['counter','index']).reset_index().drop(columns=['index'])
    C0_8 = pd.DataFrame(C0[C0.counter == 8]).drop(columns=['counter','index']).reset_index().drop(columns=['index'])
    C0_9 = pd.DataFrame(C0[C0.counter == 9]).drop(columns=['counter','index']).reset_index().drop(columns=['index'])
    C0_10 = pd.DataFrame(C0[C0.counter == 10]).drop(columns=['counter','index']).reset_index().drop(columns=['index'])
    C0_11 = pd.DataFrame(C0[C0.counter == 11]).drop(columns=['counter','index']).reset_index().drop(columns=['index'])
    C0_12 = pd.DataFrame(C0[C0.counter == 12]).drop(columns=['counter','index']).reset_index().drop(columns=['index'])

    return C0_0, C0_1, C0_2, C0_3, C0_4, C0_5, C0_6, C0_7, C0_8, C0_9, C0_10, C0_11, C0_12


if __name__ == "__main__":

    path_to_data = input('PATH TO DATA: ')
    data = pd.read_csv(path_to_data)
    data.columns = ['X_coord', 'Y_coord', 'heading_direction', \
                'cumulative_direction','beat_freq', 'beat_amp', \
                'tail_move?', 'timestamp', 'contrast_level', 'flow_direction']
    right, left = divide_data_by_flow_direction(data)
    ### preprocess all data ###



    right_C0, right_C01, right_C1, right_C2, right_C3, right_C5, right_C7, right_C10 = divide_data_by_contrast(right)
    left_C0, left_C01, left_C1, left_C2, left_C3, left_C5, left_C7, left_C10 = divide_data_by_contrast(left)
    print('This is the left_C01: \n',left_C01)
    print('Successful data division')
