# coding: utf-8
import sys
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

class ChangeCursorApp(App):

    def on_start(self):
        """
        As opções para alterar o cursor no windows são:

        - arrow
        - ibeam
        - wait
        - crosshair
        - arrow
        - size_nwse
        - size_nesw
        - size_we
        - size_ns
        - size_all
        - no
        - hand

	 	Windows		MacOS		Linux X11	Linux Wayland
arrow	        arrow		arrow		arrow	        arrow
ibeam	        ibeam		ibeam		ibeam	        ibeam
wait	        wait		arrow		wait		wait
crosshair	crosshair	crosshair	crosshair	hand
wait_arrow	arrow		arrow		wait		wait
size_nwse	size_nwse	size_all	size_all	hand
size_nesw	size_nesw	size_all	size_all	hand
size_we		size_we		size_we		size_we		hand
size_ns		size_ns		size_ns		size_ns		hand
size_all	size_all	size_all	size_all	hand
no		no		no		no		ibeam
hand		hand		hand		hand		hand

        Para obter uma lista completa, visite:
        https://kivy.org/docs/api-kivy.core.window.html#kivy.core.window.WindowBase.set_system_cursor
        """

        Window.set_system_cursor(sys.argv[1])
        print("")

    def build(self):
        return Button(text='Funcionou :D',
                      size_hint=(.2, .2),
                      pos_hint={"center_x": .5, "center_y": .5, }
                      )


if __name__ == '__main__':
    """
    Aplicação de demonstração de como alterar o cursor do mouse numa aplicação.
    """
    o = ChangeCursorApp()
    o.run()
