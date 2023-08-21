# fileanme: 1203... leetcode.py
# by: Abhay Gupta
# date: 23-08-21

class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        nums                = [i] * n
        group_lengths       = [0] * m
        no_group            = []
        beforeGroup         = [[]] * n 
        nums_group_lengths  = [[]] * m
        group2              = [[]] * m

        ### PRINT INPUT AS A TABLE
        #print("INPUT")
        # for i in range(n):
        # print(nums[i], group[i], beforeItems[i])
        #print("END"

        # find size of groups and numbers in each group
        for num, group_num in enumerate(group):
            if group_num == -1:
                no_group.append(num)
            else:
                group_lengths[group_num] += 1
                nums_group_lengths[group_num].append(num)

        # fill out group_lengths with blanks based on size
        for c, i in enumerate(group_lengths):
            group_lengths[c] = [-1] * i 

        # add element to group in sorted position
        for c, i in enumerate(beforeItems):  # iterate through before items
            if group[c] > -1:
                # print(group_lengths[group[c]])
                # print(i)

                temp = i.copy()
                for b, j in enumerate(temp):  # find each before item per element
                    if j not in nums_group_lengths[group[c]]:  # if before item isn't supposed to be there
                        beforeGroup[c].append(j)
                        i.remove(j)  # remove before item from list
                        # group_lengths[group[c]].pop()

                # print(i)
                # print(group[c], "len", len(i), i, nums[c])
                # print(group_lengths[group[c]], nums)

                # print(nums[c], len(i))
                group_lengths[group[c]][len(i)] = nums[c]

                check = False
                for d, elem in enumerate(group2[group[c]]):
                    if nums[c] in elem:
                        check = True
                        e = d
                if check == False:
                    group2[group[c]].append([nums[c]])
                    e = len(group2[group[c]]) - 1

                curr = []
                for j in beforeItems[c]:
                    # print("before", j)
                    check = False
                    for elem in group2:
                        for d, elem2 in enumerate(elem):
                            # print(j, elem2, j in elem2)
                            if j in elem2:
                                check = True
                                if d == e:
                                    print("NEED TO FINISH")
                                if d > e:
                                    return []
                    if check == False:
                        curr.append(j)

                # print(curr, group2[group[c]])
                if curr:
                    group2[group[c]] = [curr] + group2[group[c]]


            else:
                # print(i)
                if i:
                    beforeGroup[c] = i

        # print("GG", group2)
        # print(beforeItems)

        now = []
        for i in group2:
            curr = []
            for j in i:
                for c in j:
                    curr.append(c)
            now.append(curr)

        # print("ING", group_lengths)
        # print("now", now)
        group_lengths = now

        # return empty list if elem in group cannot be sorted
        for i in group_lengths:
            for j in i:
                if j == -1:
                    # print("YO MAMA")
                    # print(group_lengths)
                    # print(i)
                    return []

        #############

        [group_lengths.append([i]) for i in no_group]
        output = [[]]
        # print("IG", group_lengths)
        # print("BG", beforeGroup)

        # sort groups
        for c, i in enumerate(beforeGroup):
            for j in group_lengths:
                if nums[c] in j:  # current in j-group
                    flag = False

                    # check if group in output
                    for d, out in enumerate(output):
                        if j in out:
                            flag = True
                            e = d
                    if flag == False:
                        e = d
                        output[-1] += [j]

            # print("out", output)
            curr = []
            for elemB in i:
                for subGroup in group_lengths:
                    if elemB in subGroup:
                        flag = False
                        for d, out in enumerate(output):
                            # print("OUT", elemB, subGroup, out)
                            if subGroup in out:
                                if d == e:
                                    # print("NEED 2 FINISH 2")
                                    for z in group_lengths:
                                        if nums[c] in z:
                                            # print("ZZ", z)
                                            break
                                    # print(out)
                                    # print("out", out[1])
                                    if z in out:
                                        out.remove(z)
                                        # print(out)
                                        output.insert(d + 1, [z])
                                    # print(out)
                                    # return []
                                    # out.remove(z)
                                    # output.insert(d+1, z)
                                    # jprint("THIS", output, d)

                                    # pop group containing [c]
                                    # move group to 1 space right
                                    # print(subGroup)
                                    # print(elemB)
                                    # print(c)

                                if d > e:
                                    # print("DE", d, e, output)
                                    return []
                                flag = True
                        if flag == False:
                            # print("HELLO", subGroup)
                            if subGroup not in curr:
                                curr.append(subGroup)
            if curr:
                flag = False
                for r, x in enumerate(output):
                    for y in x:
                        if nums[c] in y:
                            flag = True
                            break
                    if flag == True:
                        break
                        # print(r, nums[c],output[r])
                # print(curr)
                # print("first", output)
                if r == 0:
                    output = [curr] + output
                else:
                    # print(curr, r)
                    output[r - 1] += curr
                # output = [curr] + output
                # print(output)
                # return

        temp = []
        for out in output:
            for j in out:
                temp.extend(j)

        return temp

# Test Cases
n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3],[],[4],[]]

class_instance = Solution()
class_instance.sortItems(n, m, group, beforeItems)