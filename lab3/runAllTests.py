#napisała Sylwia :c
#Stolen't https://github.com/sy1wi4/graph-algorithms-2020/blob/main/run.py
import os
import pathlib
 


def run(func, directory = "/tests/", ext = ''):
    def fix(path):
        fixed = ''

        for sign in path :
            if sign == '\\' :
                fixed += '/'
            else:
                fixed += sign
            
        return fixed

        
    path = fix(str(pathlib.Path(__file__).parent.absolute()))
    

    path += directory

    failed = 0
    failedList = []
    passed = 0
    for file in os.listdir(path) :
        

        if os.path.splitext(path + file)[1] == ext :
            print (file)
            if func(path + file) is True:
                print (file, "is ok")
                passed += 1
            else:
                print (file, "WRONG !!!!")
                failed +=1
                failedList.append(file)

            print()
    
    print("")
    print("=" *20)
    print("summary:")
    print("passed:", passed)
    print("failed:", failed)

    if failed != 0:
        print("\nlist of failed tests:")
        i = 0
        for failedTest in failedList:
            print(i,failedTest)
            i += 1