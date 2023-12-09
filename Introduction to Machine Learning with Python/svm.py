# -*- coding: utf-8 -*-
"""SVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cMP5ymWZt2Kwc_fSLNpdFQDtJABtqU9U
"""

from sklearn import datasets                          # import cancer dataset from sklearn
from sklearn import svm                               # Import SVM algorithm from sklearn 
from sklearn.metrics import accuracy_score            # compute the accuracy of the model after training
from sklearn.model_selection import train_test_split  # splitting data into training set and testing set

#####################################################################################################
# This program will classify a tumor as malignant or benign using the supervised  ML                #
# algorithm, Support Vector Machines (SVM). The features that will be used to train the             #
# model include:                                                                                    #
# ['mean radius' 'mean texture' 'mean perimeter' 'mean area'                                        #
# 'mean smoothness' 'mean compactness' 'mean concavity'                                             #
# 'mean concave points' 'mean symmetry' 'mean fractal dimension'                                    #
# 'radius error' 'texture error' 'perimeter error' 'area error'                                     #
# 'smoothness error' 'compactness error' 'concavity error'                                          #
# 'concave points error' 'symmetry error' 'fractal dimension error'                                 #
# 'worst radius' 'worst texture' 'worst perimeter' 'worst area'                                     #
# 'worst smoothness' 'worst compactness' 'worst concavity'                                          #
# 'worst concave points' 'worst symmetry' 'worst fractal dimension']                                #
##################################################################################################### 

#######################################################################################
# Step 1: Load the data and store the labels in variable x and target in variable y   #
#######################################################################################
cancer_data = datasets.load_breast_cancer()

print("Features: \n", cancer_data.feature_names, "\n")
print("Targets: \n", cancer_data.target_names)

x = cancer_data.data
y = cancer_data.target

#######################################################################################
# Step 2: Split the dataset into a training set and test set.                         #
#         70% of the data should be for the training set.                             #
#         30% of the data should be for the test set.                                 #
#######################################################################################

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3) 


classes = ['malignant', 'benign ']  # 0 = malignant, 1 = benign

##################################
# Step 3: Create the model.      #
##################################

# SVC: Support Vector Classification
svm_model = svm.SVC(kernel="linear")

##################################
# Step 4: Train the model.       #
##################################
svm_model.fit(x_train, y_train)

##################################
# Step 5: Test the model.        #
##################################
predicted = svm_model.predict(x_test)

##################################
# Step 6: Evaluate the model.    #
##################################
accuracy = accuracy_score(y_test, predicted) * 100

print("\nAccuracy of the model is: " + str(round(accuracy, 2)) + "%\n")

##################################
# Step 7: Print Results.         #
##################################
for i in range(len(predicted)):
  print("Predicted: ", classes[predicted[i]], "\nData: ", x_test[i], "\nActual: ", classes[y_test[i]], "\n")