
import pandas
import numpy
import argparse

def sanity_check(csv_file: str) -> pandas.DataFrame: 
    annotations_df                          = pandas.read_csv(csv_file)
    annotations_df['sent-id']               = annotations_df['sent-id'].astype(int)
    annotations_df['num_statements']        = annotations_df['num_statements'].astype(int)
    # we both accept 'statement_spans' and 'statement_spans ' as column title
    statement_spans_key                     = 'statement_spans' if 'statement_spans' in annotations_df.keys() else 'statement_spans '
    annotations_df[statement_spans_key]     = annotations_df[statement_spans_key].map(lambda list_string: [] if (isinstance(list_string, float) and numpy.isnan(list_string)) 
                                                                                                        else eval(list_string))
    return annotations_df

if __name__ == '__main__':
    # Example command line call: python .\sanity_check.py -f trial.csv --print_head
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--csv_file", help = "Path to the csv-file", default='trial.csv',type=str)
    parser.add_argument("-head", "--print_head", help = "Flag, whether the head should be printed", action='store_true')
    args = parser.parse_args()

    annotations_df = sanity_check(args.csv_file)
    if args.print_head:
        print(annotations_df.head())
    print('Sanity check was successful. There seem to be no parsing errors.')