import heapq

def heap_Sort(elements):
    heapq.heapify(elements)
    sorted_lst=[]
    
    for i in range(len(elements)):
        sorted_lst.append(heapq.heappop(elements))
    
    return sorted_lst

ele=[12,14,8,7,3,-6,5,2]
x=heap_Sort(ele)
print(x)
