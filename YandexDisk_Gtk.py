import Modulo_Util as Util
import Modulo_Util_Gtk as Util_Gtk
import Modulo_YandexDisk as YD
import os, pathlib, subprocess

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
        button_login = Gtk.Button(label='Iniciar sesion')
        button_login.connect('clicked', self.evt_login)
        vbox_main.pack_start(button_login, True, False, 0)
        
        # Seccion Vertical 3 - Estado-Status
        button_status = Gtk.Button(label='Estado de conección')
        button_status.connect('clicked', self.evt_status)
        vbox_main.pack_start(button_status, True, False, 0)
        
        # Seccion Vertical 2 - Ayuda
        button_help = Gtk.Button(label='Ayuda')
        button_help.connect('clicked', self.evt_help)
        vbox_main.pack_start(button_help, True, False, 0)
        
        # Seccion Vertical 3 - Iniciar o Parar
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        vbox_main.pack_start(hbox, True, False, 0)
        
        label_start = Gtk.Label(label='Parar / Iniciar')
        hbox.pack_start(label_start, False, True, 0)
        
        switch_start = Gtk.Switch()
        switch_start.set_active(False)
        switch_start.connect('notify::active', self.evt_start)
        hbox.pack_end(switch_start, False, True, 0)
        
        # Fin, Mostrar contenedor y su contenido
        self.add(vbox_main)
        
    def evt_login(self, QWidget):
        dialog = Util_Gtk.Dialog_Command_Run(
            self, cfg=YD.token()
        )
        dialog.run()
        dialog.destroy()
        
    def evt_status(self, QWidget):
        dialog = Util_Gtk.Dialog_Command_Run(
            self, cfg=YD.status()
        )
        dialog.run()
        dialog.destroy()
        
    def evt_help(self, QWidget):
        dialog = Util_Gtk.Dialog_Command_Run(self, cfg=YD.help())
        dialog.run()
        dialog.destroy()
        
    def evt_start(self, switch, gparam):
        if switch.get_active():
            dialog = Dialog_Start(self)
            dialog.run()
            dialog.destroy()
            #switch.set_active(False) # Para desactivar cuando se cierre.
        else:
            dialog = Util_Gtk.Dialog_Command_Run(
                self, cfg=(YD.stop())
            )
            dialog.run()
            dialog.destroy()


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
        self.text_path = ''
        button_path = Gtk.Button(label='Carpeta')
        button_path.connect('clicked', self.evt_path)
        vbox_main.pack_start(button_path, True, False, 0)
        
        # Seccion Vertical 2 - Carpeta Label
        self.label_path = Gtk.Label()
        vbox_main.pack_start(self.label_path, True, False, 0)
        
        # Seccion Vertical 3 - Start y Excluir Directorios
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        vbox_main.pack_start(hbox, True, False, 0)
        
        label_excludedirs = Gtk.Label(label='Excluir Directorios:')
        hbox.pack_start(label_excludedirs, False, False, 0)
        
        self.entry_excludedirs = Gtk.Entry()
        self.entry_excludedirs.set_placeholder_text('DIR1,DIR2,...')
        if pathlib.Path('Exclude-Dirs.txt').exists():
            self.entry_excludedirs.set_text(
                Util.Text_Read('Exclude-Dirs.txt', 'ModeTextOnly')
            )
        else:
            pass
        hbox.pack_end(self.entry_excludedirs, False, False, 0)
        
        # Seccion Vertical 4 - Sincronisar
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        vbox_main.pack_start(hbox, True, False, 0)
        
        label_sync = Gtk.Label(label='Sincronisar / Modo:')
        hbox.pack_start(label_sync, False, False, 0)
        
        liststore_sync = Gtk.ListStore(str)
        options_sync = [
            'Por defecto',
            'Solo lectura'
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
        button_start = Gtk.Button(label='Iniciar y Sincronisar')
        button_start.connect('clicked', self.evt_start)
        vbox_main.pack_end(button_start, True, False, 0)
        
        # Fin, agragar el contenido
        self.get_content_area().add(vbox_main)
        self.show_all()
        
    def evt_path(self, QWidget):
        dialog = Gtk.FileChooserDialog(
            title='Carpeta para Yandex Disk',
            parent=self,
            action=Gtk.FileChooserAction.SELECT_FOLDER
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            'Seleccionar', Gtk.ResponseType.OK
        )
        
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.label_path.set_text('Carpeta seleccionada')
            self.text_path = dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            self.label_path.set_text('')
            self.text_path = dialog.get_filename()
            
        dialog.destroy()
        
    def evt_start(self, QWidget):
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
        if sync == 'Por defecto':
            sync = YD.sync('')
        elif sync == 'Solo lectura':
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