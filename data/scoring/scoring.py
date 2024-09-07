import helper
import pandas as pd
import os 
import json

pd.options.mode.chained_assignment = None  # default='warn'

import subprocess
import sys


subprocess.call([sys.executable, '-m', 'pip', 'install', "sacrebleu"], stderr=subprocess.DEVNULL)

## read data

prediction_dir = "path_to_your_prediction_data/"
reference_dir = "../" # path_to_your_gold_data
score_dir = 'path_to_save_your_output'
print('Reading prediction')

predicted_data = helper.read_data(os.path.join(prediction_dir, 'prediction.csv'))
data_split = "eval" # "test", "train"
gold_data = helper.read_data(os.path.join(reference_dir, data_split+'.csv'))

print("Checking Data Format")
# merge gold and predicted data by sent-id to consider shuffled or wrong input data
full_data = helper.check_data(gold_data, predicted_data)


## score data
scores = helper.score_both_tasks(full_data)
print(scores)

with open(os.path.join(score_dir, 'scores.json'), 'w') as score_file:
    score_file.write(json.dumps(scores))
