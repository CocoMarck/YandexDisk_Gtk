import Modulo_Util as Util
import subprocess, os, pathlib


need = 'yandex-disk'

home = subprocess.check_output(
    'echo $HOME', shell=True, text=True
).replace('\n', '')

path = (
    home +
    '/.config/yandex-disk'
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
    
def setPath(dir_YD=''):
    # Carpeta
    if dir_YD == '':
        dir_YD = f'{home}/Yandex-Disk'
    else:
        pass
    
    if pathlib.Path(dir_YD).exists():
        mkdir = f'# La carpeta es {dir_YD}'
    else:
        dir_YD = f'{home}/Yandex-Disk'
        mkdir = f'mkdir {dir_YD} &&'

    # Archivo
    if pathlib.Path(f'{path}/config.cfg').exists():
        archive = Util.Text_Read(
            file_and_path=f'{path}/config.cfg',
            opc='ModeText'
        )
    
        text = ''
        for line in archive.split('\n'):
            if line.startswith('dir='):
                text += f'dir={dir_YD}\n'
            else:
                text += line + '\n'
    
        with open(f'Path-Config.txt', 'w') as source_file:
            source_file.write(text)
        file_replace = f'cp ./Path-Config.txt {path}/config.cfg'
    else:
        file_replace = '# Sin archivo, no se detecto Yandex-Disk'
    
    # Configuracion
    cfg = (
        '# Carpeta \n' + mkdir + '\n\n'
        '# Archivo \n' + file_replace
    )
    
    return cfg