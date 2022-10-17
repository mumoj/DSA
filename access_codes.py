def solution(l):

    def lucky_threes(l):
        lucky_threes = []
        print("List 0 : " +str(l))
        for i,x in enumerate([num for num in l if num!=0]):

            list1 = []
            if i < len(l)-2: list1 = l[i+1: len(l)]
            print("List 1 : " +str(list1))
            for j,y in enumerate([num for num in list1 if num!=0]):
                if y%x == 0:
                    lucky_three =[x,y]
                    print("Lucky 3 Init" + str(lucky_three))
                    list2 = []
                    if j <= len(list1)-2: list2 = list1[j+1: len(list1)]
                    print("List 2 : " +str(list2))

                    for z in list2:
                        if z%y == 0:
                            lucky_three.append(z)
                            print(lucky_three)
                            lucky_threes.append(lucky_three)
                        else:
                            pass
                else:
                    pass

        return lucky_threes

    count = len(lucky_threes(l))
    if count>0 and count<= 0x7FFFFFFF :
        return count
    else:
        return 0

print(solution(l=[1,1,1]))