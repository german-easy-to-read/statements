import pandas as pd
import re
import random
import numpy as np


# 0. Create all baseline dataframes and copy sentence ids
base_all_1 = pd.DataFrame()
base_random = pd.DataFrame()
base_string_split = pd.DataFrame()
eval = pd.read_csv("../eval_blind.csv")

base_all_1["sent-id"] = eval["sent-id"]
base_random["sent-id"] = eval["sent-id"]
base_string_split["sent-id"] = eval["sent-id"]

# 1. Baseline all 1 -> empty statement spans
base_all_1["num_statements"] = [1] * len(base_all_1)
base_all_1["statement_spans"] = [[]] * len(base_all_1)
base_all_1.to_csv("baseline_all_1.csv", index=False)

# 2. Baseline with random number of statements
num_statements_random = []
statement_spans_random = []
for phrase_tokenized in eval["phrase_tokenized"]:
	num_statements = random.randint(1,3)
	num_statements_random.append(num_statements)
	spans = []
	if num_statements > 1:
		phrase_tokens = phrase_tokenized.split(" ")
		last_index = int(phrase_tokens[-1].split(":=")[0])
		#print(range(1, last_index -1), num_statements -1)
		#split_indices = sorted(random.sample(range(1, last_index -1), num_statements -1))
		#print(np.arange(last_index +1), split_indices)
		#for split in np.split(np.arange(last_index +1), split_indices):
		for split in np.array_split(np.arange(last_index +1), num_statements):
			spans.append(split.tolist())
	statement_spans_random.append(spans)
base_random["num_statements"] = num_statements_random
base_random["statement_spans"] = statement_spans_random
base_random.to_csv("baseline_all_random.csv", index=False)

# 3. Baseline splits at conjunctions
conjunctions = ["und", "oder", "aber"]

def get_conjunction_matches(phrase: str):
	return re.findall(r"|".join([f"\d+:={c} " for c in conjunctions]), phrase)

def split_recursive(phrase:str, init=True):
	matches = get_conjunction_matches(phrase)
	if len(matches) == 0:
		tokenized = phrase.strip().split(" ")
		return [int(tok.split(":=")[0]) for tok in tokenized] if not init else []
	else:
		spans = []
		match = matches[0]
		for text in phrase.split(match):
			result = split_recursive(text, init=False)
			if type(result[0]) != list:
				spans.append(result)
			else:
				spans += result
		return spans


base_string_split["num_statements"] = [len(get_conjunction_matches(phrase)) + 1 for phrase in eval["phrase_tokenized"]]
base_string_split["statement_spans"] = [split_recursive(phrase) for phrase in eval["phrase_tokenized"]]
base_string_split.to_csv("baseline_string_split.csv", index=False)

#test = "Bekannte Rück-ruf-aktionen hat es bei Autos und bei Essen und Trinken gegeben."
#test2 = "Heute scheint die Sonne und mir ist zu warm, aber ich gehe trotzdem spazieren."
#print(' '.join([str(j)+':='+tok for j, tok in enumerate(test.split(' '))]))
#print(split_prepare(test))
#print(split_prepare(test2))