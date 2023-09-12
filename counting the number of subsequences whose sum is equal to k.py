def subsecsum(i,n,arr,summ,k):
    if i==n:
        if summ==k:
            return True
        return False
    summ+=arr[i]
    l=subsecsum(i+1,n,arr,summ,k)
    summ-=arr[i]

    r=subsecsum(i+1,n,arr,summ,k)
    return l+r


if __name__=="__main__":
    arr=[1,2,3,1]
    n=len(arr)
    k=3
    summ=0
    print(subsecsum(0,n,arr,summ,k))
