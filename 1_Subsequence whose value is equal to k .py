def subsecsum(i,n,ans,arr,summ,k):
    if i==n:
        if summ==k:
            print(ans)
        return 
    ans.append(arr[i])
    summ+=arr[i]
    subsecsum(i+1,n,ans,arr,summ,k)
    summ-=arr[i]
    ans.pop()
    subsecsum(i+1,n,ans,arr,summ,k)



if __name__=="__main__":
    arr=[1,2,1]
    n=len(arr)
    k=2
    ans=[]
    summ=0
    subsecsum(0,n,ans,arr,summ,k)
