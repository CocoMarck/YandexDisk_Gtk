from logic.Modulo_System import(
    CleanScreen,
    Command_Run
)
from data import Modulo_YandexDisk as YD
from interface.Modulo_ShowPrint import (
    Title,
    Separator,
    Continue,
)
from data.Modulo_Language import (
    YesNo as LangYN,
    get_text as Lang
)
import os


def Menu_YandexDisk():
    # Iniciar loop, si loop es True
    loop = True
    while loop == True:
        CleanScreen()
        # Menu de opciones, y input de opcion
        Title(f'Yandex Disk')
        print(
            f"1. {Lang('login')}\n"
            f"2. {Lang('connect_status')}\n"
            f"3. {Lang('stop')} / {Lang('start')}\n"
            f"4. {Lang('help')}\n"
            f"0. {Lang('exit')}\n"
        )
        option = input(f"{Lang('set_option')}: ")
        
        # Opcion elegida
        cmd = None
        if option == '0':
            # Salir del loop, y por lo tanto del programa
            loop = False
        elif option == '1':
            cmd = YD.token()
        elif option == '2':
            cmd = YD.status()
        elif option == '3':
            cmd = start_or_stop()
        elif option == '4':
            # Ayuda del programa
            cmd = YD.help()
        else:
            Continue(
                text=option,
                message_error=True
            )
        
        # Si el comando esta listo.
        if type(cmd) is str:
            # Visual de continuar o no
            CleanScreen()
            print(
                f'{Lang("cmd")}:\n'
                f'{cmd}\n'
            )
            option = Continue()
            
            # Opcion elegida
            if option == LangYN('yes'):
                CleanScreen()
                Command_Run(
                    cmd=cmd,
                    open_new_terminal=False,
                    text_input=f"{Lang('continue_enter')}..."
                )
            elif option == LangYN('no'):
                pass
            else:
                pass
        else:
            pass
    
    print(Lang('bye'))


def start_or_stop():
    # Menu, parte visual de seleccion de opcion
    CleanScreen()
    Title('Yandex Disk')
    print(
        f'1. {Lang("start&sync")}\n'
        f'2. {Lang("stop")}'
    )
    option = input(f"{Lang('set_option')}: ")
    
    # Opcion elegida
    cmd = ''
    if option == '1':
        cmd = f'{YD.start()} && {YD.sync()}'
    elif option == '2':
        cmd = YD.stop()
    else:
        cmd = 'echo'
    
    return cmd


if __name__ == '__main__':
    Menu_YandexDisk()