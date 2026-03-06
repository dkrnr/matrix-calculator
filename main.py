print("Matrice Calculator\n")
finalMatrice = []
matrices = []
oprt =  input("Choose an operation (+,-,*):").strip()
i = 1

match oprt:
    case "*":
        while i>0:
            matrix = []
            print(f"\nEnter details for Matrix {i}")
            print("=====================")
            rowCount = int(input(f"enter rows count of matrix {i} (eg :row x column):"))
            columnCount = int(input(f"enter column count of matrix {i} (eg :row x column):"))
            print()
            for j in range(rowCount):
                matrix.append([])
                for k in range(columnCount):
                    value =  int(input(f"Enter values for row {j+1}, column {k+1}:"))
                    matrix[j].append(value)
            matrices.append(matrix)
            print()
            for l in range (len(matrix)):
                print(matrix[l])
            i+=1
            if(i>2):
                break
            if(i>2 and input("\nAdd another Matrix to calculation (n if no):").lower() == "n"):
                break
        
        if len(matrices[0][0])!=len(matrices[1]):
            print("Cannot Multiply")
        else:
            for rw in range(len(matrices[0])):
                finalMatrice.append([])
                for clmn in range(len(matrices[1][0])):
                    sum = 0
                    for val in range(len(matrices[0][0])):
                        sum += matrices[0][rw][val]*matrices[1][val][clmn]
                    finalMatrice[rw].append(sum)

            print("\nThe Final Matrix")
            print("==============")
            for l in range (len(finalMatrice)):
                print(finalMatrice[l])    

    case "+"|"-":

        rowCount = int(input("enter rows count of matrices (eg :row x column):"))
        columnCount = int(input("enter column count of matrices (eg :row x column):"))

        while i>0:
            matrix = []
            print(f"\nEnter details for Matrix {i}")
            print("=====================")
            for j in range(rowCount):
                matrix.append([])
                for k in range(columnCount):
                    value =  int(input(f"Enter values for row {j+1}, column {k+1}:"))
                    matrix[j].append(value)
            matrices.append(matrix)
            print()
            for l in range (len(matrix)):
                print(matrix[l])
            i+=1
            if(i>2 and input("\nAdd another Matrix to calculation (n if no):").lower() == "n"):
                break

        for j in range(rowCount):
            finalMatrice.append([])
            for k in range(columnCount):
                sum = 0
                for m in range(len(matrices)):
                    if(oprt == "+"):
                        sum += matrices[m][j][k]
                    else:
                        if(m>0):
                            sum -= matrices[m][j][k]
                        else:
                            sum += matrices[m][j][k]
                finalMatrice[j].append(sum)

        print("\nThe Final Matrix")
        print("==============")
        for l in range (len(finalMatrice)):
            print(finalMatrice[l])

    case _:
        print("Invalid Operator")
