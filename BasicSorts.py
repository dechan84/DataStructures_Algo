# Lets review basic sorts algorithm

class Sorts:
    # Bubble Sort
    # The idea is to sort the values in a list by comparing a pair (the value and the value next to it) until
    # we bubble out the biggest value, the we loop again but the length of the list decrease by 1, so we keep doing
    # this until we have bubble out all the numbers in the list. We need a nested loop and keep track of the value
    # The time complex is O(n^2)
    def bubble_sort(self, list1):
        # Remember we start with all the numbers in the list for the loop then we keep decreasing it when
        # we bubble out one of the value (which in this case would be the biggest from the remaining initial loop)
        for i in range(len(list1)-1, 0, -1):
            for j in range(i):
                if list1[j] > list1[j+1]:
                    temp = list1[j]
                    list1[j] = list1[j+1]
                    list1[j+1] = temp
        return list1
    # Selection Sort
    # We need to define a variable min_index where we are going to have the min value for each cycle, and we keep
    # reducing the loop range after we found a minimum value moved to the min_index, there is a special case
    # when at the start of the loop the min_index contains the min_value
    def selection_sort(self, list1):
        # First we define the loop from 0 to length-1, the idea is that before the last item the list will be sorted
        for i in range (len(list1)-1):
            min_index = i
            # The second loop is going to move the index j to compare it with the values from i, if the conditions
            # are met we change the min_index value to j
            for j in range(i + 1, len(list1)):
                if list1[min_index]>list1[j]:
                    min_index = j
            # If there are no changes and min_index is still the i then we dont do the swap
            if min_index != i:
                temp = list1[i]
                list1[i] = list1[min_index]
                list1[min_index] = temp
        return list1
    # Insertion Sort
    # The idea is to start from the second element and compare to previous element if its smaller, if True then
    # we insert it before the previous element, and keep doing it until we found a value that is smaller than the one
    # we use to compare
    # BIg O analysis: The worst case scenario is O(n^2) because of the nested loop,
    # best case is if we have a list that is almost sorted data, the complexity is O(n) so take that into consideration.
    def insertion_sort(self, list1):
        # ALways start in the second element
        for i in range(1, len(list1)):
            temp = list1[i]
            j = i - 1
            while temp < list1[j] and j > -1:
                list1[j+1] = list1[j]
                list1[j] = temp
                j -= 1
        return list1
    # Merge Sort: The idea is to first breakdown the list into 2 proportional list, then into 4 proportional list, etc.
    # until we have n list of 1 element, then we join pairs of element and sort it, then we join groups of 4 elements,
    # etc until we have a list of the original size which would be easy to sort
    # To start creating the merge sort, we first need to create a helper method that will allow us to merge
    # two list, this method will be called merge
    # Merge: It receives two sorted list, then it will have index i for one list and index j for the other, the idea
    # is that both index values will be comparing each other and the smallest value will be sent to the new list
    # this is done in a loop until one of the list is empty, then we just insert the remainings elements of the other
    # list
    def merge(self, list1, list2):
        combined = []
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                combined.append(list1[i])
                i += 1
            else:
                combined.append(list2[j])
                j += 1
        if i == len(list1):
            for j2 in range(j, len(list2)):
                combined.append(list2[j2])
        for i2 in range(i, len(list1)):
            combined.append(list1[i2])
        return combined
    # Now lets create Merge Sort, first we break the list in half until list of 1 element, then we call Merge to keep
    # merging the mini list in a sorted way, until the len of the new list is the same as the original one.
    # Big O analysis: Space complexity is high because we keep creating lists to breakdown the main list into 1 element
    # this is O(n), in time complexity if we consider an example of a list with 8 elements it took 3 operations to
    # break it down it means O(log n) but when we tried to merge it back again it took us O(n) because we need to loop
    # through each item, considering both stages, we have a time complexity of O(n log n), which is faster than bubble,
    # insert and select sort but use more space complexity compare to them. If we want to sort multiple types of data
    # merge sort is the preferred option.
    def merge_sort(self, list1):
        # First consider the base case, which is when we have the a list with 1 element
        if len(list1) == 1:
            return list1
        # Find the midpoint of the list, if the list is odd we need to round it, we can do it with int
        mid = int(len(list1)/2)
        # Now we create two list, the first one contains the values from zero to mid index
        left = list1[:mid]
        # the second list contains values from mid to the last value of index
        right = list1[mid:]
        # We need to use recursion to keep breaking down the list until 1 element and merge that
        return self.merge(self.merge_sort(left), self.merge_sort(right))
    # Quick Sort: We need to first identify the pivot number(i) which is the reference number to compare,
    # first to compare it with the i+1 number if its bigger then we go to the i+2, if this number is smaller than
    # pivot we swap positions with the first number that was greater than pivot (in this example should
    # be with i+1), we should reach to a point where we have grouped all the numbers that are lower than pivot together
    # and the ones that are bigger than pivot together, then we swap pivot to the position of the last number less than
    # pivot, we should have the lower numbers on the left and the bigger to the right.
    # Now we run the method again for the left and the right group until we have a list of 1 element. After that we
    # should have the list sorted by quick sort.
    # Pivot, lets define first the code for pivot and the respective references to be able to swap the elements until
    # all the less than pivot numbers are grouped to the left and all the greater than pivot numbers are grouped to the
    # right, this is for the first iteration.
    # Big O analysis: Swap has an loop so that is O(n), in the case of quick_sort it has a recursive method that
    # requires at least 3 operations for a list of 8 elements again the same relationship as merge short which is
    # O(log n), in total the time complexity would be O(n log n), this would be for best or average scenario,
    # if we have an already sorted list that is the worst case scenario, it would take pivot to walkthrou all the list
    # and compare this is O(n^2), so we need to be very carefull choosing the sort method based on the input we have

    # Swap function
    def swap(self, mylist, i1, i2):
        temp = mylist[i1]
        mylist[i1] = mylist[i2]
        mylist[i2] = temp
    def pivot(self, mylist, pivot_index, end_index):
        swap_index = pivot_index
        # We start to loop to find the elements to compare with pivot index until the end of list
        for i in range(pivot_index+1, end_index+1):
            # We do swap when we find elements lesser than pivot
            if mylist[i] < mylist[pivot_index]:
                swap_index += 1
                self.swap(mylist, swap_index, i)
        # The last position of swap_index will always be the last lesser number compared to pivot that was swap
        self.swap(mylist, pivot_index, swap_index)
        return swap_index
    # This is the quick sort method using pivot and swap, at the start it receives the index of zero on the left and
    # len(mylist) on right
    def quick_sort_helper(self, mylist, left, right):
        # Base case is defined when left is bigger or equal to right (this happens when we cannot sort anymore and the
        # index left and right are the same)
        if left<right:
            pivot_index = self.pivot(mylist, left, right)
            # After running the first pivot, we have the grouped list and the swap of pivot, we also got the swap_index
            # Now with those values we can recursively run quick_sort until we reach 1 element list
            self.quick_sort_helper(mylist, left, pivot_index-1)
            self.quick_sort_helper(mylist, pivot_index+1, right)
        return mylist
    #Some optimization to the code using the quick_sort_helper
    def quick_sort(self, mylist):
        return self.quick_sort_helper(mylist, 0, len(mylist)-1)















