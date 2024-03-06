def LinearSearch(arr,n,x):
    for i in range(0,n):
        if(arr[i]==x):
            return i
    return -1

#drive code
if __name__ == "__main__":
    arr=[2,3,5,9]
    x=5
    n=len(arr)

    result = LinearSearch(arr,n,x)
    if(result == -1):
        print("Eliment not found")
    else:
        print("Eliment is found")