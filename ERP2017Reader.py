import pandas as pd
import tables #required for read_hdf (Data is stored in tables format within hdf5 files)

from glob import glob

if __name__ == '__main__':
    # Load signal descriptions
    signal_descriptions = pd.read_csv('signal_descriptions.csv', index_col=0).squeeze().to_dict()
    # For all files:
    for file_path in glob('data/*.hdf5'):
        # Load as Pandas DataFrame
        df = pd.read_hdf(file_path)