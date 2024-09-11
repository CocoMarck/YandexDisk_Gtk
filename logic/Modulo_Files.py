import os
import shutil
from pathlib import Path as pathlib
from glob import glob
from logic.Modulo_System import (
    get_system,
    View_echo
)


def Path(path='', system=get_system()):
    import subprocess # Por path
    '''Comprobar o hacer que una carpeta termine con su slash correspondiente.'''
    path_fin = ''
    if system == 'linux':
        path_fin = '/'

    elif system == 'win':
        path_fin = '\\'

    else: path = ''

    if path == '':
        if system == 'win':
            path = (os.path.join(os.path.join(os.environ['USERPROFILE']),
                   'Desktop'))
        elif system == 'linux': 
            path = subprocess.check_output(
                'echo $HOME', shell=True, text=True
            ).replace('\n', '')
        else: pass

    try: path_laststr = path[-1]
    except: path_laststr = path_fin
    if path_laststr == path_fin: pass
    else:        
        path = path + path_fin

    return path


def Name(name=''):
    '''Elegir el nombre de un archivo'''
    if name == '':
        name ='No_name'
    else: pass

    return name


def Files_List(files='', path='', remove_path=False):
    '''Te lista los archivos existentes en una ruta espaficada'''
    # Buscar archivos
    search_files = sorted(
        pathlib(path)
        .glob(files)
    )
    
    # Agregar los archivos buscados a una lista
    files_list = []
    for file_text in search_files:
        # Convertir el objeto pathlib a str
        file_text = str( pathlib(file_text) )

        # Remplazar o no el path
        if remove_path == True:
            file_text = file_text.replace(path, '')
        else:
            pass
        
        # Agregar el archivo a la lista de archivos
        files_list.append( file_text )
    
    return files_list


def Files_Copy(source='', destiny=''):
    from distutils.dir_util import copy_tree # Por files copy
    '''Copia archivos a una rota especificada'''
    
    state = 'Copy Ready'
    
    # Detectar si es una carpeta
    if os.path.isdir(source):
        destiny = f'{Path(destiny)}{source}'
        Create_Dir(file_dir=destiny)
        copy_tree(source, destiny)
    # Detectar si es un archivo
    elif os.path.isfile(source):
        shutil.copy(source, destiny)
    else:
        state = None
    
    return state


def Create_Dir(file_dir=''):
    '''Crear una carpeta o varias carpetas'''

    if os.path.isdir(file_dir):
        # Carpeta ya existente, por lo tanto no se creara.
        pass
    
    else:
        # Intentar Crear carpeta, porque no existe
        try:
            # Separador de slash
            if get_system() == 'linux':
                slash = '/'
            elif get_system() == 'win':
                slash = '\\'
            else:
                pass
            
            # Separar Carpetas basado en los slash
            dir_ready = ''
            for text_dir in file_dir.split(slash):
                dir_ready += f'{text_dir}{slash}'
                
                if os.path.isdir(dir_ready):
                    # Si existe la carpeta
                    pass
                else:
                    # Si no existe la carpeta
                    os.mkdir(dir_ready)
        except:
            pass


def Execute_DirectAccess(
        name='',
        version=1.0,
        execute='',
        path='',
        categories=[''],
        comment='',
        icon='',
        terminal=False,
        path_DirectAccess=''
    ):
    '''Para crear un acceso directo.'''
    
    '''Recuerda que el parametro execute, se refiere a la aplicación que quieras ejecutar, por medio del acceso directo.
    
    Y path_DirectAccess, se refiere a la ruta de cración del acceso directo. Podriamos decir que es un parametro opcional, ya que la mayoria de veces, es mejor dejarlo sin llenar.

    Pide como parametros:
    version=float,
    name=str,
    execute=str,
    path=str,
    categories=list[str],
    comment=str,
    icon=str,
    terminal=bool,
    path_DirectAccess=str
    '''
    # Si existe el path y entonces se seguira
    if pathlib(path).exists():
        # Si existe la aplicación, entonces se sigue
        go = True
        
        # Verificar la existencia del nombre
        if name == '':
            name = 'NoName'
        else:
            pass
            
        # Verificar que la version sea un float
        if type(version) is float:
            pass
        else:
            version=1.0
        
        # Verificar que el icono exista
        if pathlib(icon).exists():
            pass
        else:
            icon = ''
            
        # Verificar que las categorias sean una lista
        if type(categories) is list:
            pass
        else:
            categories = ['']
            
        # Verificar que el parametro terminal sea un boleano
        if type(terminal) is bool:
            if get_system() == 'linux':
                # Solo en linux
                if terminal == True:
                    terminal = 'true'
                else:
                    terminal = 'false'
            else:
                pass
        else:
            terminal = False

    else:
        # Si no existe el path y el app no se seguira
        go = False

    
    # Si se cumplen los requisitos, para crear el acceso directo
    if go == True:
        # Poner la lista de categorias en una variable tipo str
        categories_ready = ''
        for categorie in categories:
            categorie = str(categorie)
            categories_ready += categorie
            if categorie == '':
                pass
            else:
                categories_ready += ';'
        categories_ready = categories_ready.replace('\n','')
        
        # Verificar o establecer el path necesario para el acceso directo
        if path_DirectAccess == '':
            if get_system() == 'linux':
                path_DirectAccess = View_echo(
                    text='$HOME/.local/share/applications/'
                )
            elif get_system() == 'win':
                path_DirectAccess = View_echo(
                    '%USERPROFILE%'
                    '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\'
                )
            else:
                pass
        else:
            pass
        if pathlib(path_DirectAccess).exists():
            pass
        else:
            Create_Dir( path_DirectAccess )

        # Texto necesario para el acceso directo
        if get_system() == 'linux':
            type_DirectAccess = '.desktop'
        
            text_DirectAccess = (
                '[Desktop Entry]\n'
                'Encoding=UTF-8\n'
                'Type=Application\n'
                f'Version={version}\n'
                f'Name={name}\n'
                f'Comment={comment}\n'
                f'Icon={Path(path)}{icon}\n'
                f'Exec={execute}\n'
                f'Path={path}\n'
                f'Terminal={terminal}\n'
                f'Categories={categories_ready}'
            )
        elif get_system() == 'win':
            type_DirectAccess = '.vbs'

            if terminal == True:
                with open(f'{Path(path)}{name}.bat', 'w') as text_exec:
                    text_exec.write(
                        '@echo off\n'
                        f'{execute}\n'
                        'pause'
                    )
                execute = f'{name}.bat'

            else:
                pass
        
            text_DirectAccess = (
                # Objeto para acceder a la shell
                'Set objShell = WScript.CreateObject("WScript.SHell")\n\n'

                # Objeto DirectAccess - Crear acceso directo
                'Set objDirectAccess = objShell.CreateShortcut'
                f'("{path_DirectAccess}{name}.Lnk")\n'
                
                # Objeto DirectAccess - Aplicacion a ejecutar
                '    objDirectAccess.TargetPath = '
                f'"{Path(path)}{execute}"\n'
                
                # DirectAccess - Parametro de carpeta de trabajo
                f'    objDirectAccess.WorkingDirectory = "{path}"\n'
                
                # DierctAccess - Parametro de comentario
                f'    objDirectAccess.Description = "{comment}"\n'
                
                # DirectAccess - Parametro de icono
                '    objDirectAccess.IconLocation = '
                f'"{Path(path)}{icon}"\n\n'
                
                # Fin, para guardar el acceso directo
                'objDirectAccess.Save'
            )
        else: pass
            
        
        # Establecer el acceso directo, con el path y el name indicados
        # Tambien darle permisos de ejecución
        DirectAccess = name + type_DirectAccess
        
        if get_system() == 'linux':
            with open(
                path_DirectAccess + DirectAccess,
                'w'
            ) as DirectAccess_ready:
                DirectAccess_ready.write(text_DirectAccess)

            os.system(f'chmod +x "{path_DirectAccess + DirectAccess}"')

        elif get_system() == 'win':
            with open(DirectAccess, 'w') as DirectAccess_ready:
                DirectAccess_ready.write(text_DirectAccess)
        
            os.system(f'"{DirectAccess}"')
            #os.remove(DirectAccess)
        else:
            pass
        
    # Si no se cumple los requisitos, entonces no se hace nada
    else:
        pass