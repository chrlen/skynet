import sklearn.datasets as skld
import sklearn.model_selection as sklm
import sklearn.svm as sklsvm
import skynet as skn

def create_iris_svm_classifier():
    IRIS_DATA = skld.load_iris()
    IRIS_X_TRAIN, IRIS_X_TEST, IRIS_Y_TRAIN, IRIS_Y_TEST = sklm.train_test_split(
        IRIS_DATA['data'],
        IRIS_DATA['target'],
        test_size=0.33,
        random_state=skn.RANDOM_STATE)
    IRIS_SVM = sklsvm.SVC()
    IRIS_SVM.fit(IRIS_X_TRAIN,IRIS_Y_TRAIN)
    return IRIS_SVM


