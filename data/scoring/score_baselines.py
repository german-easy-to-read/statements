import helper
import pandas as pd
import os
import json

pd.options.mode.chained_assignment = None  # default='warn'

prediction_dir = "../eval_baselines"
reference_dir = "../"  # path_to_your_gold_data
score_dir = ''
data_split = "eval" # "test", "train"
print('Reading prediction')

baselines = {
    "baseline_all_1.csv": [],
    "baseline_all_random.csv": [],
    "baseline_string_split.csv": [],
}

for baseline in baselines.keys():
    print("\n\n**", baseline)
    predicted_data = helper.read_data(os.path.join(prediction_dir, baseline))
    gold_data = helper.read_data(os.path.join(reference_dir, data_split+'.csv'))

    print("Checking Data Format")
    # merge gold and predicted data by sent-id to consider shuffled or wrong input data
    full_data = helper.check_data(gold_data, predicted_data)

    ## score data
    scores = helper.score_both_tasks(full_data)
    print("\t", scores)
    baselines[baseline] = scores

with open(os.path.join(score_dir, 'baseline_scores.json'), 'w') as score_file:
    score_file.write(json.dumps(baselines))
