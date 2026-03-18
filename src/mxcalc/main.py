from mxcalc import interface as intf

def main():
    while True:
        matrices = []
        i = 1
        print("Matrice Calculator")
        print("==================\n")
        
        oprt =  input("Choose an operation (+,-,*):").strip()
        match oprt:
            case "*":
                intf.matrixMultiplicationHelper(matrices,i)
            case "+"|"-":
                intf.matrixAddSubHelper(matrices,oprt,i)
            case _:
                print("Invalid Operator")

        if(input("\nRepeat this process? (y if yes):").lower() != "y"):
            print("\nExiting system...")
            break  
        

if __name__ == "__main__":
    main()