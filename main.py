from svm import SVM
import numpy as np
import data_helper

train_csv_path = './TrainingData.csv'
valid_csv_path = './ValidationData.csv'

if __name__ == '__main__':
    train_x, train_y, valid_x, valid_y, test_x, test_y = \
        data_helper.load(train_csv_path, valid_csv_path)
    model = SVM()
    # model.fit(train_x, train_y)
    # y_ = model.predict(test_x)
    # print y_
    # print test_y
    print model.error(test_x, test_y)