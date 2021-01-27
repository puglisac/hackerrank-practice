"""
Function Description

Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

matchingStrings has the following parameters:

string strings[n] - an array of strings to search
string queries[q] - an array of query strings
Returns

int[q]: an array of results for each query

>>> matching_strings(['def', 'de', 'fgh'], ['de', 'lmn', 'fgh'])
[1, 0, 1]
"""
def matching_strings(strings, queries):
    strings_counts = {}
    results_arr=[]
    for string in strings:
        if string in strings_counts.keys():
            strings_counts[string]+=1
        else:
            strings_counts[string]=1
    for query in queries:
        if query in strings_counts.keys():
            results_arr.append(strings_counts[query])
        else:
            results_arr.append(0)
    return results_arr
