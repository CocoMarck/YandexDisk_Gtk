'''Modulo de prueba para usar en mis programas jejej'''

import os, platform, pathlib, subprocess


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
            input(f'Esa opción no existe\n'
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
    CleanScreen()
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

    CleanScreen()
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
        
    else: text_final = 'No existe ese texto'

    return text_final

    
def Command_Run(cmd='dir'):
    '''Se encarga de abrir una consola/terminal y ejecutar un comando espeficificado'''
    if sys == 'win':
        txt = Text_Read('Modulo_Util_Win.dat', 'ModeText')
        smb = '"'
        
        cmd = (
            cmd + " & pause"
        )
        cmd.replace('\n', ' ')
        
    elif sys == 'linux':
        txt = Text_Read('Modulo_Util_Linux.dat', 'ModeText')
        smb = "'"
        
        cmd = (
            cmd + ' &&\n\n' +
            Title('Pause', see=False) +
            'read -rsp $"Press ENTER..." -n 1 key'
        )

    cmd = cmd.replace("'", '"')
    
    line_go = []
    for line in txt.split('\n'):
        if not line.startswith('#'):
            line_go.append(line)
        
    txt = ('\n'.join(line_go)).replace('\n', ' ')
    
    print(f'{txt} {smb}{cmd}{smb}')
    os.system(f'{txt} {smb}{cmd}{smb}')
    #print(f'{txt} execute {cmd}')
    #subprocess.Popen([txt, '-e', cmd], stdin=subprocess.PIPE)