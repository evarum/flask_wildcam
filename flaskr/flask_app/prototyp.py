zahlen = [1,2,3,4,5,7,8,9]
k_zahlen = [1.1,2.1,3.1,4.1,5.1,6.1,7.1,9.1]
zahlen.sort()
k_zahlen.sort()
# print(zahlen)
# print(k_zahlen)
# paar =[]
# print(paar)
# two sorted lists are compared and written down if they fullfill the following condition: lower_limit <= element_between < upper_limit
def paar_sort(list1, list2):
    # limits_list sets the borders of possible placement for elements of liste_between
    limits_list = list1
    liste_between = list2
    paar = []
    # iteration through limits_list
    for lower_limit in limits_list:
       # print(lower_limit)
        for element_between in liste_between:
            # is element_between bigger/equal than the lower_limit?
            if element_between >= lower_limit:
                # defining upper_limit
                upper_limit = lower_limit+1
                # is element_between bigger than the upper_limit?
                if element_between > upper_limit:
                    # exit loop and go to next element_between
                    break
                # appending lower_limit and element_between to list paar
                paar.append([lower_limit,element_between])
    print(paar)
    # giving back the finished sets
    return paar

paar_sort(zahlen, k_zahlen)