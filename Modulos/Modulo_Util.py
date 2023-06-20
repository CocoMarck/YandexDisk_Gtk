'''Modulo de prueba para usar en mis programas jejej'''

import os, platform, pathlib, subprocess
import shutil
from distutils.dir_util import copy_tree
from glob import glob


def System(opc = 'System'):
    '''Comandos de sistema utiles (Limpiar pantalla - Verción del Sistema - Mostrar Archivos)'''
    cmd = ''
    if opc == 'System':
        '''Devuelve el sistema operativo'''
        cmd = platform.system()
        if cmd == 'Windows': cmd = 'win'
        elif cmd == 'Linux': cmd = 'linux'
        else: cmd = 'linux' #(Mac)

    elif opc == 'CleanScreen':
        '''Limpia el texto/comandos que se muestren en la terminal'''
        sys = System('System')
        if sys == 'linux':
            os.system('clear')
        elif sys == 'win':
            os.system('cls')
        else: pass

    elif opc == 'ShowArchive':
        '''Muestra los archivos existentes en una ruta'''
        sys = System('System')
        if sys == 'linux':
            os.system('ls')
        elif sys == 'win':
            os.system('dir')
        else: pass


    else: pass


    return cmd




def CleanScreen():
    System('CleanScreen')


sys = System()




def Show(opc = 'Title', txt = '', smb = '#', see = True, spc = 4):
    '''Mostrar un texto predefinido'''
    if opc == 'Title':
        '''Mostrar un titulo'''
        spc = ' '*spc
        txt = f'{smb}{spc}{txt}{spc}{smb}'
        if see == True:
            print(txt)
        elif see == False:
            txt += '\n'
        else:
            pass

    elif opc == 'Separator':
        '''Para separar texto'''
        txt = smb*spc
        if see == True:
            print(txt)
        elif see == False:
            txt += '\n'
        else:
            pass

    else: txt = ''


    return txt

def Title(txt='', smb = '#', see = True, spc = 4):
    txt = Show(opc='Title', txt=txt, smb=smb, see=see, spc=spc)
    return txt




def Separator(smb = '#', see = True, spc = 128):
    txt = Show(opc='Separator', smb=smb, see=see, spc=spc)
    return txt




def Continue(
        txt='¿Continuar?',
        lang = 'español', msg = False,
        sys=sys,
        loop = True
    ):
    idm = ['']*2
    if lang == 'español': idm[0], idm[1] = 's', 'n'
    elif lang == 'english': idm[0], idm[1] = 'y', 'n'
    else: idm[0], idm[1] = '', ''

    opc = ''

    while loop == True:
        if msg == False:
            opc = input(f'{txt} {idm[0]}/{idm[1]}: ')
            System('CleanScreen')

            if (
                opc == 's' or
                opc == 'n'
            ): loop = False

            elif opc == '':
                print('No escribiste nada\n')
                opc = Continue(txt=txt, lang=lang, loop = False)

            else: 
                print(f'"{opc}" No existe\n')
                opc = Continue(txt=txt, lang=lang, loop = False)
        else:
            loop = False
            if txt == '':
                input('Esa opción no existe\n'
                      'Precione enter para continuar...')
            else:
                input(f'No exite la opcion "{txt}"\n'
                      'Precione enter para continuar...')
        
    return opc




def Name(nme=''):
    if nme == '':
        nme ='No_name'
    else: pass
    CleanScreen()
    return nme




def Path(pth='', sys=sys):
#    pth = ''
    pth_fin = ''
    if sys == 'linux':
        pth_fin = '/'

    elif sys == 'win':
        pth_fin = '\\'

    else: pth = ''

    if pth == '':
        if sys == 'win':
            pth = (os.path.join(os.path.join(os.environ['USERPROFILE']),
                   'Desktop'))
        elif sys == 'linux': 
            pth = subprocess.check_output(
                'echo $HOME', shell=True, text=True
            ).replace('\n', '')
        else: pass

    try: pth_laststr = pth[-1]
    except: pth_laststr = pth_fin
    if pth_laststr == pth_fin: pass
    else:        
        pth = pth + pth_fin

    return pth
    

def Archive_Path(txt='Archivo'):
    CleanScreen()
    
    Title(f'Ruta - {txt}')
    cfg = Path(input('Ruta/Carpeta: '))
    
    Title(f'Nombre - {txt}')
    cfg = cfg + Name(input('Nombre/Archivo: '))
    
    return cfg
    

def Text_Read(file_and_path='', opc='ModeList'):
    '''Lee archivos de texto y adjunta la información en una lista, variable o diccionario'''
    text_final = ''

    if pathlib.Path(file_and_path).exists():
        with open(file_and_path, 'r') as file_end:
            text_read = file_end.read()
   
        if (opc == 'ModeTextOnly' or
            opc == 'ModeText'):
            text_final = ''
            for text_line in text_read:
                text_final += text_line
                
            if opc == 'ModeTextOnly':
                text_final = text_final.replace('\n', ' ')

        elif opc == 'ModeDict':
            text_final = {}
            text_read = Text_Read(file_and_path, opc='ModeText')
            nmr = 0
            for line in text_read.splitlines():
                nmr += 1
                text_final.update({nmr : line})
                
        elif opc == 'ModeList':
            text_final = text_read

        else: text_final = text_read
        
    else: text_final = ''

    return text_final
    

def Ignore_Comment(text='Hola #Texto', comment='#'):
    if (
        '\n' in text and
        comment in text
    ):
        # Cuando hay saltos de linea y comentarios
        
        text_ready = ''
        for line in text.split('\n'):
            line = Ignore_Comment(text=line, comment=comment)
            text_ready += f'{line}\n'
            
        text = text_ready[:-1]
        
    elif comment in text:
        # Cuando hay comentarios pero no saltos de linea

        text = text.split(comment)
        text = text[0]
        
    else:
        # No hay nada de comenarios
        pass
        
    return text

    
def Command_Run(cmd='dir'):
    '''Se encarga de abrir una consola/terminal y ejecutar un comando espeficificado'''
    if sys == 'win':
        txt = Text_Read('./data/Modulo_Util_Win.dat', 'ModeText')
        smb = '"'
        
        cmd = (
            cmd + " & pause"
        )
        cmd.replace('\n', ' ')
        
    elif sys == 'linux':
        txt = Text_Read('./data/Modulo_Util_Linux.dat', 'ModeText')
        smb = "'"
        
        cmd = (
            cmd + ' &&\n\n' +
            Title('Pause', see=False) +
            'read -rsp $"Press ENTER..." -n 1 key'
        )

    cmd = cmd.replace("'", '"')
    
    txt = Ignore_Comment(text=txt, comment='#').replace('\n', ' ')
    
    print(f'{txt} {smb}{cmd}{smb}')
    os.system(f'{txt} {smb}{cmd}{smb}')
    #print(f'{txt} execute {cmd}')
    #subprocess.Popen([txt, '-e', cmd], stdin=subprocess.PIPE)
    
    
def Files_List(files='', path='', remove_path=False):
    # Buscar archivos
    search_files = sorted(
        pathlib.Path(path)
        .glob(files)
    )
    
    # Agregar los archivos buscados a una lista
    files_list = []
    for file_text in search_files:
        # Convertir el objeto pathlib a str
        file_text = str( pathlib.Path(file_text) )

        # Remplazar o no el path
        if remove_path == True:
            file_text = file_text.replace(path, '')
        else:
            pass
        
        # Agregar el archivo a la lista de archivos
        files_list.append( file_text )
    
    return files_list
    

def Files_Copy(src='', dst=''):
    '''
    Copia archivos a una ruta especificada
    '''
    
    state = 'Copy Ready'

    # Detectar si es una carpeta
    if os.path.isdir(src):
        dst = f'{Path(dst)}{src}'
        Create_Dir(file_dir=dst)
        copy_tree(src, dst)
    # Detectar si es un archivo
    elif os.path.isfile(src):
        shutil.copy(src, dst)
    else:
        state = 'ERROR - source no exists'
        
    return state

    
def Text_Separe(text='', text_separe='='):
    '''Para separar el texto en 2 y almacenarlo en un diccionario'''

    text_dict = {}
    if (
        '\n' in text and
        text_separe in text
    ):
        # Cuando hay saltos de linea y separador
        for line in text.split('\n'):
            line = Text_Separe(text=line, text_separe=text_separe)
            for key in line.keys():
                text_dict.update( {key : line[key]} )

    elif text_separe in text:
        # Cuando solo hay separador
        text = text.split(text_separe)
        text_dict.update( {text[0] : text[1]} )
    else:
        pass
    
    return text_dict
    
    
def View_echo(text=None):
    if (
        sys == 'linux' or
        sys == 'win'
    ):
        text = subprocess.check_output(
                f'echo {text}',
                shell=True,
                text=True
            ).replace('\n', '')
    else:
        pass

    return text
    

def Create_Dir(file_dir=''):
    if pathlib.Path(file_dir).exists():
        # Carpeta ya existente, por lo tanto no se creara
        pass
        
    else:
        # Intentar Crear carpeta, porque no existe.
        try:
            # Separador de slash
            if sys == 'linux':
                slash = '/'
            elif sys == 'win':
                slash = '\\'
            else:
                pass
                
            # Separar Carpetas basado en los slash
            dir_ready = ''
            for text_dir in file_dir.split(slash):
                dir_ready = f'{dir_ready}{slash}{text_dir}'

                if pathlib.Path(dir_ready).exists():
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
    '''
    Para crear un acceso directo.
    
    Recuerda que el parametro execute, se refiere a la aplicación que quieras ejecutar, por medio del acceso directo.
    
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
    if pathlib.Path(path).exists():
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
        if pathlib.Path(icon).exists():
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
            if sys == 'linux':
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
            if sys == 'linux':
                path_DirectAccess = View_echo(
                    text='$HOME/.local/share/applications/'
                )
            elif sys == 'win':
                path_DirectAccess = View_echo(
                    '%USERPROFILE%'
                    '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\'
                )
            else:
                pass
        else:
            pass
        if pathlib.Path(path_DirectAccess).exists():
            pass
        else:
            Create_Dir( path_DirectAccess )

        # Texto necesario para el acceso directo
        if sys == 'linux':
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
        elif sys == 'win':
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
        
        if sys == 'linux':
            with open(
                path_DirectAccess + DirectAccess,
                'w'
            ) as DirectAccess_ready:
                DirectAccess_ready.write(text_DirectAccess)

            os.system(f'chmod +x "{path_DirectAccess + DirectAccess}"')

        elif sys == 'win':
            with open(DirectAccess, 'w') as DirectAccess_ready:
                DirectAccess_ready.write(text_DirectAccess)
        
            os.system(f'"{DirectAccess}"')
            #os.remove(DirectAccess)
        else:
            pass
        
    # Si no se cumple los requisitos, entonces no se hace nada
    else:
        pass