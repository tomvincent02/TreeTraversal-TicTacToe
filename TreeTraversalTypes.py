#Tree Traversal Types

class Graph_search_methods:

    def __init__(self, graph, name_type):
        self._graph = graph
        self._name_type = name_type
        if name_type == 'pre_order':
            pre_order()
        elif name_type == 'post_order':
            post_order()
        elif name_type == 'in_order':
            in_order()
        else:
            pass

    def pre_order(self, graph, name_type, start_node, desired_node):
        while desired_node != start_node:
            if desired_node < start_node:
                left_node = get_nbr(start_node)[0] #first nbr of start_node since its to the right
                    pre_order(graph, name_type, left_node, desired_node)

            else: #desired_node > start_node
                right_node = get_nbr(start_node)[1]
                pre_order(graph, name_type, right_node, desired_node)

        return 'Found' , desired_node

    def post_order(self, graph, name_type, start_node, desired_node):
        if start_node > desired_node:
            left_node = get_nbr(start_node)[0]
            post_order()

    def in_order(self, graph, name_type):

#practicing insertion_sort

def insertion_sort(lst):
    """
    for item in the lst, check if it is not the first element in the list
        knowing it is not move to second
    while
        evauluate if less than the one before it, if so the lesser one takes the idx of the spot
    return lst
    """
    for idx in range(1,len(lst)): #figure out return (recursion) and indexing
        while lst[idx] > lst[idx - 1]:
            final = lst[:idx-1] + lst[idx] + lst[idx-1] + lst[idx:]
            #lst.append[idx-1](lst[idx]) #change the order of the item
    return final

long = [1,2,1]

print(insertion_sort(long))

def merge_sort(lst):
    """
    divide lst by 2 until all lists are len(1) long
    compare and merge sort
    """
    if len(lst) == 1:
        return lst
    else:
        array = merge_sort(lst[:len(lst)/2])
        array_1 = lst[(len(lst)/2) + 1:]
        return merge_final(array, array_1)

def merge_final(array, array_1):
    """
    :param array: comparing single numbers together and adding to array_2
    :param array_1:
    :return: array_2 whcih should be sorted
    """