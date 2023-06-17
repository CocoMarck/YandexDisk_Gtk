import locale
import Modulo_Util as Util
from Modulo_GT import Translate as GoogleTranslator


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
        # Si es incorrecto, entonces se coloca el dafault
        pass

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
        file_and_path='./Languages.dat',
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
    with open('./Languages.dat', 'w') as text_lang:
        text_lang.write(lang_ready)


def Translate(
    language_input=Default_Language(),
    language_output='pt'
):
    # Establecer dict-lang por medio del parametro
    lang = Language(language_input)
    
    # Declarar list_text, que obtendra el texto traducido.
    # Obtener el texto, del dicionario lang
    list_text = []
    for text in lang.keys():
        # Verificar que sea un str o una lista.
        if type(lang[text]) is list:
            # Si es una lista, concatenar lista a un str
            # Para que lo puede traducir el GoogleTraductor
            lang_ready = ''
            for text in lang[text]:
                lang_ready += f'{text} . '
                #input(lang_ready)

            # Eliminar ultima estos caracteres: ' . '
            # Modo lista activado
            lang_ready = lang_ready[:-3]
            #input(lang_ready)
            is_list = True

        else:
            # Si es un str, entonces ya esta listo lo demas
            is_list = False
            lang_ready = lang[text]
    
        # Traducir texto obtenido del dict-lang
        try:
            text = GoogleTranslator(
                text_only=lang_ready,
                language_input=language_input,
                language_output=language_output,
                print_mode=False
            )

            # Verificar que el caracter esta listo para ser una lista
            if is_list == True:
                # Sera una lista
                lst = []
                for txt in text.split(' . '):
                    lst.append(txt)
                text = lst

            else:
                # De lo contrario, no se hace nada.
                pass
            
            # Alistar texto
            list_text.append(text)
        except:
            # No hay interet, asi que, se colocara la traduccion local.
            list_text = list( lang.values() )
    
    # Declarar dict que tendra el texto.
    dict_lang = {}
    
    # Contar la cantidad de str que hay en list_text
    total_number = 0
    for text in list_text:
        # Sumar texto
        total_number += 1

    # Añadir key y texto al dict_lang
    # Es -1 porque se enpieza por el cero, y en el for le sumo uno
    number_ready = -1
    for key in lang.keys():
        # Verificar que el number_ready sea igual al numero_total
        # Se le resta al total_number uno porque se cuenta el cero.
        if number_ready == total_number-1:
            pass
        else:
            number_ready += 1

        # Añadir key y texto
        dict_lang.update(
            { key : list_text[number_ready] } 
        )
    
    # Devolver el diccionario listo.
    return dict_lang