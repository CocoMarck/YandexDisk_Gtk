import Modulo_Util as Util
from Modulo_GT import Translate as GoogleTranslator
from Modulo_Language import (
    Default_Language,
    Language
)


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