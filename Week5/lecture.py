# Complete Binary Tree (CBT) and Operations 

# Create a complete binary tree using lists:
# tree = [[[[1], 6, [3]], 2, [[5], 8, [7]], 7, [[2], 3, [4]], 9, [[6], 5, [8]]]]
tree = [[[7], 1, [9]], 3, [[8], 2, [4]]]

# count number of nodes
def numOfNodes(t):
    if len(t) == 1:
        return 1
    else:
        numLeft = numOfNodes(t[0])
        numRight = numOfNodes(t[2])
        return (numLeft + 1 + numRight)

# calculate sum of nodes
def sumOfNodes(t):
    if len(t) == 1:
        return t[0]
    else:
        sumLeft = sumOfNodes(t[0])
        sumRight = sumOfNodes(t[2])
        return (sumLeft + t[1] + sumRight)

# find max of nodes
def maxOfNodes(t):
    if len(t) == 1:
        return t[0]
    else:
        maxNum = t[1]
        maxL = maxOfNodes(t[0])
        maxR = maxOfNodes(t[2])
        if (maxL > maxNum):
            maxNum = maxL
        if (maxR > maxNum):
            maxNum = maxR
        return maxNum

# find min of nodes
def minOfNodes(t):
    if len(t) == 1:
        return t[0]
    else:
        minNum = t[1]
        minL = minOfNodes(t[0])
        minR = minOfNodes(t[2])
        if (minL < minNum):
            minNum = minL
        if (minR < minNum):
            minNum = minR
        return minNum

# mirror CBT:
def mirrorTree(t):
    if len(t) == 1:
        return t
    else:
        new_treeR = mirrorTree(t[0])
        new_treeL = mirrorTree(t[2])
        return [new_treeL, t[1], new_treeR]
        

print(numOfNodes(tree))
print(sumOfNodes(tree))
print(maxOfNodes(tree))
print(minOfNodes(tree))
print(mirrorTree(tree))