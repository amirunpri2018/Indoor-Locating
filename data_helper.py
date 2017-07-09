import pandas as pd
import numpy as np

def load(train_file_name, valid_file_name):
    """
        Load the training data and validation data
        In this function, 1/10 part of training will be the 'final' validation data.
        The other 9/10 part of training will be the 'final' training data.
        At last, the validation data will be the 'final' testing data.

        The x data contain 520 rssi value.
        The y data contain the Longitude, Latitude, floor ID and building ID.

        Arg:    train_file_name - The name of the training file
                valid_file_name - The name of the validation file
        Ret:    training x, training y, validation x, validation y, testing x and testing y data
    """
    # Read the file
    if train_file_name == None or valid_file_name == None:
        print 'file name is None...'
        exit()
    train_data_frame = pd.read_csv(train_file_name)
    test_data_frame = pd.read_csv(valid_file_name)

    # Random pick 1/10 data to be the final validation data
    rest_data_frame = train_data_frame
    valid_data_trame = pd.DataFrame(columns=train_data_frame.columns)
    valid_num = int(len(train_data_frame)/10)
    sample_row = rest_data_frame.sample(valid_num)
    rest_data_frame = rest_data_frame.drop(sample_row.index)
    valid_data_trame = valid_data_trame.append(sample_row)
    train_data_frame = rest_data_frame

    # Split data frame and return
    training_x = train_data_frame.get_values().T[:520].T
    training_y = train_data_frame.get_values().T[[520, 521, 522, 523], :].T
    validation_x = valid_data_trame.get_values().T[:520].T
    validation_y = valid_data_trame.get_values().T[[520, 521, 522, 523], :].T
    testing_x = test_data_frame.get_values().T[:520].T
    testing_y = test_data_frame.get_values().T[[520, 521, 522, 523], :].T
    return training_x, training_y, validation_x, validation_y, testing_x, testing_y

load('./TrainingData.csv', './ValidationData.csv')