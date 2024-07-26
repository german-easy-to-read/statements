#!/usr/bin/env python
# coding: utf-8

import json
import os
import numpy as np
import pandas as pd

from sklearn.metrics import accuracy_score, mean_absolute_error, mean_squared_error, precision_recall_fscore_support, classification_report
from ast import literal_eval

import subprocess
import sys


subprocess.call([sys.executable, '-m', 'pip', 'install', "sacrebleu"], stderr=subprocess.DEVNULL)

import jaccard
from sacrebleu.metrics import  CHRF
sacrebleu_chrf = CHRF(char_order=6, word_order=0, beta=2, lowercase=False, whitespace=False)


def read_data(input_path: str) -> pd.DataFrame:
    """ read input data; 
        rename columns if whitespace in column; 
        convert statements to nested lists.
    """
    df = pd.read_csv(input_path)
    df = df.rename(columns=lambda x: x.strip()) #  remove whitespace from column headers
    if "statement_spans" not in df.columns:
        df["num_statements"] = np.nan
    df = read_segments(df)
    
    pd.to_numeric(df["num_statements"])
    return df



def read_segments(df: pd.DataFrame) -> pd.DataFrame:
    """ 
        convert string segments to lists
    """
    index_segments = df[~df["statement_spans"].isnull()].index
    try:
        df.loc[index_segments,"statement_spans"] = df.loc[index_segments,"statement_spans"].map(literal_eval)
    except ValueError:
        print("WARNING: wrong data input: lists are not well-formed. Spans will not be evaluated.")
        df.loc[index_segments,"statement_spans"] = np.nan
           
    for i, row in df.iterrows():
        if type(row["statement_spans"]) == list:
            df.at[i,"statement_spans"] = sort_segments(row["statement_spans"])
    return df



def sort_segments(statement_span: list) -> list:
    """
        sort each segment and the list of segments. start with lowest id.
    """
    new_statement_span = list()
    for span in statement_span:
        # sort ids within span
        new_statement_span.append(sorted(span))
    # sort spans in segments
    sorted_list = sorted(new_statement_span, key=lambda lst: lst[0])
    # print(statement_span, new_statement_span, sorted_list, "\n", sep="\n")
    return new_statement_span



def check_data(df_gold: pd.DataFrame, df_pred: pd.DataFrame) -> pd.DataFrame:
    """
         merge gold and predicted data by sent-id to consider shuffled or wrong input data
    """
    
    df_full = pd.merge(df_gold, df_pred, how="outer", on=["sent-id"])

    if len(df_pred) != len(df_gold) or len(df_pred) != len(df_full):
        print(len(df_pred), len(df_gold), len(df_full))
        raise ValueError("wrong data input: data has wrong length")
    
    return df_full


## map integer to string to avoid string overlap between single digits and double digits
## for example str(1) and str(4) would overlap with str(14). 
## but they do not overlap if assigned to unique letters 
## for example 1 (str: B), 4 (str: E) and 14 (str: O). 
output = "{"
for i in range(0,26):
    output += str(i)+': "'+chr(ord('@')+1+i)+'", '
for i in range(1,27):
    output += str(25+i)+': "'+chr(ord('@')+i).lower()+'", '
for i in range(1,250):
    output += str(51+i)+': "'+chr(191+i)+'", '
output += "}"
mapping_int2chr = eval(output)
# print(mapping_int2chr) -> type: dict



def int2chr(segment: list, mapping_dict=mapping_int2chr, concat=False) -> list:
    "replacing an integer with a unique letter based on a mapping_dict"
    new_segment = list()
    for span in segment:
        if concat:
            new_span = str()
            for n in span:
                new_span += mapping_dict[n]
        else:
            new_span = list()
            for n in span:
                new_span.append(mapping_dict[n])
            
        new_segment.append(new_span)
    return new_segment


def add_span_scores(df: pd.DataFrame, mapping_dict=mapping_int2chr):
    """ 
        Scorer for Subtask 2: Segementing Spans of Statements.
        Calculates a score per gold data item where the number of statements is greater than 1 (and the prediction != 0).
        Calculating chrf and jaccard similarity. The scores are added in new columns.
        The more similar the spans, the higher the scores. Th best score is 1, if the spans are identical.
    """   
    data_segments = df[~df["statement_spans_x"].isnull()]
    data_segments["chrf"] = np.nan
    data_segments["chrf_concat"] = np.nan
    data_segments["jaccard_robust"] = np.nan
    data_segments["jaccard_robust_str_concat"] = np.nan
    
    data_segments["statement_spans_x_str"] = np.nan
    data_segments["statement_spans_y_str"] = np.nan
    data_segments["statement_spans_x_str_concat"] = np.nan
    data_segments["statement_spans_y_str_concat"] = np.nan

    for i, row in data_segments.iterrows():
        # print(i, row["num_statements_x"], row["num_statements_y"], row["statement_spans_x"], row["statement_spans_y"])
        
        if row["num_statements_y"] == 1 and row["num_statements_x"] != 1:
            data_segments.loc[i, "chrf"] = 0
            data_segments.loc[i, "jaccard_robust"] = 0
            data_segments.loc[i, "chrf_concat"] = 0
            data_segments.loc[i, "jaccard_robust_str_concat"] = 0
        elif row["num_statements_y"] == 0 and row["num_statements_x"] != 1:
            data_segments.loc[i, "chrf"] = 0
            data_segments.loc[i, "jaccard_robust"] = 0
            data_segments.loc[i, "chrf_concat"] = 0
            data_segments.loc[i, "jaccard_robust_str_concat"] = 0
        elif (row["num_statements_x"] > row["num_statements_y"]) or (row["num_statements_x"] <= row["num_statements_y"]):
            str_span_gold = str(int2chr(row["statement_spans_x"], mapping_dict))
            str_span_prediction = str(int2chr(row["statement_spans_y"], mapping_dict))
            str_span_gold_concat = str(int2chr(row["statement_spans_x"], mapping_dict, concat=True))
            str_span_prediction_concat = str(int2chr(row["statement_spans_y"], mapping_dict, concat=True))
            
            data_segments.loc[i, "statement_spans_x_str"] = str_span_gold
            data_segments.loc[i, "statement_spans_y_str"] = str_span_prediction
            data_segments.loc[i, "statement_spans_x_str_concat"] = str_span_gold_concat
            data_segments.loc[i, "statement_spans_y_str_concat"] = str_span_prediction_concat
            
            chrf_result = sacrebleu_chrf.corpus_score([str_span_gold], [[str_span_prediction]])
            chrf_result_concat = sacrebleu_chrf.corpus_score([str_span_gold_concat], [[str_span_prediction_concat]])
            jaccard_result = jaccard.robust_multiset_jaccard_similarity(row["statement_spans_x"], row["statement_spans_y"])
            jaccard_result_str_concat = jaccard.robust_multiset_jaccard_similarity(str_span_gold_concat, str_span_prediction_concat)

            data_segments.loc[i, "chrf"] = chrf_result.score/100
            data_segments.loc[i, "chrf_concat"] = chrf_result_concat.score/100
            data_segments.loc[i, "jaccard_robust"] = jaccard_result
            data_segments.loc[i, "jaccard_robust_str_concat"] = jaccard_result_str_concat

        else:
            print("todo:", row["num_statements_x"], row["num_statements_y"])
    return data_segments


def get_span_scores(df: pd.DataFrame, mapping_dict=mapping_int2chr) -> tuple:
    """
        add the score columns and return the mean value per score
    """
    print(len(df[~df["statement_spans_y"].isnull()]))
    if len(df[~df["statement_spans_y"].isnull()]) == 0:
        return 0, 0
    else:
        data_segments = add_span_scores(df, mapping_dict)
        return data_segments["chrf_concat"].mean(), data_segments["jaccard_robust"].mean(), 
    

    
def score_task_1(full_data: pd.DataFrame) -> tuple:
    """
        scoring for subtask 1 (Identifying Number of Statements):
        using mean absolute error and mean squared error.
    """
    truth = full_data[["num_statements_x"]]
    prediction = full_data[["num_statements_y"]]

    print('Checking Mean Absolute Error')
    mae = mean_absolute_error(truth, prediction)
    print('Checking Mean Squared Error')
    mse = mean_squared_error(truth, prediction)
    
    return mae, mse


def score_task_2(full_data: pd.DataFrame, mapping_int2chr=mapping_int2chr) -> tuple:
    """
        scoring for subtask 2 (Identifying Segements of Statements):
        using precision, recall and F1 for matching of number of statements
        using CHaRacter-level F-score (chrF) and jaccard similarity for scoring segments of statements
    """
    truth = full_data[["num_statements_x", "statement_spans_x"]]
    prediction = full_data[["num_statements_y", "statement_spans_y"]]
    labels = list(set(truth["num_statements_x"]))

    print("Calculating Precision, Recall & F1")
    precision, recall, f1, support = precision_recall_fscore_support(truth["num_statements_x"], 
                                                                     prediction["num_statements_y"], 
                                                                     labels=labels, 
                                                                     average="weighted")
    print("Calculating ChrF and jaccard similiarty")
    sacrebleu_chrf = CHRF(char_order=6, word_order=0, beta=2, lowercase=False, whitespace=False)
    # chrf = evaluate.load("chrf")
    chrf_value, jaccard_value = get_span_scores(full_data, mapping_int2chr)

    return precision, recall, f1, chrf_value, jaccard_value


def score_both_tasks(full_data: pd.DataFrame, mapping_int2chr=mapping_int2chr) -> dict:
    """ combining the scoring for both subtasks."""
    mae, mse = score_task_1(full_data)
    precision, recall, f1, chrf_value, jaccard_value = score_task_2(full_data, mapping_int2chr=mapping_int2chr)
    scores = {
        # 'accuracy': accuracy,
        'mae': mae,
        'mse': mse,
        'P': precision,
        'R': recall,
        'F1': f1,
        'chrf': chrf_value,
        'jaccard': jaccard_value,
    }
    return scores
