import numpy as np
import pandas as pd
from scipy.stats import sem
from scipy.ndimage import gaussian_filter1d
from scipy.signal import find_peaks
from scipy import signal


def combine_fish_data(*args):
    '''Combines preprocessed data from all fish into a 3D numpy array'''
    combined_fish = np.stack((args),axis=0)
    return combined_fish


def omr_analysis(combined_fish):
    '''Full data analysis of OMR data'''

    # Average cumulative heading and SEM per frame
    cumul_av = [np.nanmean(combined_fish[:,frame,4]) for frame in combined_fish]
    cumul_sem = [sem(combined_fish[:,frame,4],nan_policy='omit') for frame in combined_fish]

    # Continuous wavelet transform and fast fourier transform to denoise data and find events



    analysis = []
    return analysis



def make_fish_list():
    pass

def make_event_list():
    pass

def data_summary():
    pass
