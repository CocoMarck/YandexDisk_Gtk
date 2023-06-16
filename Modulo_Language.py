import locale
import Modulo_Util as Util


def Default_Language():
    # Obtener lista de languaje default del OS y establecer el lang
    lang_default = locale.getdefaultlocale()
    lang_default = lang_default[0]

    # Separar el el texto por _ y establecer el texto de la izq
    lang_default = lang_default.split('_')
    lang_default = lang_default[0]
    
    return lang_default


def Language( lang=Default_Language() ):
    # Leer Archivo languages
    file_text = Util.Ignore_Comment(
        Util.Text_Read(
            file_and_path='./Languages.dat',
            opc='ModeRead'
        )
    )
    # Obtener str de languages
    file_dict = Util.Text_Separe(
        text=file_text,
        text_separe='='
    )
    
    # Verificar un language establecido por el archivo - usuario
    if file_dict['set_lang'] == '':
        # Si no hay str, entonces se coloca el default
        pass

    elif (
        file_dict['set_lang'] == 'es' or
        file_dict['set_lang'] == 'en'
    ):
        # Si el str es correcto, establece en la app
        lang = file_dict['set_lang']

    else:
        # Si es incorrecto, entonces se coloca english
        lang = 'en'

    # Verificar que el lang sea español o english
    if (
        lang == 'es' or
        lang == 'en'
    ):
        pass
    else:
        # Si no es español o english, entonces sera enlgish.
        #print(lang)
        lang = 'en'
    
    # Agregar str de languages a un dicionario
    if (
        lang == 'es' or
        lang == 'en'
    ):
        # Formato, es_opcion - en_opcion
        lang=f'{lang}_'
        
        # Declarar variables, tipo lista, si es necesario
        list_YesNo = []
        for option in (file_dict[f'{lang}YesNo']).split(','):
            list_YesNo.append(option)

        # Agregar al diccionario
        lang_dict = {
            # Opciones
            'option': file_dict[f'{lang}option'],
            'exit': file_dict[f'{lang}exit'],
            'continue': file_dict[f'{lang}continue'],
            'continue_enter': file_dict[f'{lang}continue_enter'],
            'install': file_dict[f'{lang}install'],
            'select': file_dict[f'{lang}select'],
            'YesNo': list_YesNo,
            'more_info': file_dict[f'{lang}more_info'],
            'set_dir': file_dict[f'{lang}set_dir'],
            
            # Finalizando - Completando
            'finalized': file_dict[f'{lang}finalized'],
            'bye': file_dict[f'{lang}bye'],
            'fin_install': file_dict[f'{lang}fin_install'],
            
            # Errores
            'error_admin': file_dict[f'{lang}error_admin'],
            'error_dir': file_dict[f'{lang}error_dir'],
            'error_parameter': file_dict[f'{lang}error_parameter'],
            
            # Ayuda
            'help_wait': file_dict[f'{lang}help_wait'],
            
            # Solo texto
            'app': file_dict[f'{lang}app'],
            'title': file_dict[f'{lang}title'],
            'lang': file_dict[f'{lang}lang'],
            'dir': file_dict[f'{lang}dir'],
            'ver': file_dict[f'{lang}ver'],
            'name': file_dict[f'{lang}name'],
            'exec': file_dict[f'{lang}exec'],
            'icon': file_dict[f'{lang}icon'],
            'comment': file_dict[f'{lang}comment'],
            'terminal': file_dict[f'{lang}terminal'],
            'categories': file_dict[f'{lang}categories'],
            'wait': file_dict[f'{lang}wait'],
            'text': file_dict[f'{lang}text'],
            'cmd': file_dict[f'{lang}cmd']
        }
    else:
        pass
    
    return lang_dict