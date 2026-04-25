import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("320x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#1c1c1c")
        
        self.result_var = tk.StringVar(value="0")
        self.history_var = tk.StringVar(value="")
        
        # Variáveis de Estado
        self.current_value = "0"
        self.previous_value = None
        self.current_op = None
        self.new_input = True
        self.error_state = False
        
        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        # Display Area
        display_frame = tk.Frame(self.root, bg="#1c1c1c")
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        history_label = tk.Label(
            display_frame,
            textvariable=self.history_var,
            font=("Helvetica", 16),
            bg="#1c1c1c",
            fg="#a5a5a5",
            anchor="e"
        )
        history_label.pack(fill="x")
        
        display_label = tk.Label(
            display_frame, 
            textvariable=self.result_var, 
            font=("Helvetica", 48), 
            bg="#1c1c1c", 
            fg="#ffffff", 
            anchor="e"
        )
        display_label.pack(expand=True, fill="both")
        
        # Keys Area
        keys_frame = tk.Frame(self.root, bg="#1c1c1c")
        keys_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        buttons = [
            ('AC', 'C', '+/-', '/'),
            ('7', '8', '9', 'X'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('0', '.', '=')
        ]
        
        for r, row in enumerate(buttons):
            keys_frame.rowconfigure(r, weight=1)
            for c, char in enumerate(row):
                keys_frame.columnconfigure(c, weight=1)
                
                # Cores do Dark Mode baseado no iOS
                bg_color = "#333333"
                fg_color = "#ffffff"
                active_bg = "#555555"
                
                if char in ['/', 'X', '-', '+', '=']:
                    bg_color = "#ff9f0a"
                    active_bg = "#ffb340"
                elif char in ['AC', 'C', '+/-']:
                    bg_color = "#a5a5a5"
                    fg_color = "#000000"
                    active_bg = "#d4d4d4"
                    
                # Configurando o Botão do "0" para ser mais largo (span)
                if char == '0':
                    btn = tk.Button(
                        keys_frame, text=char, bg=bg_color, fg=fg_color, 
                        font=("Helvetica", 20), borderwidth=0, activebackground=active_bg,
                        command=lambda x=char: self.on_click(x)
                    )
                    btn.grid(row=r, column=0, columnspan=2, sticky="nsew", padx=4, pady=4)
                    continue
                
                # Ajustanto a posição do '.' e '=' baseada no span do '0'
                col_index = c
                if r == 4 and char == '.': col_index = 2
                elif r == 4 and char == '=': col_index = 3
                
                btn = tk.Button(
                    keys_frame, text=char, bg=bg_color, fg=fg_color, 
                    font=("Helvetica", 20), borderwidth=0, activebackground=active_bg,
                    command=lambda x=char: self.on_click(x)
                )
                btn.grid(row=r, column=col_index, sticky="nsew", padx=4, pady=4)

    def bind_keys(self):
        # Mapeando teclado físico do pc
        for str_key in '0123456789.':
            self.root.bind(str_key, lambda e, char=str_key: self.on_click(char))
        
        self.root.bind('<Return>', lambda e: self.on_click('=')) # Enter
        self.root.bind('<Escape>', lambda e: self.on_click('AC')) # Esc
        self.root.bind('<BackSpace>', lambda e: self.on_click('C')) # Backspace
        
        self.root.bind('+', lambda e: self.on_click('+'))
        self.root.bind('-', lambda e: self.on_click('-'))
        self.root.bind('*', lambda e: self.on_click('X'))
        self.root.bind('/', lambda e: self.on_click('/'))

    def format_num(self, val):
        if val is None: return ""
        try:
            f_val = float(val)
            if f_val.is_integer():
                return str(int(f_val))
            res = str(round(f_val, 3))
            if '.' in res:
                return res.rstrip('0').rstrip('.')
            return res
        except Exception:
            return str(val)

    def update_display(self, text):
        if text == "ERR":
            self.result_var.set("ERR")
            self.error_state = True
            self.history_var.set("")
            return
            
        str_val = str(text)
        
        # Respeitamos o máximo de 8 dígitos de forma geral
        len_digits = len(str_val.replace('.', '').replace('-', ''))
        if len_digits > 8:
            self.result_var.set("ERR")
            self.error_state = True
            self.history_var.set("")
            return
            
        self.result_var.set(str_val)

    def on_click(self, char):
        # Bloquear tudo menos AC se tiver dado erro
        if self.error_state and char != 'AC':
            return
            
        if char == 'AC':
            self.current_value = "0"
            self.previous_value = None
            self.current_op = None
            self.new_input = True
            self.error_state = False
            self.history_var.set("")
            self.update_display("0")
            return
            
        if char == 'C':
            if not self.new_input:
                if len(self.current_value) > 1 and self.current_value[:-1] != '-':
                    self.current_value = self.current_value[:-1]
                else:
                    self.current_value = "0"
                    self.new_input = True
                self.update_display(self.current_value)
            else:
                self.current_op = None
                if self.previous_value is not None:
                    self.history_var.set(self.format_num(self.previous_value))
                else:
                    self.history_var.set("")
            return
            
        if char in '0123456789':
            if self.new_input:
                self.current_value = char
                self.new_input = False
            else:
                # Impede entrada maior que 8 dígitos
                if len(self.current_value.replace('.', '').replace('-', '')) < 8:
                    if self.current_value == "0":
                        self.current_value = char
                    else:
                        self.current_value += char
            self.update_display(self.current_value)
            return
            
        if char == '.':
            if self.new_input:
                self.current_value = "0."
                self.new_input = False
            else:
                if '.' not in self.current_value and len(self.current_value.replace('-', '')) < 8:
                    self.current_value += '.'
            self.update_display(self.current_value)
            return
            
        if char == '+/-':
            if self.current_value != "0" and not self.new_input:
                if self.current_value.startswith('-'):
                    self.current_value = self.current_value[1:]
                else:
                    self.current_value = '-' + self.current_value
                self.update_display(self.current_value)
            return

        # Controle de Operadores Aritméticos
        if char in ['+', '-', 'X', '/']:
            if not self.new_input and self.previous_value is not None and self.current_op:
                self.calculate()
                if self.error_state:
                    return
            elif not self.new_input:
                self.previous_value = float(self.current_value)
                
            self.current_op = char
            self.new_input = True
            self.history_var.set(f"{self.format_num(self.previous_value)} {self.current_op}")
            return
            
        # Controle de Igual (=)
        if char == '=':
            if self.previous_value is not None and self.current_op:
                history_text = f"{self.format_num(self.previous_value)} {self.current_op} {self.format_num(self.current_value)} ="
                self.history_var.set(history_text)
                self.calculate()
                self.current_op = None
                self.previous_value = None # Reseta proximo calculo em sequencia nova

    def calculate(self):
        try:
            val1 = self.previous_value
            val2 = float(self.current_value)
            
            if self.current_op == '+':
                result = val1 + val2
            elif self.current_op == '-':
                result = val1 - val2
            elif self.current_op == 'X':
                result = val1 * val2
            elif self.current_op == '/':
                if val2 == 0:
                    self.update_display("ERR")
                    return
                result = val1 / val2
            else:
                return

            # Tratamento de finalização Inteiro e Float (com restrição a 3 casas como regra)
            if result.is_integer():
                result_str = str(int(result))
            else:
                result_str = str(round(result, 3))
                if '.' in result_str:
                    result_str = result_str.rstrip('0').rstrip('.')
                    
            if len(result_str.replace('.', '').replace('-', '')) > 8:
                self.update_display("ERR")
                return
                
            self.current_value = result_str
            self.previous_value = float(result_str)
            self.new_input = True
            self.update_display(self.current_value)
            
        except Exception:
            self.update_display("ERR")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
