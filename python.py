# segment tree

class segment_tree_max_min:
    def __init__(self,n): # n = length of array
        self.length=4*n+1
        self.array=[[0,0] for _ in range(4*n+1)] # array is 1-based
        # [maximum(minimum) , number of occurence]
    
    def max_min(self,i,j,ind,start,end) : # gives the sum of elements in array
        ''' it returns maximum(minimum) of elements and the numder of its occurence from index i to j      # from index i to j  
            ind should be 1
            start should be 1
            end should be the length of array
        '''
        if start > j or i>end : # not overlap
            return([-float('inf'),0])
        if i<=start and j>= end : # the segment in node is compeletly in the segment we want to calculate the sum of
            return  (self.array[ind])
        mid=(start+end) >> 1  # overlaping
        p1=self.max_min(i,j,2*ind,start,mid)
        p2=self.max_min(i,j,2*ind+1,mid+1,end)
        if p1[0] > p2[0] :
            return p1  # if you want the minimum you have to return p2
        elif p1[0] < p2[0] :
            return p2  # if you want the minimum you have to return p1
        return([p1[0],p1[1]+p2[1]])
    
    def replace(self,i,val,ind,start,end):
        ''' it changes the value at index i to  val
            ind should be 1
            start should be 1
            end should be the length of array
        '''
        if ind > self.length :  # we have reached the leaf
            return
        if self.array[ind][0] < val :
            self.array[ind]=[val,1]
        elif self.array[ind][0] == val :
            self.array[ind][1]+=1
        mid=(start+end) >> 1
        if  start <= i <= mid :   
            self.replace(i,val,2*ind,start,mid)  # going to the left child
        else:
            self.replace(i,val,2*ind+1,mid+1,end)  # going to the right child

if __name__ == '__main__' :  # just for a test :)

    xxx=segment_tree_max_min(10)
    xxx.replace(6,1,1,1,10)
    xxx.replace(2,10,1,1,10)
    xxx.replace(9,33,1,1,10)
    xxx.replace(5,-4,1,1,10)
    xxx.replace(1,9,1,1,10)
    xxx.replace(10,-76,1,1,10)
    print(xxx.array)
    print(xxx.max_min(1,5,1,1,10))
    print(xxx.max_min(2,5,1,1,10))
    print(xxx.max_min(1,10,1,1,10))
    print(xxx.max_min(4,9,1,1,10))
    print(xxx.max_min(3,4,1,1,10))
    print(xxx.max_min(3,5,1,1,10))
    print(xxx.max_min(7,8,1,1,10))    
    