class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        #find the restaurants in commmon:
        common = []
        for n in list1:
            if n in list2:
                common.append(n)
        
        #calculate the index sum AND create the dictionary with the common items as keys and index_sum as values:
        if common is None:
            return False
        else:
            item_index={}
            for item in common:
                index_sum = list1.index(item)+list2.index(item)
                item_index[item]=index_sum
            
            #find the least-sum items and store them in a list:
            result = []
            for (key,value) in item_index.items(): 
                if value == min(item_index.values()):
                    result.append(key)
            return result
