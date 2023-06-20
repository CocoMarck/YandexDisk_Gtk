from PyQt6.QtWidgets import(
    QWidget,
    QDialog,
    QPushButton,
    QLabel,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout
)

from Modulos import Modulo_Util as Util
from Modulos.Modulo_Language import Language


lang = Language()


class Dialog_TextEdit(QDialog):
    def __init__(
        self, parent=None, text=f'{lang["text"]}...'
    ):
        super().__init__(parent)
        
        self.setWindowTitle( lang['text'] )
        self.setMinimumWidth(512)
        self.setMinimumHeight(256)
        
        # Contenedor Principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Seccion Vertical 1 - Text Edit
        text_edit = QTextEdit(str(text).replace('\n', '<br>'))
        text_edit.setReadOnly(True)
        vbox_main.addWidget(text_edit)
        
        # Seccion Vetical 2 - Boton para salir
        button_exit = QPushButton( lang['exit'] )
        button_exit.clicked.connect(self.evt_exit)
        vbox_main.addWidget(button_exit)

    def evt_exit(self):
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
                cfg_file.write(self.cmd + f'\n#{Util.Separator(see=False)}\n')
                
        Util.Command_Run(self.cmd)


class Dialog_Wait(QDialog):
    def __init__(self, parent=None, text=lang['help_wait']):
        super().__init__(parent)
        
        self.setWindowTitle( lang['wait'] )
        self.setGeometry(100, 100, 256, 128)
        
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