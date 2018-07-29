def thirdMax(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls = [None, None, None]
        index = 0
        i = 0
        while i < 3:
            try:
                if i == 0:
                    ls[i] = max(nums)
                    nums.remove(ls[i])
                    i += 1
                    continue
                if(ls[i-1] == max(nums)):
                    nums.remove(max(nums))
                    continue
                ls[i] = max(nums)
                nums.remove(ls[i])
                i += 1
            except:
                break
            
            
        if ls[2] == None:
            return ls[0]
        
        return ls[2]

ls =[2,2,3,1]
thirdMax(ls)
