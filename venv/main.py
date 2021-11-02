import sys
sys.path.insert(0, 'C:\\Users\\meyap\\PycharmProjects\\RospyAI\\MainCore')
sys.path.insert(0, 'C:\\Users\\meyap\\PycharmProjects\\RospyAI\\TGbot')
from maincode import * # import module
from botmainc import *
from time import sleep as sl
from guipass import *
from update_check import *
#a = 100
# ___________________________________________________________________________________________
def hello():
    print(' \n'*20)
    print('*******************************************************************************')
    print('*******************************************************************************')
    print('----------RospyAI. ALfA V.0.0.1~~      Development of the MPDF inc.------------')
    print(' ')
    sl(0.4)
    print('----------In collaboration with: ')
    print(' ')
    print('GOOGLE')
    print('IBM')
    print('CloudMinds')
    print('Facebook')
    print(' ')
    print(' ')
    print('********************************************************************************')
    print('********************************************************************************')
    sl(3)
    print(' \n' * 20)
    sl(2)
def starting():    # starting output module
    print(' ')
    print('RospyAI\\MainCore\\main.py: ')
    print('STARTING...')
    print('*'*30)
    sl(1.3)
def starting_help1():
    print('STARTED...')
    print(' ')
    print(' ')
    print('Waiting for commands...')
    print(' ')
    sl(1.5)
# ****************************************************************
def main_console():
    while True:
        print(' ')
        print('_________________________________________________')
        print(' ')
        geting_console_com = input('CONSOLE:~# ')
        print(' ')
        print('LOG(com):',geting_console_com)
        if geting_console_com == 'help':
            print(' ')
            print('help - for help.')
            print('start - for open start info.')
            print('shutdown - for shutdown')

        elif geting_console_com == 'start':
            print(' ')
            print('start-ai --> for start main core.')
            print('start-rospy --> for start all services.')
            print(' ')

        elif geting_console_com == 'shutdown':
            #break
            exit(0)

        elif geting_console_com == 'start-ai':
            print('STARTING: MainCore ')
            start_main()

        elif geting_console_com == 'start-rospy':
            print(' ')
            print('STARTING: ALL SERVICES OF RospyAi...')
            sl(1)
            print('STARTING: RospyAI MainCore...')
            sl(0.5)
            start_main()
            print('RospyAI MainCore...')
            sl(0.5)
            print('STARTED...')
        elif geting_console_com == 'info':
            print(' ')
            print(' ')
            print(' ')
        else:
            print(' ')
            print('**********************************')
            print('UNKNOWN COOMAND USE help FOR HELP.')
            print('**********************************')

def func_start():
    upd_check_mod()
    
    gui_pass_main()

    hello()     # hello module

    starting() # starting output module

    starting_help1() # start help module1

    main_console()


# *********************************************************
func_start() # start starting

