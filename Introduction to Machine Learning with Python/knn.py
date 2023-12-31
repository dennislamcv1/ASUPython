# -*- coding: utf-8 -*-
"""KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U3HCO8nHNEJLLNOmecQDi5RuJWqEJBM1
"""

import pandas as pd                                       # import pandas to store data in dataframes using datasets from sklearn
import numpy  as np                                       # import numpy to use arrays
from sklearn.neighbors import KNeighborsClassifier        # import the KNN algorithm from sklearn.neighbors
from sklearn.model_selection import train_test_split      # splitting data into training set and testing set
from sklearn import linear_model                          # utilizing linear model from sklearn
from sklearn import preprocessing                         # import preprocessing to preprocess the data

# Link to dataset: https://archive.ics.uci.edu/ml/datasets/car+evaluation

#######################################################################################################
# This program will classify the acceptability condition of a car based on the buying price,          #
# maintainance price, number of doors, number of people to carry, size of the luggage boot,           #
# and the estimated safety of the car.                                                                #
#######################################################################################################


#######################################################################################
# Step 1: Load the data and store the labels in variable x and target in variable y   #
#######################################################################################

# Make sure to add the labels and target into car.data before proceeding
car_df = pd.read_csv("car.data")
car_df.head() # prints out first 5 rows of the dataframe in car.data

# Convert non-numeric labels into numeric labels
# Encode target labels with value between 0 and n_classes-1
preprocessed_data = preprocessing.LabelEncoder() 

# fit_transform() wil fit label encoder and return encoded labels 
buying            =   preprocessed_data.fit_transform(list(car_df["buying"])) 
maintainance      =   preprocessed_data.fit_transform(list(car_df["maint"]))
number_of_doors   =   preprocessed_data.fit_transform(list(car_df["door"])) 
number_of_people  =   preprocessed_data.fit_transform(list(car_df["persons"])) 
lug_boot_size     =   preprocessed_data.fit_transform(list(car_df["lug_boot"])) 
safety_measure    =   preprocessed_data.fit_transform(list(car_df["safety"])) 
cls               =   preprocessed_data.fit_transform(list(car_df["class"])) 

#####################################################
# Taregets:                                         #
#   3 = vhigh                                       #
#   2 = high                                        #
#   1 = med                                         #
#   0 = low                                         #
#####################################################

X = list(zip(buying, maintainance, number_of_doors, number_of_people, lug_boot_size, safety_measure)) # features - properties of training data
Y = list(cls) # label - output 

#######################################################################################
# Step 2: Split the dataset into a training set and test set.                         #
#         70% of the data should be for the training set.                             #
#         30% of the data should be for the test set.                                 #
#######################################################################################

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3)

##################################
# Step 3: Create the model.      #
##################################

knn_model = KNeighborsClassifier(n_neighbors=3) # number of neighbors

##################################
# Step 4: Train the model.       #
##################################

knn_model.fit(x_train,y_train) 

##################################
# Step 5: Test the model.        #
##################################

predicted = knn_model.predict(x_test) 

##################################
# Step 6: Evaluate the model.    #
##################################

accuracy = knn_model.score(x_test, y_test)
accuracy = round(accuracy*100, 2)
print(f"Accuracy of the model is: {accuracy}%")

##################################
# Step 7: Print out results.     #
##################################

# print out test data, prediciton, and actual value
targets = ["unacc", "acc", "good", "vgood"]
for i in range(len(predicted)):
  print("Predicted: ", predicted[i], "Data: ", x_test[i], "Actual: ", y_test[i])

# print out test data, prediciton, and actual value
for i in range(len(predicted)):
  print("Predicted: ", targets[predicted[i]], "Data: ", x_test[i], "Actual: ", targets[y_test[i]])