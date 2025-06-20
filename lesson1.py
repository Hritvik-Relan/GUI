import math
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class CalcApp(App):
    def build(self):
        self.is_advanced = False
        self.input = TextInput(readonly=True, halign="right", font_size=40, multiline=False)
        self.layout = BoxLayout(orientation="vertical")
        self.layout.add_widget(self.input)

        self.button_grid = GridLayout(cols=4)
        self.build_buttons()
        self.layout.add_widget(self.button_grid)

        return self.layout

    def build_buttons(self):
        self.button_grid.clear_widgets()

        basic_buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+',
        ]

        advanced_buttons = [
            '(', ')', '^', '√',
            'log', 'ln', 'abs', '.',
            'sin', 'cos', 'tan', 'π',
            'e'
        ]

        buttons = basic_buttons + advanced_buttons if self.is_advanced else basic_buttons

        for b in buttons:
            btn = Button(text=b, font_size=24)
            btn.bind(on_press=self.on_button_press)
            self.button_grid.add_widget(btn)

        toggle_btn = Button(text="Advanced" if not self.is_advanced else "Basic", font_size=20)
        toggle_btn.bind(on_press=self.toggle_mode)
        self.button_grid.add_widget(toggle_btn)

    def on_button_press(self, instance):
        text = instance.text

        if text == 'C':
            self.input.text = ''
        elif text == '=':
            try:
                expr = self.input.text

                expr = expr.replace('^', '**')
                expr = expr.replace('√', 'math.sqrt')
                expr = expr.replace('log', 'math.log10')
                expr = expr.replace('ln', 'math.log')
                expr = expr.replace('π', str(math.pi))
                expr = expr.replace('e', str(math.e))
                expr = expr.replace('sin', 'math.sin')
                expr = expr.replace('cos', 'math.cos')
                expr = expr.replace('tan', 'math.tan')
                expr = expr.replace('abs', 'abs')

                allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
                allowed_names['abs'] = abs
                self.input.text = str(eval(expr, {"__builtins__": None}, allowed_names))
            except Exception:
                self.input.text = 'Error'
        elif text not in ('Advanced', 'Basic'):
            self.input.text += text

    def toggle_mode(self, instance):
        self.is_advanced = not self.is_advanced
        self.build_buttons()


if __name__ == "__main__":
    CalcApp().run()
