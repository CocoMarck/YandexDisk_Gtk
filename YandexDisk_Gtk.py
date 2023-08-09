from Modulos.Modulo_Text import(
    Text_Read
)
from Modulos.Modulo_System import(
    Command_Run
)
from Modulos import Modulo_YandexDisk as YD
from Interface import Modulo_Util_Gtk as Util_Gtk
from Modulos.Modulo_Language import get_text as Lang
import threading
import pathlib

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Window_Main(Gtk.Window):
    def __init__(self):
        super().__init__(title='Yandex-Disk Gtk')
        self.set_resizable(True)
        self.set_default_size(256, -1)
        
        # Contenedor Principal
        vbox_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        
        # Seccion Vertical 1 - Iniciar sesion
        button_login = Gtk.Button(label=Lang('login') )
        button_login.connect('clicked', self.evt_login)
        vbox_main.pack_start(button_login, True, False, 0)
        
        # Seccion Vertical 3 - Estado-Status
        button_status = Gtk.Button(label=Lang('connect_status') )
        button_status.connect('clicked', self.evt_status)
        vbox_main.pack_start(button_status, True, False, 0)
        
        # Seccion Vertical 2 - Ayuda
        button_help = Gtk.Button(label=Lang('help') )
        button_help.connect('clicked', self.evt_help)
        vbox_main.pack_start(button_help, True, False, 0)
        
        # Seccion Vertical 3 - Iniciar o Parar
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        vbox_main.pack_start(hbox, True, False, 0)
        
        label_start = Gtk.Label(
            label=f'{Lang("stop")} / {Lang("start")}'
        )
        hbox.pack_start(label_start, False, True, 0)
        
        switch_start = Gtk.Switch()
        switch_start.set_active(False)
        switch_start.connect('notify::active', self.evt_start)
        hbox.pack_end(switch_start, False, True, 0)
        
        # Fin, Mostrar contenedor y su contenido
        self.add(vbox_main)
        
    def evt_login(self, widget):
        dialog = Util_Gtk.Dialog_Command_Run(
            self, cfg=YD.token()
        )
        dialog.run()
        dialog.destroy()
        
    def evt_status(self, widget):
        dialog = Util_Gtk.Dialog_Command_Run(
            self, cfg=YD.status()
        )
        dialog.run()
        dialog.destroy()
        
    def evt_help(self, widget):
        dialog = Util_Gtk.Dialog_Command_Run(self, cfg=YD.help())
        dialog.run()
        dialog.destroy()
        
    def evt_start(self, switch, gparam):
        if switch.get_active():
            self.hide()
            dialog_start = Dialog_Start(self)
            dialog_start.run()
            dialog_start.destroy()
            self.show_all()
            #switch.set_active(False) # Para desactivar cuando se cierre.
        else:
            self.thread = threading.Thread(target=self.thread_stop)
            self.thread.start()
            #dialog = Util_Gtk.Dialog_Command_Run(
            #    self, cfg=(YD.stop())
            #)
            #dialog.run()
            #dialog.destroy()
    
    def thread_stop(self):
        Command_Run(
            cmd=(YD.stop()),
            open_new_terminal=True,
            text_input=Lang('continue_enter')
        )


class Dialog_Start(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title = 'Dialog_Start')
        self.set_resizable(True)
        self.set_default_size(308, -1)
        
        # Contenedor Principal
        vbox_main = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=8
        )
        vbox_main.set_property("expand", True)
        
        # Seccion Vertical 1 - Carpeta
        self.text_path = None
        button_path = Gtk.Button(
            label=f"{Lang('set_dir')} / Yandex-Disk"
        )
        button_path.connect('clicked', self.evt_path)
        vbox_main.pack_start(button_path, True, False, 0)
        
        # Seccion Vertical 2 - Carpeta Label
        self.label_path = Gtk.Label()
        vbox_main.pack_start(self.label_path, True, False, 0)
        
        # Seccion Vertical 3 - Start y Excluir Directorios
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        vbox_main.pack_start(hbox, True, False, 0)
        
        label_excludedirs = Gtk.Label(label=f"{Lang('exclude_dirs')}:")
        hbox.pack_start(label_excludedirs, False, False, 0)
        
        self.entry_excludedirs = Gtk.Entry()
        self.entry_excludedirs.set_placeholder_text('DIR1,DIR2,...')
        if pathlib.Path('Exclude-Dirs.txt').exists():
            # Subproceso para leer el archivo de texto.
            self.thread = threading.Thread(
                target=self.thread_excludedirs_text
            )
            self.thread.start()
            #self.entry_excludedirs.set_text(
            #    Text_Read('Exclude-Dirs.txt', 'ModeTextOnly')
            #)
        else:
            pass
        hbox.pack_end(self.entry_excludedirs, False, False, 0)
        
        # Seccion Vertical 4 - Sincronisar
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        vbox_main.pack_start(hbox, True, False, 0)
        
        label_sync = Gtk.Label(
            label=f'{Lang("sync")} / {Lang("mode")}:'
        )
        hbox.pack_start(label_sync, False, False, 0)
        
        liststore_sync = Gtk.ListStore(str)
        options_sync = [
            Lang('default'),
            Lang('read_only')
        ]
        for option in options_sync:
            liststore_sync.append([option])
        
        self.combobox_sync = Gtk.ComboBox.new_with_model(liststore_sync)
        CellRendererText_sync = Gtk.CellRendererText()
        self.combobox_sync.pack_start(CellRendererText_sync, True)
        self.combobox_sync.add_attribute(CellRendererText_sync, 'text', 0)
        self.combobox_sync.set_active(0)
        hbox.pack_end(self.combobox_sync, False, False, 0)
        
        # Seccion Vertical Final - Iniciar
        button_start = Gtk.Button(label=Lang('start&sync') )
        button_start.connect('clicked', self.evt_start)
        vbox_main.pack_end(button_start, True, False, 0)
        
        # Fin, agragar el contenido
        self.get_content_area().add(vbox_main)
        self.show_all()
    
    def thread_excludedirs_text(self):
        # Aca se bloquea, y no se porque
        self.entry_excludedirs.set_text(
            Text_Read('Exclude-Dirs.txt', 'ModeTextOnly')
        )
        
    def evt_path(self, widget):
        dialog = Gtk.FileChooserDialog(
            title=Lang('dir_main'),
            parent=self,
            action=Gtk.FileChooserAction.SELECT_FOLDER
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Lang('set'), Gtk.ResponseType.OK
        )
        
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.label_path.set_text(Lang('set_dir') )
            self.text_path = dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            self.label_path.set_text('')
            self.text_path = None
            
        dialog.destroy()
        
    def evt_start(self, widget):
        # Carpeta
        path = YD.setPath(self.text_path)

        # Start y Excluir Directorios
        if self.entry_excludedirs.get_text() == '':
            start = YD.start()
        else:
            start = YD.start(dirs=self.entry_excludedirs.get_text())
        with open(f'Exclude-Dirs.txt', 'w') as file_txt:
            file_txt.write(self.entry_excludedirs.get_text())
        
        # Sincronisación
        sync_iter = self.combobox_sync.get_active_iter()
        sync_model = self.combobox_sync.get_model()
        sync = sync_model[sync_iter][0]
        if sync == Lang('default'):
            sync = YD.sync('')
        elif sync == Lang('read_only'):
            sync = YD.sync('read')
        
        # Ejecutar comando
        dialog = Util_Gtk.Dialog_Command_Run(
            self,
            cfg=(
                path + ' &&\n\n' +
                start + ' &&\n\n' +
                sync
            )
        )
        dialog.run()
        dialog.destroy()


win = Window_Main()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()