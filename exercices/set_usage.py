from typing import List
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int])-> bool:
        counter_  = Counter(arr)
        return len(set(list(counter_.values()))) == len(list(counter_.values()))


        