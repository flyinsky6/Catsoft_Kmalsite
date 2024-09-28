import numpy as np
from catboost import CatBoostClassifier
from sklearn.metrics import roc_auc_score,accuracy_score,recall_score,precision_score,f1_score,matthews_corrcoef
from sklearn.metrics import roc_curve, auc, precision_recall_curve
import matplotlib.pyplot as plt


data_path = "./Dataset/"

x_train1 = np.load(data_path + "x_trainCTDC.npy")
x_test1 = np.load(data_path + "x_testCTDC.npy")
x_train2 = np.load(data_path + "x_trainEAAC.npy")
x_test2 = np.load(data_path + "x_testEAAC.npy")
x_train3 = np.load(data_path + "x_trainEGAAC.npy")
x_test3 = np.load(data_path + "x_testEGAAC.npy")
x_train4 = np.load(data_path + "x_trainPDB.npy")
x_test4 = np.load(data_path + "x_testPDB.npy")

x_train123=np.hstack((x_train1,x_train2,x_train3))
y_train = np.load(data_path + "y_train.npy").ravel()

params123 ={'iterations': 1824,'l2_leaf_reg': 6, 'learning_rate': 0.01, 'max_depth': 13, 'subsample': 0.8}
params4 = {'iterations':491,'l2_leaf_reg': 2, 'learning_rate': 0.03, 'max_depth': 12, 'subsample': 0.6}

model1 = CatBoostClassifier(**params123,early_stopping_rounds=20,logging_level='Silent')
model1.fit(x_train123, y_train)
model2 = CatBoostClassifier(**params4,early_stopping_rounds=20,logging_level='Silent')
model2.fit(x_train4, y_train)

model1.save_model('model1')
model2.save_model('model2')


class MyModel:
    def __init__(self):
        self.params1 = {'iterations': 1824, 'l2_leaf_reg': 6, 'learning_rate': 0.01, 'max_depth': 13, 'subsample': 0.8}
        self.params2 = {'iterations': 491, 'l2_leaf_reg': 2, 'learning_rate': 0.03, 'max_depth': 12, 'subsample': 0.6}

        self.model1 = CatBoostClassifier()
        self.model1.load_model("model1")
        self.model2 = CatBoostClassifier()
        self.model2.load_model("model2")

    def predict(self, data1, data2):
        preds1 = self.model1.predict_proba(data1)[:, 1]
        preds2 = self.model2.predict_proba(data2)[:, 1]

        weight = [0.4538986914845343, 0.5461013085154657]

        soft_preds = preds1 * weight[0] + preds2 * weight[1]
        soft_pred = np.round(soft_preds >= 0.5).astype(int)

        return soft_preds, soft_pred

