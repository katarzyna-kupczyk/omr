import pandas as pd
import numpy as np
from divide_data import divide_data_by_contrast
from divide_data import divide_data_by_flow_direction


def omr_preprocess(data):
    # remove timestamp and extras
    # keep x, y, heading, cumulative, timestamp
    data.columns = ['X_coord', 'Y_coord', 'heading_direction', \
                'cumulative_direction','beat_freq', 'beat_amp', \
                'tail_move?', 'timestamp', 'contrast_level', 'flow_direction']
    new = data.drop(columns = ['beat_freq', 'beat_amp','tail_move?', 'contrast_level', 'flow_direction'])

    # resetting index
    new = pd.DataFrame(new)
    new = new.set_index('timestamp').reset_index()


    # remove time points where there was an angle change of more than pi from one frame to another
    for i, row in new.iterrows():
        if i+1 == len(new):
            break
            # modify to add the exclusion zone
        if np.abs(new.at[i+1,'cumulative_direction']-new.at[i,'cumulative_direction']) >= 2.5:
            new.at[i+1, 'cumulative_direction'] = new.at[i,'cumulative_direction']

    tstp = np.arange(0,30,30/len(new))
    if len(new['timestamp']) != len(tstp):
        tstp = tstp[:-1]
    tstpdate = pd.to_datetime(tstp,unit='s')
    new['timestamp'] = tstp
    new['tstpdate'] = tstpdate
    new = new.set_index('tstpdate')
    new_df = new.resample('10ms')
    new_df = new_df.first()
    new_df.interpolate(method='linear',inplace=True)

    interp = new_df.copy()
    # setting first cumulative_angle to zero and ajdusting all others
    interp.iloc[:,4] -= interp.iloc[0,4]


    # calculating distance traveled between each timeframe
    # distance = sqrt((x2-x1)**2 + (y2-y1)**2)
    interp['distance_pts'] = 0
    for row in range(1,len(interp),1):
        distance = np.sqrt((interp['X_coord'][row]-interp['X_coord'][row-1])**2\
                            +(interp['Y_coord'][row]-interp['Y_coord'][row-1])**2)
        interp.iloc[row,5] = distance


    #cleaning the timestamps
    interp.insert(0, 'new_timestamp', range(1, 1 + len(interp)))
    interp = interp.drop(columns=['timestamp']).rename(columns={'new_timestamp':'timestamp'})
    interp['timestamp'] = interp['timestamp']/100

    #resetting index to integers
    interp = interp.reset_index()
    interp = interp.drop(columns=['tstpdate'])

    return np.array(interp)


def combine_fish_data(*args):
    '''Combines preprocessed data from all fish into a 3D numpy array'''
    combined_fish = np.stack((args),axis=0)
    return combined_fish



if __name__ == "__main__":
    path_to_data = input('PATH TO DATA: ')
    data = pd.read_csv(path_to_data)
    data.columns = ['X_coord', 'Y_coord', 'heading_direction', \
                'cumulative_direction','beat_freq', 'beat_amp', \
                'tail_move?', 'timestamp', 'contrast_level', 'flow_direction']
    right, left = divide_data_by_flow_direction(data)
    right_C0, right_C01, right_C1, right_C2, right_C3, right_C5, right_C7, right_C10 = divide_data_by_contrast(right)
    left_C0, left_C01, left_C1, left_C2, left_C3, left_C5, left_C7, left_C10 = divide_data_by_contrast(left)
    preproc_left_C01 = omr_preprocess(left_C01)

    print('This is the preprocessed left_C01: \n',preproc_left_C01)
    print('Successful data preprocessing')
