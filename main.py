import os
import sys
import traceback
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.clipboard import Clipboard

# ---------------------------------------------------------
# 1. Təhlükəsizlik Bloğu (Proqram çökərsə bu işə düşür)
# ---------------------------------------------------------
class CrashApp(App):
    def __init__(self, error_msg, **kwargs):
        super().__init__(**kwargs)
        self.error_msg = error_msg

    def build(self):
        # Xətanı göstərən sadə ekran
        root = ScrollView()
        label = Label(
            text=f"XƏTA BAŞ VERDİ (ScreenShot çəkib göndər):\n\n{self.error_msg}",
            color=(1, 0, 0, 1),  # Qırmızı rəng
            font_size='18sp',
            size_hint_y=None,
            halign="left",
            valign="top"
        )
        label.bind(texture_size=label.setter('size'))
        root.add_widget(label)
        return root

# ---------------------------------------------------------
# 2. Sənin Əsas Proqramın
# ---------------------------------------------------------
try:
    # Kitabxanaları burada import edirik
    from kivymd.app import MDApp
    from kivymd.uix.screen import MDScreen
    from kivymd.uix.textfield import MDTextField
    from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton
    from kivymd.uix.label import MDLabel
    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.uix.card import MDCard
    from kivymd.toast import toast
    import hashlib

    SECRET_KEY_SALT = "AKIF_TV_2025_SECURE"

    class AdminKeygenApp(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Red"
            
            screen = MDScreen()
            layout = MDBoxLayout(orientation="vertical", padding=40, spacing=30, pos_hint={"center_y": 0.5})
            
            title = MDLabel(text="AKİF ADMIN KEYGEN", halign="center", font_style="H5", theme_text_color="Custom", text_color=(1, 0, 0, 1), bold=True)
            layout.add_widget(title)
            
            self.input_id = MDTextField(
                hint_text="Müştəri ID-sini bura yaz",
                helper_text="Məs: 9X2A-5B7C",
                helper_text_mode="on_focus",
                font_size=26
            )
            layout.add_widget(self.input_id)
            
            btn_gen = MDFillRoundFlatButton(
                text="KODU YARAT", font_size=20, pos_hint={"center_x": 0.5}, size_hint_x=1
            )
            btn_gen.bind(on_release=self.generate_key)
            layout.add_widget(btn_gen)
            
            self.card = MDCard(
                orientation="vertical", padding=20, size_hint=(1, None), height=150, radius=[20],
                md_bg_color=(0.15, 0.15, 0.15, 1)
            )
            
            lbl_info = MDLabel(text="Aktivasiya Kodu:", halign="center", theme_text_color="Secondary")
            self.lbl_code = MDLabel(text="----", halign="center", font_style="H4", theme_text_color="Custom", text_color=(0, 1, 0, 1), bold=True)
            
            self.card.add_widget(lbl_info)
            self.card.add_widget(self.lbl_code)
            layout.add_widget(self.card)
            
            self.btn_copy = MDIconButton(
                icon="content-copy", pos_hint={"center_x": 0.5}, user_font_size="48sp",
                theme_text_color="Custom", text_color=(1, 1, 1, 1), disabled=True
            )
            self.btn_copy.bind(on_release=self.copy_code)
            layout.add_widget(self.btn_copy)
            
            screen.add_widget(layout)
            return screen

        def generate_key(self, instance):
            machine_id = self.input_id.text.strip()
            if not machine_id:
                toast("ID yazılmayıb!")
                return
            try:
                raw = machine_id + SECRET_KEY_SALT
                key = hashlib.sha256(raw.encode()).hexdigest().upper()[:8]
                self.lbl_code.text = key
                self.btn_copy.disabled = False
                self.btn_copy.text_color = (0, 1, 0, 1)
                toast("Kod Hazırdır!")
            except:
                self.lbl_code.text = "XƏTA"

        def copy_code(self, instance):
            Clipboard.copy(self.lbl_code.text)
            toast("Kopyalandı")

    # Proqramı işə salırıq
    if __name__ == "__main__":
        try:
            AdminKeygenApp().run()
        except Exception:
            # Əgər KivyMD daxilində xəta olsa, bura düşəcək
            error_text = traceback.format_exc()
            CrashApp(error_text).run()

except Exception:
    # Əgər Kitabxanalar (import) zamanı xəta olsa, bura düşəcək
    error_text = traceback.format_exc()
    CrashApp(error_text).run()