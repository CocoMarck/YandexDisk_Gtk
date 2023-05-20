import Modulo_Util as Util
import subprocess, os, pathlib


need = 'yandex-disk'

path = (
    Util.Path() +
    '.config/yandex-disk'
)
    

def help():
    return f'{need} --help'
    

def status():
    return f'{need} status'


def start(dirs=''):
    if dirs == '':
        start = f'{need} start'
    else:
        start = f'{need} start --exclude-dirs={dirs}'
    
    return start
    

def stop():
    return f'{need} stop'


def token():
    return f'{need} token'

    
def sync(opc=''):
    sync = f'{need} sync'

    if opc == 'read':
        sync = f'{sync} --read-only'
    
    else:
        pass

    return sync
    
def setPath(dir_YD=None):
    # Si el Archivo existe
    if pathlib.Path(f'{path}/config.cfg').exists():
        # Leer el archivo config.cfg
        archive = Util.Text_Read(
            file_and_path=f'{path}/config.cfg',
            opc='ModeText'
        )
        
        # Variables a utilizar
        dir_correct = None  # Para obtener dir del archivo config.cfg
        stop_force = False  # Para forzar o no el remplzo del dir del config.cfg
        go = False          # Para indicar que dir_correct es correcto
        mkdir = ''          # Para indicar si se crea o no una carpeta
        
        # Verificar si existe el dir adentro del config.cfg
        for line in archive.split('\n'):
            if line.startswith('dir='):
                dir_correct = line.split('dir=')
                dir_correct = dir_correct[1]

                if pathlib.Path(dir_correct).exists():
                    go = True
                
                else:
                    dir_correct = None
                
            elif line.startswith('#dir='):
                dir_YD = f'{Util.Path()}Yandex-Disk'
                mkdir = f'mkdir {dir_YD} &&'
                
            else:
                pass
        
        # Verificar que exista el path asignado por el usuario        
        # Forzar o no el remplazo del dir adentro del config.cfg
        if pathlib.Path(str(dir_YD)).exists():
            mkdir = f'# La carpeta es "{dir_YD}"'

        elif dir_YD == None:
            if dir_correct == None:
                dir_YD = f'{Util.Path()}Yandex-Disk'
                if pathlib.Path(str(dir_YD)).exists():
                    mkdir = f'# MODO carpeta Default "{dir_YD}"'
                else:
                    mkdir = f'mkdir {dir_YD} &&'
            
            else:
                mkdir = f'# La carpeta es "{dir_correct}"'
                stop_force = True
        else:
            pass
        
        # Remplazar o no el dir adentro del config.cfg
        if (
            dir_correct == dir_YD and go == True or
            stop_force == True
        ):
            file_replace = f'# Ya esta establecido el dir "{dir_correct}"'

        else:
            text = ''
            for line in archive.split('\n'):
                if (
                    line.startswith('#dir=') or
                    line.startswith('dir=')
                ):
                    text += f'dir={dir_YD}\n'
                else:
                    text += line + '\n'
        
            with open(f'Path-Config.txt', 'w') as source_file:
                source_file.write( text[:-1] )
            file_replace = f'cp ./Path-Config.txt "{path}/config.cfg"'

    else:
        file_replace = '# Sin archivo, no se detecto Yandex-Disk'
    
    # Configuracion
    cfg = (
        '# Carpeta\n' + mkdir + '\n\n'
        '# Archivo\n' + file_replace
    )
    
    return cfg