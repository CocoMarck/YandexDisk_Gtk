import Modulo_Util as Util

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

sys = Util.System()

class Dialog_TextView(Gtk.Dialog):
    def __init__(
        self, parent,
        text = 'Texto\nSalto de linea y etc...'
    ):
        super().__init__(title='Text', transient_for=parent, flags=0)
        self.set_default_size(512, 256)

        box_v = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        text_scroll = Gtk.ScrolledWindow()
        text_scroll.set_hexpand(True)
        text_scroll.set_vexpand(True)
        
        text_view = Gtk.TextView()
        #text_view.set_size_request(512, 256)
        text_view.set_editable(False)
        text_buffer = text_view.get_buffer()
        text_buffer.set_text(text)
        text_scroll.add(text_view)
        
        box_v.pack_start(text_scroll, True, True, 0)
        
        exit_box = Gtk.Box(spacing=4)
        box_v.pack_start(exit_box, False, True, 0)
        
        exit_btn = Gtk.Button(label='Salir')
        exit_btn.connect('clicked', self.evt_exit)
        exit_box.pack_start(exit_btn, True, True, 0)
        
        box_main = self.get_content_area()
        box_main.add(box_v)
        self.show_all()
        
    def evt_exit(self, widget):
        self.destroy()


class Dialog_Command_Run(Gtk.Dialog):
    def __init__(self, parent, cfg='', txt='Ejecutar Comando', cfg_file=''):
        super().__init__(title='Command Run', transient_for=parent, flags=0)
        self.set_default_size(512, 256)
        self.cfg = cfg
        self.cfg_file = cfg_file
        
        title_HeaderBar = Gtk.HeaderBar()
        title_HeaderBar.set_show_close_button(True)
        title_HeaderBar.props.title = 'Comando'
        self.set_titlebar(title_HeaderBar)
        
        box_v = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        #box_v.set_homogeneous(False)
        #box_v.set_property("expand", True)
        #box_v.set_property("halign", Gtk.Align.CENTER)
        
        #label = Gtk.Label()
        #label.set_markup(f'<b>Comando</b>')
        #label.set_line_wrap(True)
        #box_v.pack_start(label, False, False, 16)
        
        # Zona donde se ve el comando
        cmd_scroll = Gtk.ScrolledWindow()
        cmd_scroll.set_hexpand(True)
        cmd_scroll.set_vexpand(True)
        cmd_label = Gtk.Label()
        #cmd_label.set_line_wrap(True)
        cmd_label.set_selectable(True)
        #cmd_label.set_justify(Gtk.Justification.LEFT)
        cmd_label.set_text(f'{self.cfg}')
        cmd_scroll.add(cmd_label)
        box_v.pack_start(cmd_scroll, True, True, 0)
        
        button = Gtk.Button(label=txt)
        button.connect('clicked', self.evt_command_run)
        box_v.pack_end(button, False, False, 16)
        
        self.get_content_area().add(box_v)
        self.show_all()
        
    def evt_command_run(self, widget):
        if self.cfg_file == '':
            pass
        else:
            with open(self.cfg_file, 'a') as file_cfg:
                    file_cfg.write(self.cfg + f'\n#{Util.Separator(see=False)}\n')
                
        Util.Command_Run(self.cfg)
        self.destroy()