from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_column as fc

import tensorflow as tf

# Load dataset.
dftrain = pd.read_csv('http://unes.epizy.com/database.csv') # training data
dfeval = pd.read_csv('http://unes.epizy.com/eval.csv') # testing data
y_train = dftrain.pop('winner')
print(dftrain.head())
y_eval = dfeval.pop('winner')
print(dftrain.head())

CATEGORICAL_COLUMNS = [
"top_red_champion", 
"top_blue_champion",
"jg_red_champion",
"jg_blue_champion", 
"mid_red_champion", 
"mid_blue_champion",
"adc_red_champion", 
"adc_blue_champion",
"sup_red_champion", 
"sup_blue_champion"]
NUMERIC_COLUMNS = ["top_red_champion_ward", "top_red_rota_champion_month", "top_red_champion_alltime_wr","top_red_champion_kda", 
"top_blue_champion_ward", "top_blue_rota_champion_month", "top_blue_champion_alltime_wr","top_blue_champion_kda", 
"jg_red_champion_ward", "jg_red_rota_champion_month", "jg_red_champion_alltime_wr","jg_red_champion_kda", 
"jg_blue_champion_ward", "jg_blue_rota_champion_month", "jg_blue_champion_alltime_wr","jg_blue_champion_kda", 
"mid_red_champion_ward", "mid_red_rota_champion_month", "mid_red_champion_alltime_wr","mid_red_champion_kda", 
"mid_blue_champion_ward", "mid_blue_rota_champion_month", "mid_blue_champion_alltime_wr","mid_blue_champion_kda",
"adc_red_champion_ward", "adc_red_rota_champion_month", "adc_red_champion_alltime_wr","adc_red_champion_kda",
"adc_blue_champion_ward", "adc_blue_rota_champion_month", "adc_blue_champion_alltime_wr","adc_blue_champion_kda",
"sup_red_champion_ward", "sup_red_rota_champion_month", "sup_red_champion_alltime_wr","sup_red_champion_kda",
"sup_blue_champion_ward", "sup_blue_rota_champion_month", "sup_blue_champion_alltime_wr","sup_blue_champion_kda"]

feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
  vocabulary = dftrain[feature_name].unique()  # gets a list of all unique values from given feature column
  feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
  feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

print(list(feature_columns[49]))


dftrain.head()


def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
  def input_function():  # inner function, this will be returned
    ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))  # create tf.data.Dataset object with data and its label
    if shuffle:
      ds = ds.shuffle(1000)  # randomize order of data
    ds = ds.batch(batch_size).repeat(num_epochs)  # split dataset into batches of 32 and repeat process for number of epochs
    return ds  # return a batch of the dataset
  return input_function  # return a function object for use

train_input_fn = make_input_fn(dftrain, y_train)  # here we will call the input_function that was returned to us to get a dataset object we can feed to the model
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)


linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)
# We create a linear estimtor by passing the feature columns we created earlier

linear_est.train(train_input_fn)  # train
result = linear_est.evaluate(eval_input_fn)  # get model metrics/stats by testing on tetsing data

clear_output()  # clears consoke output
print(result['accuracy'])  # the result variable is simply a dict of stats about our model

result = list(linear_est.predict(eval_input_fn))
print(dfeval.loc[0])
print(y_eval.loc[0])
print(result[0]['probabilities'][1])


