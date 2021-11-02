# <h2 class="font_2" style="font-size:28px">ALPHA\0.0.1</h2>
# https://rospyai.wixsite.com/rospy-ai/update-check-mod

# ----------------------------------------------------------------

# ***************************************************************************************************************
def upd_check_mod():
    from time import sleep as sl
    from datetime import datetime
    import urllib.request

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    app_version = 'ALPHA:0.0.1'

    print(' ')
    print('VERSION CHECKING...')
    sl(1)
    print('VERSION CHECKING...')
    sl(1)
    print('VERSION CHECKING...')
    print(' ')
    sl(1)

    global qwerty
    qwerty = False

    f = urllib.request.urlopen("https://rospyai.wixsite.com/rospy-ai/update-check-mod").read()
    c = str(f)
    f3 = open('htmlupdate.txt', 'w')
    f3.write(c)
    f3.close()
    # --------------------------------------------
    w = f'<h2 class="font_2" style="font-size:28px">{app_version}</h2>'
    f3 = open('htmlupdate.txt')
    text = f3.read()
    f3.close()
    c = text.count(w)
    print('_____________________________________________________________________________________')
    global text_up_ch
    if text.count(w) >= 1:
        text_up_ch = 'You using the [ LATEST ] version of RospyAI: '
        qwerty = True
        c = (current_time + ' | LOG: ' + text_up_ch + app_version + '\n')
        f2 = open('up_ch_log.log', 'a')
        f2.write(c)
        f2.close()
        print('You using the [ LATEST ] version of RospyAI:', app_version)
    else:
        text_up_ch = 'You using an [ OUTDATED ] version of RospyAI: '
        c = (current_time + ' | LOG: ' + text_up_ch + app_version + '\n')
        f2 = open('up_ch_log.log', 'a')
        f2.write(c)
        f2.close()
        print(' ')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('You using an [ OUTDATED ] version of RospyAI:', app_version)
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        sl(3)
        print('To continue, press the Enter.')
        print(' ')
        input()
#upd_check_mod()










