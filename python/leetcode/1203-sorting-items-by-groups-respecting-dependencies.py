class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        nums = [i for i in range(n)]
        in_group = [0 for i in range(m)]
        no_group = []

        #print("INPUT")
        # for i in range(n):
        # print(nums[i], group[i], beforeItems[i])
        #print("END")

        beforeGroup = [[] for i in range(n)]
        elems_in_group = [[] for i in range(m)]

        # find size of groups
        for num, group_num in enumerate(group):
            if group_num == -1:
                no_group.append(num)
            else:
                in_group[group_num] += 1
                elems_in_group[group_num].append(num)

        group2 = [[] for i in range(m)]

        # fill out in_group with blanks based on size
        for c, i in enumerate(in_group):
            in_group[c] = [-1 for j in range(i)]

        # print(in_group)
        # add element to group in sorted position
        for c, i in enumerate(beforeItems):  # iterate through before items
            if group[c] > -1:

                # print(in_group[group[c]])
                # print(i)

                temp = i.copy()
                for b, j in enumerate(temp):  # find each before item per element
                    if j not in elems_in_group[group[c]]:  # if before item isn't supposed to be there
                        beforeGroup[c].append(j)
                        i.remove(j)  # remove before item from list
                        # in_group[group[c]].pop()

                # print(i)
                # print(group[c], "len", len(i), i, nums[c])
                # print(in_group[group[c]], nums)

                # print(nums[c], len(i))
                in_group[group[c]][len(i)] = nums[c]

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

        # print("ING", in_group)
        # print("now", now)
        in_group = now

        # return empty list if elem in group cannot be sorted
        for i in in_group:
            for j in i:
                if j == -1:
                    # print("YO MAMA")
                    # print(in_group)
                    # print(i)
                    return []

        #############

        [in_group.append([i]) for i in no_group]
        output = [[]]
        # print("IG", in_group)
        # print("BG", beforeGroup)

        # sort groups
        for c, i in enumerate(beforeGroup):
            for j in in_group:
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
                for subGroup in in_group:
                    if elemB in subGroup:
                        flag = False
                        for d, out in enumerate(output):
                            # print("OUT", elemB, subGroup, out)
                            if subGroup in out:
                                if d == e:
                                    # print("NEED 2 FINISH 2")
                                    for z in in_group:
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
