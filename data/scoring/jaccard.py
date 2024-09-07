from statistics import mean, median
from collections.abc import Collection

def multiset_jaccard_similarity(multiset_true: Collection, multiset_prediction: Collection, sorted_func=max, reverse=False) -> float:
    """calculates the Jaccard Index (https://en.wikipedia.org/wiki/Jaccard_index) for two multisets.
    """

    sum_of_intersection         = 0
    sum_of_union                = 0
    multiset_true_sorted        = sorted(multiset_true, key=lambda x: sorted_func(x), reverse=reverse)
    multiset_prediction_sorted  = sorted(multiset_prediction, key=lambda x: sorted_func(x), reverse=reverse)
    for list_true, list_prediction in zip(multiset_true_sorted, multiset_prediction_sorted):
        set_true                = set(list_true)
        set_prediction          = set(list_prediction)
        sum_of_intersection     += len(set_true.intersection(set_prediction))
        sum_of_union            += len(set_true.union(set_prediction))
    if sum_of_union == 0:
        return 0
    return sum_of_intersection / sum_of_union

def robust_multiset_jaccard_similarity(multiset_true: Collection, multiset_prediction: Collection) -> float:
    """calculates the Jaccard Index (https://en.wikipedia.org/wiki/Jaccard_index) for two multisets.
        In a more robust way. By averaging the results of the following scenario:
            1) sorting by the highest value in the set in ascending order
            2) sorting by the highest value in the set in descending order
            3) sorting by the lowest value in the set in ascending order
            4) sorting by the lowest value in the set in descending order
            5) sorting by the median value in the set in ascending order
            6) sorting by the median value in the set in descending order
    """
    
    return mean( [  multiset_jaccard_similarity(multiset_true, multiset_prediction, sorted_func=max, reverse=False), 
                    multiset_jaccard_similarity(multiset_true, multiset_prediction, sorted_func=max, reverse=True), 
                    multiset_jaccard_similarity(multiset_true, multiset_prediction, sorted_func=min, reverse=False), 
                    multiset_jaccard_similarity(multiset_true, multiset_prediction, sorted_func=min, reverse=True), 
                    multiset_jaccard_similarity(multiset_true, multiset_prediction, sorted_func=median, reverse=False), 
                    multiset_jaccard_similarity(multiset_true, multiset_prediction, sorted_func=median, reverse=True)])
    

    
if __name__ == '__main__':
    print(multiset_jaccard_similarity([[1,2,3], [5,7]], [[1], [5,7]]))
    print(multiset_jaccard_similarity([{1,2,3}, {5}, {7}], [{1}, {5,7}]))
    print(multiset_jaccard_similarity([{1,2,3}, {5}, {7}], [{1}, {5}, {7}]))
    print(robust_multiset_jaccard_similarity([{1,2,3}, {5}, {7}], [{3}, {2,1}, {7}]))
    print(robust_multiset_jaccard_similarity([{1,2,3}, {5}, {7}], [{1}, {2,3}, {7}]))
    print(multiset_jaccard_similarity([{31}, {1}, {8}], [{1}, {31}, {8}]))
    print(robust_multiset_jaccard_similarity([{31}], [{1}, {31}, {8}]))
    print(robust_multiset_jaccard_similarity([{1}, {31}, {8}], [{31}]))
    print(robust_multiset_jaccard_similarity([{1}, {31}, {8}], [{31,8,1}]))
    print(robust_multiset_jaccard_similarity([{1}, {31}, {8}], [{5}]))
