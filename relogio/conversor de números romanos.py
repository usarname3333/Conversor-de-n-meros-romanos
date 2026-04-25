"""
Módulo para conversão de números romanos e decimais.
Fornece uma interface gráfica moderna utilizando Tkinter.
"""

import tkinter as tk
from tkinter import font


def roman_to_int(s: str) -> int:
    """
    Converte um número romano em um número inteiro decimal.

    Args:
        s (str): A string representando o número romano.

    Returns:
        int: O valor decimal correspondente.

    Raises:
        ValueError: Se um caractere inválido for encontrado na string.
    """
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in s.upper():
        if char not in roman_values:
            raise ValueError(f"Símbolo inválido inserido: '{char}'")

    for char in reversed(s.upper()):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    return total


def int_to_roman(num: int) -> str:
    """
    Converte um número inteiro decimal em número romano.

    Args:
        num (int): O número inteiro a ser convertido (1 a 3999).

    Returns:
        str: A string com o número romano correspondente.

    Raises:
        ValueError: Se o número não estiver no intervalo suportado.
    """
    if not 0 < num < 4000:
        raise ValueError("Digite um número entre 1 e 3999")
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


class ModernConverterApp(tk.Tk):
    """
    Classe principal do aplicativo de conversão.
    Herda de tk.Tk e constrói a interface gráfica.
    """

    def __init__(self):
        """Inicializa a interface gráfica, variáveis e estilos."""
        super().__init__()
        self.title("Conversor Romano")
        self.geometry("420x520")
        self.configure(bg="#F2F4F8")

        # Centralizar a janela
        self.update_idletasks()
        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width
        height = self.winfo_height()
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2
        self.geometry(f'{width}x{height}+{x}+{y}')

        # Fontes personalizadas
        self.title_font = font.Font(family="Segoe UI", size=22, weight="bold")
        self.subtitle_font = font.Font(family="Segoe UI", size=10)
        self.label_font = font.Font(family="Segoe UI", size=9, weight="bold")
        self.entry_font = font.Font(family="Segoe UI", size=26)

        # Variáveis de Estado
        self.roman_var = tk.StringVar()
        self.decimal_var = tk.StringVar()
        self.roman_var.trace_add("write", self.on_roman_change)
        self.decimal_var.trace_add("write", self.on_decimal_change)
        self.updating = False

        self._build_ui()

    def _build_ui(self):
        """Constrói os componentes visuais do aplicativo."""
        # Card Principal (Efeito de container branco flutuante)
        self.main_card = tk.Frame(
            self, bg="#FFFFFF", highlightthickness=1,
            highlightbackground="#E2E5EA"
        )
        self.main_card.pack(expand=True, fill="both", padx=25, pady=25)

        # Cabeçalho
        tk.Label(
            self.main_card, text="Conversor", font=self.title_font,
            bg="#FFFFFF", fg="#1A1F36"
        ).pack(pady=(25, 2))
        tk.Label(
            self.main_card, text="ROMANO ⇄ DECIMAL", font=self.subtitle_font,
            bg="#FFFFFF", fg="#8792A2"
        ).pack(pady=(0, 25))

        # --- Campo Romano ---
        tk.Label(
            self.main_card, text="NÚMERO ROMANO", font=self.label_font,
            bg="#FFFFFF", fg="#A3ACBA"
        ).pack(anchor="w", padx=30)

        self.roman_frame = tk.Frame(
            self.main_card, bg="#F7F9FC", highlightthickness=2,
            highlightbackground="#E2E5EA"
        )
        self.roman_frame.pack(fill="x", padx=30, pady=(6, 20))

        self.roman_entry = tk.Entry(
            self.roman_frame, textvariable=self.roman_var, font=self.entry_font,
            bg="#F7F9FC", bd=0, highlightthickness=0, justify="center",
            fg="#1A1F36", insertbackground="#635BFF"
        )
        self.roman_entry.pack(fill="x", padx=10, pady=12)

        # --- Campo Decimal ---
        tk.Label(
            self.main_card, text="NÚMERO DECIMAL", font=self.label_font,
            bg="#FFFFFF", fg="#A3ACBA"
        ).pack(anchor="w", padx=30)

        self.decimal_frame = tk.Frame(
            self.main_card, bg="#F7F9FC", highlightthickness=2,
            highlightbackground="#E2E5EA"
        )
        self.decimal_frame.pack(fill="x", padx=30, pady=(6, 15))

        self.decimal_entry = tk.Entry(
            self.decimal_frame, textvariable=self.decimal_var,
            font=self.entry_font, bg="#F7F9FC", bd=0, highlightthickness=0,
            justify="center", fg="#1A1F36", insertbackground="#635BFF"
        )
        self.decimal_entry.pack(fill="x", padx=10, pady=12)

        # --- Mensagem de Erro ---
        self.error_label = tk.Label(
            self.main_card, text="", font=("Segoe UI", 9, "bold"),
            bg="#FFFFFF", fg="#FF4C61"
        )
        self.error_label.pack(pady=5)

        # --- Botão Limpar ---
        self.clear_btn = tk.Button(
            self.main_card, text="Limpar", font=("Segoe UI", 10, "bold"),
            bg="#F7F9FC", fg="#4F566B", bd=0, activebackground="#E2E5EA",
            activeforeground="#1A1F36", cursor="hand2",
            command=self.clear_fields
        )
        self.clear_btn.pack(pady=(10, 25), ipadx=20, ipady=6)

        # Animações sutis nos inputs (Focus Highlight)
        self.roman_entry.bind(
            "<FocusIn>", lambda _: self.on_focus(self.roman_frame, True)
        )
        self.roman_entry.bind(
            "<FocusOut>", lambda _: self.on_focus(self.roman_frame, False)
        )
        self.decimal_entry.bind(
            "<FocusIn>", lambda _: self.on_focus(self.decimal_frame, True)
        )
        self.decimal_entry.bind(
            "<FocusOut>", lambda _: self.on_focus(self.decimal_frame, False)
        )

        # Forçar o foco inicial no campo romano
        self.roman_entry.focus()

    def on_focus(self, frame, focused):
        """
        Altera a cor da borda do frame baseado no foco do cursor.
        """
        color = "#635BFF" if focused else "#E2E5EA"
        frame.config(highlightbackground=color)

    def on_roman_change(self, *args):
        """
        Manipula a alteração de texto no campo romano.
        """
        if self.updating:
            return
        roman_text = self.roman_var.get().strip().upper()

        if not roman_text:
            self.update_decimal("")
            self.error_label.config(text="")
            return

        try:
            val = roman_to_int(roman_text)
            self.update_decimal(str(val))
            self.error_label.config(text="")
        except ValueError as e:
            self.update_decimal("")
            self.error_label.config(text=str(e))

    def on_decimal_change(self, *args):
        """
        Manipula a alteração de texto no campo decimal.
        """
        if self.updating:
            return
        decimal_text = self.decimal_var.get().strip()

        if not decimal_text:
            self.update_roman("")
            self.error_label.config(text="")
            return

        if not decimal_text.isdigit():
            self.update_roman("")
            self.error_label.config(text="Apenas números inteiros positivos")
            return

        try:
            val = int(decimal_text)
            roman_val = int_to_roman(val)
            self.update_roman(roman_val)
            self.error_label.config(text="")
        except ValueError as e:
            self.update_roman("")
            self.error_label.config(text=str(e))

    def update_decimal(self, value):
        """Atualiza a interface decimal bloqueando eventos de recursão."""
        self.updating = True
        self.decimal_var.set(value)
        self.updating = False

    def update_roman(self, value):
        """Atualiza a interface romana bloqueando eventos de recursão."""
        self.updating = True
        self.roman_var.set(value)
        self.updating = False

    def clear_fields(self):
        """Limpa todos os campos da tela."""
        self.update_roman("")
        self.update_decimal("")
        self.error_label.config(text="")
        self.roman_entry.focus()


if __name__ == "__main__":
    app = ModernConverterApp()
    app.mainloop()
