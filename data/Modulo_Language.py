import locale
from pathlib import Path as pathlib
from logic.Modulo_Text import (
    Text_Read,
    Ignore_Comment,
    Text_Separe
)
from logic.Modulo_Files import(
    Files_List
)
import os, sys


# Establecer el lenguage default del sistema
locale.setlocale(locale.LC_ALL, '')

# Obtén la ruta al directorio actual del script
current_dir = os.path.dirname( os.path.abspath(sys.argv[0]) )

# Construye la ruta a Languages desde el directorio que contiene el módulo
lang_dir = os.path.join(current_dir, 'resources', 'languages')


def Default_Language():
    # Obtener lista de languaje default del OS y establecer el lang
    lang_default = locale.getlocale()
    lang_default = str(lang_default[0])

    # Separar el el texto por _ y establecer el texto de la izq
    lang_default = lang_default.split('_')
    lang_default = lang_default[0]
    
    return lang_default


def Language( lang=Default_Language() ):
    # Leer Archivo languages
    file_text = Ignore_Comment(
        text=Text_Read(
            file_and_path=os.path.join( lang_dir, 'Language_en.dat'),
            option='ModeText'
        )
    )
    # Obtener str de languages
    file_dict = Text_Separe(
        text=file_text,
        text_separe='='
    )
    
    # Verificar un language establecido por el archivo - usuario
    if file_dict['set_lang'] == '':
        # Si no hay str, entonces se coloca el dafault
        pass

    elif pathlib(
        os.path.join( lang_dir, f'Language_{file_dict["set_lang"]}.dat')
    ).exists():
        # Si el existe el archivo de lenguaje
        lang = file_dict['set_lang']

    else:
        # Si es incorrecto, entonces se coloca el default
        pass

    # Verificar que el archivo lang exista
    if pathlib(
        os.path.join( lang_dir, os.path.join( lang_dir, f'Language_{lang}.dat'))
    ).exists():
        # Si existe el lenguage, entonces se sigue
        pass
    else:
        # Si no es existe el lenguaje, entonces sera english.
        #print(lang)
        lang = 'en'
    
    # Agregar str de languages a un dicionario
    if (
        pathlib( os.path.join( lang_dir, f'Language_{lang}.dat') ).exists()
    ):
        # Leer Archivo languages - y eliminar comentarios
        file_text = Ignore_Comment(
            Text_Read(
                file_and_path=os.path.join( lang_dir, f'Language_{lang}.dat'),
                option='ModeText'
            )
        )
        file_text = Ignore_Comment(
            text=file_text,
            comment='set_lang='
        )

        # Diccionario - Obtener str de languages
        file_dict = Text_Separe(
            text=file_text,
            text_separe='='
        )
    
        # Declarar variables, tipo lista, si es necesario
        list_YesNo = []
        for option in (file_dict['YesNo']).split(','):
            list_YesNo.append(option)
            file_dict.update( {'YesNo': list_YesNo} )

        # Agregar al diccionario
        lang_dict = file_dict
    
    return lang_dict


def YesNo(option='yes', lang=Default_Language()):
    # Obtener el primer caracter del texto si o no correspondiente.
    # Y hacerlo sin mayusculas con el metodo lower().
    if option == 'yes':
        # Obtener si
        text = ( (get_text('yes'))[:1] ).lower()

    elif option == 'no':
        # Obtener no
        text = ( (get_text('no'))[:1] ).lower()

    else:
        # Obtener no
        text = ( (get_text('no'))[:1] ).lower()
    
    return text


def get_text(text='app'):
    # Declarar variable/diccionario
    lang = Language()
    
    # Si el texto es si o no
    if text == 'yes':
        # Devolver si
        return (lang['YesNo'])[0]
    elif text == 'no':
        # Devolver no
        return (lang['YesNo'])[1]
    else:
        pass
    
    # Si el texto existe en las key del diccionario
    if text in lang.keys():
        # Devolver el resultado de la key del diccionario
        return lang[text]
    else:
        # No hacer nada, devolver un str 'ERROR'
        return 'ERROR'


def set_lang(set_lang='es'):
    # Archivo de Texto Languages.dat
    # Leer y verificar set_lang
    text_lang = Text_Read(
        file_and_path=os.path.join( lang_dir, 'Language_en.dat'),
        option='ModeText'
    )

    # Establecer lang en el archivo Languages.dat
    lang_ready = ''
    for line in text_lang.split('\n'):
        if line.startswith('set_lang='):
            # Si la linea enpieza con 'set_lang='
            lang_ready += f'set_lang={set_lang}\n'
        else:
            # Solo copiar la linea y añadir el salto de linea
            lang_ready += line + '\n'

    # Eliminar ultimo salto de linea
    lang_ready = lang_ready[:-1]
    with open(os.path.join( lang_dir, 'Language_en.dat'), 'w') as text_lang:
        text_lang.write(lang_ready)


def get_lang():
    # Archivo de Texto Languages.dat
    # Leer y verificar set_lang
    text_lang = Text_Read(
        file_and_path=os.path.join( lang_dir, 'Language_en.dat'),
        option='ModeText'
    )

    # Verificar la exitensia de la linea set_lang=
    lang_ready = ''
    for line in text_lang.split('\n'):
        if line.startswith('set_lang='):
            # Si la linea enpieza con 'set_lang='
            lang_ready = ( line.split('set_lang=') ) [1]
        else:
            # No hacer nada
            pass
    
    # Si un language es nada o no
    if lang_ready == '':
        # Etoncens es el dafault.
        lang_ready = f'default ( {Default_Language()} )'
    else:
        # El lang establecido es correcto.
        pass
            
    return lang_ready


def List_Lang():
    list_lang = Files_List(
        files='Language_*.dat',
        path=lang_dir,
        remove_path=True
    )
    
    list_ready = []
    for text in list_lang:
        text_ready = (
            (text.replace('Language_', '')).replace('.dat', '')
            .replace('/', '').replace('\\', '')
        )
        list_ready.append(text_ready)
    
    return list_ready