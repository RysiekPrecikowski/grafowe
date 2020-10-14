
import os
import pathlib
 


def run(func, ext = ''):
    # zmienia format ścieżki windowsowej ('\' -> '/')
    def fix(path):
        fixed = ''

        for sign in path :
            if sign == '\\' :
                fixed += '/'
            else:
                fixed += sign
            
        return fixed

        
    # pathlib.Path(__file__).parent.absolute()  ->  ścieżka do katalogu zawierającego ten konkretny plik

    path = fix(str(pathlib.Path(__file__).parent.absolute()))
    
    # os.listdir(path) -> zwraca listę zawierającą nazwy plików w katalogu z danej ścieżki

    path += "/tests/"

    failed = 0
    failedList = []
    passed = 0
    for file in os.listdir(path) :

        # os.path.splitext(path)[1] zwraca rozszerzenie pliku danego ścieżką
        # print(file, path)
        if os.path.splitext(path + file)[1] == ext :

            # print(func(path + file),"\n")
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