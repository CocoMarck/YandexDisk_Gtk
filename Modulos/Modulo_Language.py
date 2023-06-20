import locale
from . import Modulo_Util as Util
from pathlib import Path as pathlib


lang_dir = './Languages/'


def Default_Language():
    # Obtener lista de languaje default del OS y establecer el lang
    lang_default = locale.getlocale()
    lang_default = lang_default[0]

    # Separar el el texto por _ y establecer el texto de la izq
    lang_default = lang_default.split('_')
    lang_default = lang_default[0]
    
    return lang_default


def Language( lang=Default_Language() ):
    # Leer Archivo languages
    file_text = Util.Ignore_Comment(
        Util.Text_Read(
            file_and_path=f'{lang_dir}Language_en.dat',
            opc='ModeText'
        )
    )
    # Obtener str de languages
    file_dict = Util.Text_Separe(
        text=file_text,
        text_separe='='
    )
    
    # Verificar un language establecido por el archivo - usuario
    if file_dict['set_lang'] == '':
        # Si no hay str, entonces se coloca el dafault
        pass

    elif pathlib(
        f'{lang_dir}Language_{file_dict["set_lang"]}.dat'
    ).exists():
        # Si el existe el archivo de lenguaje
        lang = file_dict['set_lang']

    else:
        # Si es incorrecto, entonces se coloca el default
        pass

    # Verificar que el lang sea español o english
    if pathlib(
        f'{lang_dir}Language_{lang}.dat'
    ).exists():
        # Si existe el lenguage, entonces se sigue
        pass
    else:
        # Si no es existe el lenguaje, entonces sera english.
        #print(lang)
        lang = 'en'
    
    # Agregar str de languages a un dicionario
    if (
        pathlib(f'{lang_dir}Language_{lang}.dat').exists()
    ):
        # Leer Archivo languages - y eliminar comentarios
        file_text = Util.Ignore_Comment(
            Util.Text_Read(
                file_and_path=f'{lang_dir}Language_{lang}.dat',
                opc='ModeText'
            )
        )
        file_text = Util.Ignore_Comment(
            text=file_text,
            comment='set_lang='
        )

        # Diccionario - Obtener str de languages
        file_dict = Util.Text_Separe(
            text=file_text,
            text_separe='='
        )
    
        # Declarar variables, tipo lista, si es necesario
        list_YesNo = []
        for option in (file_dict['YesNo']).split(','):
            list_YesNo.append(option)

        # Agregar al diccionario
        lang_dict = {
            # Opciones
            'option': file_dict[f'option'],
            'exit': file_dict[f'exit'],
            'continue': file_dict['continue'],
            'continue_enter': file_dict['continue_enter'],
            'install': file_dict['install'],
            'select': file_dict['select'],
            'YesNo': list_YesNo,
            'more_info': file_dict['more_info'],
            'set_dir': file_dict['set_dir'],
            'view_cfg': file_dict['view_cfg'],
            'start': file_dict['start'],
            'rec_video': file_dict['rec_video'],
            'rec_audio': file_dict['rec_audio'],
            'mode': file_dict['mode'],
            'set_option': file_dict['set_option'],
            'save_arch': file_dict['save_arch'],
            
            # Finalizando - Completando
            'finalized': file_dict['finalized'],
            'bye': file_dict['bye'],
            'fin_install': file_dict['fin_install'],
            
            # Errores
            'error_admin': file_dict['error_admin'],
            'error_dir': file_dict['error_dir'],
            'error_parameter': file_dict['error_parameter'],
            
            # Ayuda
            'help_wait': file_dict['help_wait'],
            'help': file_dict['help'],
            
            # Solo texto
            'app': file_dict['app'],
            'title': file_dict['title'],
            'lang': file_dict['lang'],
            'dir': file_dict['dir'],
            'ver': file_dict['ver'],
            'name': file_dict['name'],
            'exec': file_dict['exec'],
            'icon': file_dict['icon'],
            'comment': file_dict['comment'],
            'terminal': file_dict['terminal'],
            'categories': file_dict['categories'],
            'wait': file_dict['wait'],
            'text': file_dict['text'],
            'cmd': file_dict['cmd'],
            'cfg': file_dict['cfg'],
            'record': file_dict['record'],
            'reproduce': file_dict['reproduce'],
            'set': file_dict['set'],
            'disp_audio': file_dict['disp_audio'],
            'arch': file_dict['arch'],
            'no_set': file_dict['no_set'],
            'yes_set': file_dict['yes_set'],
            'the_cfg_be': file_dict['the_cfg_be'],
            'are_disp': file_dict['are_disp'],
            'resolution': file_dict['resolution'],
            'quality': file_dict['quality'],
            'fps': file_dict['fps'],
            'cpu_use': file_dict['cpu_use'],
            'set_arch': file_dict['set_arch'],
            'no_arch': file_dict['no_arch'],
            'see_options': file_dict['see_options']
        }
    else:
        pass
    
    return lang_dict


def YesNo(option='yes', lang=Default_Language()):
    # Obtener el primer caracter del texto si o no correspondiente.
    # Y hacerlo sin mayusculas con el metodo lower().
    if option == 'yes':
        # Obtener si
        text = ( (get_text('YesNo'))[0][:1] ).lower()

    elif option == 'no':
        # Obtener no
        text = ( (get_text('YesNo'))[1][:1] ).lower()

    else:
        # Obtener no
        text = ( (get_text('YesNo'))[1][:1] ).lower()
    
    return text


def get_text(text='app'):
    # Declarar variable/diccionario
    lang = Language()
    
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
    text_lang = Util.Text_Read(
        file_and_path=f'{lang_dir}Language_en.dat',
        opc='ModeText'
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
    with open(f'{lang_dir}Language_en.dat', 'w') as text_lang:
        text_lang.write(lang_ready)