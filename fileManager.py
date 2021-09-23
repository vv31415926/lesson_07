from myLibManager import *
import victory as v
import persAccount as pa


if __name__ == '__main__':
    curDir = os.getcwd()   # текущий директорий


    goMenu=True
    while goMenu:
        nMenu = menu()

        if nMenu ==   1:
            inNewDir()
        elif nMenu == 2:
            delDir()
        elif nMenu == 3:
            copyFil()
        elif nMenu == 4:
            viewDir()
        elif nMenu == 5:
            viewOnlyDir()
        elif nMenu == 6:
            viewOnlyFil()
        elif nMenu == 7:
            infoOS()
        elif nMenu == 8:
            infoMy()
        elif nMenu == 9:
            pa.goGame()
            print('------------------')
        elif nMenu == 10:
            saveDir()
        elif nMenu == 11:
            pa.goGame()
            print('------------------')
        elif nMenu == 12:
            chDir()
            print('------------------')
        elif nMenu == 13:
            goMenu = False
        else:
            print( 'Ошибка выбора!\n-------------')