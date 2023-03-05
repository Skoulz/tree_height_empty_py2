def compute_height(n, parents):
    # Write this function
    tree1 = {}
    tree1 = numpy.zeros(n)
    def tree_heigth(i):
        if tree1[i] != 0:
        return tree1[i]

        if parents[i] = -1:
            tree1[i] = 1
        else: 
            tree1[parents[i]].append(i)
       # return tree_heigth[i]


    #max_height = 0
    # Your code here
            for i in range(n);
        tree_heigth(i)
        return int(max(tree1))

    #return max_height


def main():
    # implement input form keyboard and from files
    txt1=input()
    if "I" in txt1:
        n = int(input())
        parents = list(map(int, input().split()))
#     else:
#         print("input error")
    elif "F" in txt1:
        file1=input()
        if 'a' in file1:
            print("wrong input")
            return
        else: 
            with open(str("./test"+file1), 'r', encoding='UTF-8') as fails:
                n = int(fails.readline())
                parents = list(map(int, fails.readline().split()))
    else: 
        print("wrong input")
        print(compute_height(n, parents))


    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision

    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

    #pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))
