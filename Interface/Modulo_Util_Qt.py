from os.path import isfile
from Modulos.Modulo_System import(
    Command_Run
)
from Modulos.Modulo_Text import(
    Text_Read
)
from Modulos.Modulo_ShowPrint import(
    Separator
)
from Modulos.Modulo_Language import Language

from PyQt6.QtWidgets import(
    QWidget,
    QDialog,
    QPushButton,
    QLabel,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout
)


lang = Language()


class Dialog_TextEdit(QDialog):
    def __init__(
        self, parent=None,
        text=f'{lang["text"]}...',
        edit=False
    ):
        super().__init__(parent)
        
        self.setWindowTitle( lang['text'] )
        self.resize(512, 256)
        
        # Verificar si el Text Edit es editable
        if edit == True:
            self.text_file = text
            ReadOnly = False
        else:
            ReadOnly = True
        self.edit = edit
        
        # Verificar si texto, es un archivo
        if isfile(text):
            # Si lo es, el titulo sera el archivo
            self.setWindowTitle(text)
            
            # Si lo es, entonces se leera
            text = Text_Read(
                file_and_path=text,
                option='ModeText'
            )
            self.text_isfile = True
        else:
            # Si no es un texto, no pasa nada.
            self.text_isfile = False
        
        # Contenedor Principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Seccion Vertical 1 - Text Edit
        self.text_edit = QTextEdit(str(text).replace('\n', '<br>'))
        self.text_edit.setReadOnly(ReadOnly)
        vbox_main.addWidget(self.text_edit)
        
        # Seccion Vetical 2 - Boton para salir
        if (
            self.text_isfile == True and
            self.edit == True
        ):
            text_button = lang['save_arch']
        else:
            text_button = lang['exit']
        button_exit_or_save = QPushButton( text_button )
        button_exit_or_save.clicked.connect(self.evt_exit_or_save)
        vbox_main.addWidget(button_exit_or_save)

    def evt_exit_or_save(self):
        if (
            self.text_isfile == True and
            self.edit == True
        ):
            with open(self.text_file, 'w') as archive:
                archive.write( 
                    self.text_edit.toPlainText()
                )
        else:
            pass
        self.close()
        

class Dialog_Command_Run(QDialog):
    def __init__(self, parent=None, cmd='', cfg_file=''):
        super().__init__(parent)
        
        self.setWindowTitle(f"{lang['cmd']} - {lang['exec']}")
        self.setMinimumWidth(512)
        self.setMinimumHeight(256)
        
        self.cmd = cmd
        self.cfg_file = cfg_file
        
        # Contenedor Principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Seccion Vrtical - Label
        label = QLabel(f'{lang["cmd"]}:')
        vbox_main.addWidget(label)
        
        # Seccion Vertical - Text Edit
        text_edit = QTextEdit(str(cmd))
        text_edit.setReadOnly(True)
        vbox_main.addWidget(text_edit)
        
        # Seccion Vertical - Boton Ejecutar comando
        button_cmdRun = QPushButton( lang['exec'] )
        button_cmdRun.clicked.connect(self.evt_command_run)
        vbox_main.addWidget(button_cmdRun)
        
    def evt_command_run(self):
        self.close()
        
        if self.cfg_file == '':
            pass
        else:
            with open(self.cfg_file, 'a') as cfg_file:
                cfg_file.write(self.cmd + f'\n{Separator(print_mode=False)}\n')
                
        Command_Run(
            self.cmd,
            text_input=lang['continue_enter'],
            open_new_terminal=True
        )


class Dialog_Wait(QDialog):
    def __init__(self, parent=None, text=lang['help_wait']):
        super().__init__(parent)
        
        self.setWindowTitle( lang['wait'] )
        self.resize(256, 128)
        
        # Contenedor Pincipal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Label en el medio del dialogo
        hbox = QHBoxLayout()
        vbox_main.addLayout(hbox)

        hbox.addStretch()

        label = QLabel(text)
        hbox.addWidget(label)

        hbox.addStretch()