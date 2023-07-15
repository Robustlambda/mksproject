def binarysearch_algo(sequence,item):
    begin_index=0
    end_index=len(sequence) - 1
    while begin_index < end_index:
        midpoint= begin_index + (end_index  - begin_index) // 2
        
        if(sequence[midpoint] == item):
            print("\n The position of the given element is:",midpoint)
        elif(sequence[midpoint]<item):
            begin_index=midpoint + 1
        elif(sequence[midpoint]>item):
            end_index=midpoint-1
        else:
            print("\n The element is not found in array")
    return None
sequence_a=[1,2,3,4,6,5,7,9,8,10] 
print("\n enter the value to be searched between 1 to 10")
item=int(input("\n enter the search value:"))
print(binarysearch_algo(sequence_a,item))

def bubblesorting_algo(sequence):
    indexing_position = range(0,len(sequence)-1)
    sorted = False
    while not sorted:
        sorted=True
        for i in range(0,indexing_position):
            sorted= True

            for j in range(i+1, indexing_position):
                if sequence[i]<sequence[j]:
                    sorted=False
                else:
                    sequence[i],sequence[j] = sequence[j],sequence[i]
        return sequence
sequence_1 =[1,2,3,5,4,6,10,9,8,7,11,12,13,15,14,16]
print("\n Sorted sequence is:"bubblesorting_algo(sequence_1))

def quicksorting_algo(arr):
    pivot_number=arr.pop()

    largernumber=[]
    smallernumber=[]

    indexing_number=len(arr)-1
    for i in  range(0,indexing_number):
        if arr[i] < pivot_number:
            smallernumber.append(arr[i])
        else:
            larger_number.append(arr[i])
    return smallernumber + pivot_number + largernumber
arr1=[9,5,1,7,3,6,4,8,10,25,36,15]
print("\n sorted arry is:",quicksorting_algo(arr1))

def selectionsorting_algo(arr):
    indexing_position= range(0,len(arr)-1)

    for i in indexing_position:
        min_value=i

        for j in range(i+1,len(arr)-1):
            if arr[j]<arr[min_value]:
                min_value=j
           
        if min_value != i:
            arr[min_value],arr[i+1] = arr[i+1],arr[min_value]
    return arr
arr=[10,9,,8,7,4,5,6,1,2,3]
print(selectionsorting_algo(arr))

def insertionsorting_algo(seq1):
    indexing=range(1,len(seq1)-1)
    indexing_from_zero= range(0,len(seq1)-1)
    for j in indexing_from_zero:
        min_val=j

        for i in indexing:
            if arr[min_val] < arr[i]:
                min_val=i
        else:
            arr[min_val],arr[i] = arr[i],arr[min_val]
    return seq1
arr1=[2,5,8,7,4,1,3,6,9,8]
print(insertionsorting_algo(arr1))

def mergesorting_algorithm(list_a):
    index_one=0
    index_last=len(list_a)-1
    indexing=range(0, len(liat_a)-1)
    mid_value= index_one+index_last / 2

    for i in indexing:
        for j in range(i+1,indexing_last):
            if list_a[i] < list_a[j]:
                list_[i],list_a[j] = list_a[j],list_a[i]
    return list_a
list1=[7,4,1,8,5,2,9,6,3]
print(mergesorting_algorithm(list1))

def security_breaches(name,password,id):
    name_1=name
    passw=password
    id1=id
    i=0
    while i<3:
        if(name_1=="security_manager"):
            if(passw=="123456789"):
                if(id1=="123@$147"):
                    print("welcome")
        else:
            i=i-1
        if i==0:
            print("\n ----------------------------- system override -----------------------------------------")
    return
name=input()
password=input()
id=input()
print(security_breaches(name,password,id))


