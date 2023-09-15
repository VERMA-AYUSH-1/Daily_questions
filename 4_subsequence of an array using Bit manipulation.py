def sebseq(s,n):
    for i in range((2**n)):
        st=""
        for j in range(n):
            if (i & (1<<j)):
                st+=s[j]

        print(st)


    
if __name__=="__main__":
    # s=[3,1,2]
    s="AYUSH"
    n=len(s)

    sebseq(s,n)


def print_subsequences(arr):
    n = len(arr)
    for i in range(1 << n):  # Iterate through all possible subsets
        subset = []
        for j in range(n):
            if (i & (1 << j)) > 0:
                subset.append(arr[j])
        print(subset)

if __name__ == "__main__":
    arr = [3, 1, 2]
    arr="AYUSH"
    print_subsequences(arr)
