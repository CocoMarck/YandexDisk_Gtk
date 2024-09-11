import os
import platform
import subprocess
from logic.Modulo_Text import (
    Text_Read,
    Ignore_Comment,
    Text_Separe
)


def get_system():
    '''Para obtener el sistema operativo utilizado'''

    system = platform.system()
    if system == 'Linux':
        return 'linux'
    elif system == 'Windows':
        return 'win'
    else:
        return 'linux'


system=get_system()


def CleanScreen():
    '''Limpiar la texto de la terminal'''

    if system == 'linux':
        os.system('clear')
    elif system == 'win':
        os.system('cls')
    else:
        os.system('clear')


def ShowArchive(glob=None):
    '''Muestra los archivos existentes.'''

    if type(glob) is str:
        glob = f' {glob}'
    else:
        glob = ''

    if system == 'linux':
        os.system(f'ls{glob}')
    elif system == 'win':
        os.system(f'dir{glob}')
    else:
        os.system(f'ls{glob}')
        

def View_echo(text=None):
    '''Para obtener las funciones de echo, sirve para obtener el resultado de las variables existentes del sistema operativo'''
    if (
        system == 'linux' or
        system == 'win'
    ):
        if type(text) is str:
            text = subprocess.check_output(
                f'echo {text}',
                shell=True,
                text=True
            ).replace('\n', '')
        else:
            pass
        
    else:
        pass

    return text


def Command_Run(
    cmd='echo', open_new_terminal=True,
    text_input='Press ENTER for continue'
):
    '''Se encarga de abrir una consola/terminal y ejecutar un comando especificado'''
    # Establecer que el comando solicitado, no tenga saltos de linea.
    # Y si tiene seran reemplzandolos por un espacio
    cmd.replace('\n', ' ')
    
    # Verificar el sistema operativo utilizado
    if system == 'linux':
        # Establecer que el string sera una comilla simple
        # Y que el comando al terminar tendra una pausa tipo input, y despues se cerrara.
        string = "'"
    
    elif system == 'win':
        # Establecer que el string sera una comilla doble
        # Y que el comando al terminar tendra una pausa tipo input, y despues se cerrara.
        string = '"'
        
    cmd = cmd.replace("'", '"')
    
    # Si queire abrir una nueva terminal
    if open_new_terminal == True:
        # Importar ruta de archivo de comando de ejecucion
        from data.System_data import terminal_run

        # Abrir una terminal nueva
        if system == 'linux':            
            cmd = (
                cmd + ' && '
                f'read -rsp $"{text_input}..." -n 1 key'
            )
        elif system == 'win':
            cmd = (
                cmd + " & pause"
            )

        text_terminal = Ignore_Comment(
            text=Text_Read(
                terminal_run,
                'ModeText'
            ),
            comment='#'
        )
        text_terminal = Text_Separe(
            text=text_terminal,
            text_separe='='
        )
        text_terminal = text_terminal[system]
        
        cmd = f'{text_terminal} {string}{cmd}{string}'
        print(cmd)
        os.system(cmd)

    else:
        # Hacer todo desde la misma terminal/programa
        os.system(cmd)
        input(f'{text_input}...')