def matrixAddSub(matrices,oprt):
    """
    This is a function to add or substract the given array of matrices

    Args:
        matrices: matrices to be operated on as a list
        opr : which operation (add or substract) to be performed, as "-" or "+"

    returns:
        result: Resulting matrix
    """
    finalMatrix = []
    for j in range(len(matrices[0])):
        finalMatrix.append([])
        for k in range(len(matrices[0][0])):
            sum = 0
            for m in range(len(matrices)):
                if(oprt == "+"):
                    sum += matrices[m][j][k]
                else:
                    if(m>0):
                        sum -= matrices[m][j][k]
                    else:
                        sum += matrices[m][j][k]
            finalMatrix[j].append(sum)
    return finalMatrix

def matrixMultiplication(matrices):
    """
    This is a function to multiply the given array of matrices

    Args:
        matrices: matrices to be multiplied as a list

    returns:
        result: Resulting multiplied matrix
    """
    finalMatrix = []
    if len(matrices[0][0])!=len(matrices[1]):
        print("Cannot Multiply")
        finalMatrix = -1
    else:
        for rw in range(len(matrices[0])):
            finalMatrix.append([])
            for clmn in range(len(matrices[1][0])):
                sum = 0
                for val in range(len(matrices[0][0])):
                    sum += matrices[0][rw][val]*matrices[1][val][clmn]
                finalMatrix[rw].append(sum)
    
    return finalMatrix