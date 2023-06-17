from Modulo_Util import (
    Text_Read,
    Path,
    Title,
    Separator
)
#from Modulo_ShowPrint import (
#    Title,
#    Separator
#)
from deep_translator import GoogleTranslator
import os


def Translate(
        language_input = None,
        language_output = None,
        input_text = None,
        output_text = None,
        text_only = None,
        id_input = None,
        id_output = None,
        print_mode = True,
    ):
    # Alistar Objeto de Traduccion
    if (
        type ( language_input ) is str and
        type ( language_output ) is str
    ):
        # Si los lengujes son str
        try:
            # Objeto Traducir
            translator = GoogleTranslator(
                source=language_input,
                target=language_output
            )
        except:
            # Parametros para objeto traducir, erroneos
            translator = None

    else:
        # Los languages, no son str, por lo tanto, no es nada
        translator = None
        #print('ERROR - Lenguage input or output, no detects')

    
    # Verificar que este listo el objeto para traducir texto
    if translator == None:
        # Si el translator no esta correcto.
        print(
            'ERROR - Parameters, not goods'
        )
    else:
        # Empezar a traducir
        if type( input_text ) is str:
            # Si el input_text es un archivo de texto
            try:
                # Traducir input_text
                to_translate = Text_Read(
                    file_and_path=input_text,
                    opc='ModeText'
                )
            except:
                # El input no es un texto.
                to_translate = None
                if os.path.isdir( input_text ):
                    # El input es un directorio
                    try:
                        # Traducir id
                        to_translate = Text_Read(
                            file_and_path=(
                                Path(input_text) +
                                id_input
                            ),
                            opc='ModeText'
                        )
                    except:
                        # No traducir
                        pass
                else:
                    # No traducir
                    pass

        else:
            to_translate = None
            
            try:
                # ID Traducir
                to_translate = Text_Read(
                    file_and_path=id_input,
                    opc='ModeText'
                )
                #output_text = id_output
            except:
                # ID No traducir
                pass
            
            if type( text_only ) is str:
                # --text_only, Traducrir un str
                to_translate = text_only
        

        # Ralizar eventos, de imprimir y/o guardar archivos
        if type( to_translate ) is str:
            # Traduccion hecha
            translate_ready = translator.translate( to_translate )

            # Imprimir o no el texto i y o.
            if print_mode == True:
                if type (text_only) is str:
                    # -t, Si exite el modo solo texto
                    pass
                else:
                    # De lo contrario, mostrar -li y -lo
                    Title(text=language_input)
                    print(to_translate)
                    Separator()
                    Title(text=language_output)
                print(translate_ready)
            else:
                pass
            
            # Zona del output
            try:
                if type( output_text ) is str:
                    if os.path.isdir( output_text ):
                        # Para el ID, Modo ID y dir
                        output_text = Path(output_text) + id_output

                    else:
                        # Traduccion Modo Normal
                        output_text = output_text

                else:
                    # Para el ID, Modo ID sin dir
                    if type( id_output ) is str:
                        output_text = id_output
                    else:
                        output_text = None

                if type (output_text) is str:
                    # Meter traduccion al output
                    with open(output_text, 'w') as text_output:
                        text_output.write(translate_ready)

                    if print_mode == True:
                        Separator()
                        print('Text Saved')
                    else:
                        pass
                else:
                    pass

            except:
                Separator()
                print('ERROR - Output, not good')
            
            return translate_ready

        else:
            print('ERROR - Translating')