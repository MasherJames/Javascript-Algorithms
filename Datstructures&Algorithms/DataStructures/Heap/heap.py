import math

'''
Binary heap -  Complete binary tree
    i) Max Heap - The value of the key at the root node is greater
       than all other values below it
    ii) Min Heap - The value of the key at the root node is lesser
        than all other values below it

- Height is log n since it's filled from left to right

Common uses
 - Heap sort, with a O(log n) time complexity
 - Priority Queue (Abstract Data Type)
 - Graph Algorithms

Left Node Index = 2 * parent_node_indx
Right Node Index = 2 * parent_node_indx + 1
Parent Node Index = child_node_indx / 2
Last Layer always starts = Math.floor(number_of_nodes / 2) + 1
'''

def heapify_max(arr_heap, parent_indx, total_nodes):
    left_node_indx = 2 * parent_indx
    right_node_indx = 2 * parent_indx + 1

    largest_value_node_indx = parent_indx

    # Check if the left node is greater than parent
    if left_node_indx < total_nodes and arr_heap[left_node_indx] > arr_heap[largest_value_node_indx]:
        largest_value_node_indx = left_node_indx

    # Check if the right node is greater than the parent
    if right_node_indx < total_nodes and arr_heap[right_node_indx] > arr_heap[largest_value_node_indx]:
        largest_value_node_indx = right_node_indx

    # don't swap if the largest value is the parent index

    if largest_value_node_indx != parent_indx:
        arr_heap[parent_indx], arr_heap[largest_value_node_indx] = arr_heap[largest_value_node_indx], arr_heap[parent_indx]

        heapify_max(arr_heap, largest_value_node_indx, total_nodes)

def heapify_min(arr_heap, parent_indx, total_nodes):

    left_node_indx = 2 * parent_indx
    right_node_indx = 2 * parent_indx + 1

    # Assume root node value is minimum
    smallest_value_node_indx = parent_indx

    # If left child value is minimum than the current, replace it
    if left_node_indx < total_nodes and arr_heap[left_node_indx] < arr_heap[smallest_value_node_indx]:
        smallest_value_node_indx = left_node_indx

    # If right child value is minimum than the current, replace it
    if right_node_indx < total_nodes and arr_heap[right_node_indx] < arr_heap[smallest_value_node_indx]:
        smallest_value_node_indx = right_node_indx

    # Enter this block if a new minimum is found
    if smallest_value_node_indx != parent_indx:
        arr_heap[parent_indx], arr_heap[smallest_value_node_indx] = arr_heap[smallest_value_node_indx], arr_heap[parent_indx]

        heapify_min(arr_heap, smallest_value_node_indx, total_nodes)


def building_max_heap(arr):
    for i in range(math.floor(len(arr) / 2), 0, -1):
        heapify_max(arr, i, len(arr))

def build_min_heap(arr):
    for i in range(math.floor(len(arr) / 2), 0, -1):
        heapify_min(arr, i, len(arr))
'''
First element in array is None to make the root node index 1
'''
# heap_data = [None, 4, 5, 1, 6, 7, 3, 2]
# building_max_heap(heap_data)
# build_min_heap(heap_data)


def heap_sort(arr):
    '''
     - build min/max heap
     - Swap the value at the root(max value) with the last value in the arr rep the heap
     - heapify the new heap and reducing the heap size by one on each iteration
     - Repeat step 2 and 3
    '''
    arr_size = len(arr)
    building_max_heap(arr)

    # loop from the last element to the second one
    # The first element is sorted by default
    for i in range(arr_size - 1, 1, -1):
        arr[i], arr[1] = arr[1], arr[i]
        heapify_max(arr, 1, i)

arr_to_sort = [None, 4, 3, 7, 1, 8, 5]
heap_sort(arr_to_sort)
print(arr_to_sort)