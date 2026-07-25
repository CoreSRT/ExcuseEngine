import customtkinter as ctk
import locale as _locale
import os
import random
import sys

# ============================================================
# Translations — 14 languages
# ============================================================
TRANSLATIONS: dict[str, dict[str, str]] = {
    'ru': {
        'title': 'ExcuseEngine',
        'heading': 'Выбери вероятность',
        'entry_label': 'Или введи:',
        'button_roll': 'Выбрать',
        'yes': 'Да',
        'no': 'Нет',
    },
    'en': {
        'title': 'ExcuseEngine',
        'heading': 'Choose probability',
        'entry_label': 'Or enter:',
        'button_roll': 'Choose',
        'yes': 'Yes',
        'no': 'No',
    },
    'es': {
        'title': 'ExcuseEngine',
        'heading': 'Elige la probabilidad',
        'entry_label': 'O introduce:',
        'button_roll': 'Elegir',
        'yes': 'Sí',
        'no': 'No',
    },
    'pt': {
        'title': 'ExcuseEngine',
        'heading': 'Escolha a probabilidade',
        'entry_label': 'Ou digite:',
        'button_roll': 'Escolher',
        'yes': 'Sim',
        'no': 'Não',
    },
    'de': {
        'title': 'ExcuseEngine',
        'heading': 'Wahrscheinlichkeit wählen',
        'entry_label': 'Oder eingeben:',
        'button_roll': 'Wählen',
        'yes': 'Ja',
        'no': 'Nein',
    },
    'fr': {
        'title': 'ExcuseEngine',
        'heading': 'Choisir la probabilité',
        'entry_label': 'Ou entrer :',
        'button_roll': 'Choisir',
        'yes': 'Oui',
        'no': 'Non',
    },
    'it': {
        'title': 'ExcuseEngine',
        'heading': 'Scegli la probabilità',
        'entry_label': 'Oppure inserisci:',
        'button_roll': 'Scegli',
        'yes': 'Sì',
        'no': 'No',
    },
    'ja': {
        'title': 'ExcuseEngine',
        'heading': '確率を選択',
        'entry_label': 'または入力:',
        'button_roll': '選ぶ',
        'yes': 'はい',
        'no': 'いいえ',
    },
    'zh': {
        'title': 'ExcuseEngine',
        'heading': '选择概率',
        'entry_label': '或输入:',
        'button_roll': '选择',
        'yes': '是',
        'no': '否',
    },
    'pl': {
        'title': 'ExcuseEngine',
        'heading': 'Wybierz prawdopodobieństwo',
        'entry_label': 'Lub wpisz:',
        'button_roll': 'Wybierz',
        'yes': 'Tak',
        'no': 'Nie',
    },
    'ko': {
        'title': 'ExcuseEngine',
        'heading': '확률 선택',
        'entry_label': '또는 입력:',
        'button_roll': '선택',
        'yes': '예',
        'no': '아니요',
    },
    'ar': {
        'title': 'ExcuseEngine',
        'heading': 'اختر الاحتمال',
        'entry_label': 'أو أدخل:',
        'button_roll': 'اختر',
        'yes': 'نعم',
        'no': 'لا',
    },
    'tr': {
        'title': 'ExcuseEngine',
        'heading': 'Olasılığı seçin',
        'entry_label': 'Veya girin:',
        'button_roll': 'Seç',
        'yes': 'Evet',
        'no': 'Hayır',
    },
    'hi': {
        'title': 'ExcuseEngine',
        'heading': 'संभावना चुनें',
        'entry_label': 'या दर्ज करें:',
        'button_roll': 'चुनें',
        'yes': 'हाँ',
        'no': 'नहीं',
    },
}

# Human-readable language names (in their own script)
LANGUAGE_NAMES: dict[str, str] = {
    'ru': 'Русский',
    'en': 'English',
    'es': 'Español',
    'pt': 'Português',
    'de': 'Deutsch',
    'fr': 'Français',
    'it': 'Italiano',
    'ja': '日本語',
    'zh': '中文',
    'pl': 'Polski',
    'ko': '한국어',
    'ar': 'العربية',
    'tr': 'Türkçe',
    'hi': 'हिन्दी',
}

# Display order: Russian first, then English, then alphabetical
LANG_ORDER = ['ru', 'en', 'es', 'pt', 'de', 'fr', 'it', 'pl', 'tr', 'ar', 'hi', 'ja', 'zh', 'ko']


def detect_language() -> str:
    """Detect language from system locale (if available in the list)."""
    sys_locale = _locale.getdefaultlocale()[0]
    if sys_locale:
        lang_code = sys_locale[:2].lower()
        if lang_code in TRANSLATIONS:
            return lang_code
    return 'en'


# ============================================================
# Colors
# ============================================================
GREEN = '#2ECC71'
RED = '#E74C3C'
DARK_GREEN = '#27AE60'
DARK_RED = '#C0392B'

# ============================================================
# Window
# ============================================================
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

current_lang = detect_language()
t = TRANSLATIONS[current_lang]

app = ctk.CTk()
app.title(t['title'])
app.geometry('500x500')
app.resizable(False, False)

# Window icon (works both from source and from frozen exe)
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_path, 'icons', 'icon_dice.ico')
if not os.path.isfile(icon_path):
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'icon_dice.ico')
try:
    app.iconbitmap(icon_path)
except Exception:
    pass


# ============================================================
# Language switcher — dropdown in the top bar
# ============================================================
# Stores the last roll outcome so we can re-translate it on the fly
_last_was_yes: bool | None = None


def apply_language(lang: str) -> None:
    global current_lang, t, _last_was_yes
    current_lang = lang
    t = TRANSLATIONS[lang]
    app.title(t['title'])
    title_label.configure(text=t['heading'])
    entry_label.configure(text=t['entry_label'])
    button_roll.configure(text=t['button_roll'])
    # Re-translate the currently displayed result if one exists
    if _last_was_yes is not None:
        answer = t['yes'] if _last_was_yes else t['no']
        color = GREEN if _last_was_yes else RED
        result_label.configure(text=answer, text_color=color)
        result_frame.configure(border_color=color)


def on_lang_selected(choice: str) -> None:
    """Dropdown callback: find language code by its display name."""
    for code, name in LANGUAGE_NAMES.items():
        if name == choice:
            apply_language(code)
            break


lang_options = [LANGUAGE_NAMES[code] for code in LANG_ORDER]

# Top bar frame — keeps the combo aligned to the right
top_frame = ctk.CTkFrame(app, fg_color='transparent', height=36)
top_frame.pack(fill='x', padx=10, pady=(8, 0))
top_frame.pack_propagate(False)

lang_combo = ctk.CTkComboBox(
    top_frame,
    values=lang_options,
    command=on_lang_selected,
    width=140,
    height=30,
    font=ctk.CTkFont(size=13),
    dropdown_font=ctk.CTkFont(size=13),
    state='readonly',
)
lang_combo.set(LANGUAGE_NAMES[current_lang])
lang_combo.pack(side='right')

# ============================================================
# Heading
# ============================================================
title_label = ctk.CTkLabel(
    app,
    text=t['heading'],
    font=ctk.CTkFont(size=20, weight='bold'),
)
title_label.pack(pady=(20, 10))

# ============================================================
# Slider + 0% / 100% labels
# ============================================================
slider_frame = ctk.CTkFrame(app, fg_color='transparent')
slider_frame.pack(pady=(0, 5))

left_label = ctk.CTkLabel(
    slider_frame,
    text='0%',
    font=ctk.CTkFont(size=14),
    text_color='gray',
)
left_label.pack(side='left', padx=(0, 10))

slider_var = ctk.IntVar(value=50)

slider = ctk.CTkSlider(
    slider_frame,
    from_=0,
    to=100,
    number_of_steps=100,
    variable=slider_var,
    width=300,
)
slider.pack(side='left')

right_label = ctk.CTkLabel(
    slider_frame,
    text='100%',
    font=ctk.CTkFont(size=14),
    text_color='gray',
)
right_label.pack(side='left', padx=(10, 0))

# ============================================================
# Current percentage label
# ============================================================
value_label = ctk.CTkLabel(
    app,
    text='50%',
    font=ctk.CTkFont(size=26, weight='bold'),
)
value_label.pack(pady=(10, 5))

# ============================================================
# Numeric entry
# ============================================================
entry_frame = ctk.CTkFrame(app, fg_color='transparent')
entry_frame.pack(pady=(0, 10))

entry_var = ctk.StringVar(value='50')

entry_label = ctk.CTkLabel(
    entry_frame,
    text=t['entry_label'],
    font=ctk.CTkFont(size=13),
    text_color='gray',
)
entry_label.pack(side='left', padx=(0, 6))

entry = ctk.CTkEntry(
    entry_frame,
    textvariable=entry_var,
    width=60,
    height=30,
    font=ctk.CTkFont(size=15),
    justify='center',
)
entry.pack(side='left', padx=(0, 4))

percent_sign = ctk.CTkLabel(
    entry_frame,
    text='%',
    font=ctk.CTkFont(size=15),
)
percent_sign.pack(side='left', padx=(0, 8))

apply_button = ctk.CTkButton(
    entry_frame,
    text='✓',
    width=36,
    height=30,
    font=ctk.CTkFont(size=15, weight='bold'),
    fg_color=DARK_GREEN,
    hover_color=GREEN,
    command=lambda: sync_from_entry(),
)
apply_button.pack(side='left')


# ============================================================
# Entry ↔ Slider sync logic
# ============================================================
def sync_from_entry() -> None:
    text = entry_var.get().strip()
    if text == '':
        return
    try:
        value = int(text)
    except ValueError:
        entry_var.set(str(slider_var.get()))
        return
    value = max(0, min(100, value))
    slider_var.set(value)
    entry_var.set(str(value))
    value_label.configure(text=f'{value}%')


def on_entry_return(event) -> None:
    sync_from_entry()


entry.bind('<Return>', on_entry_return)
entry.bind('<FocusOut>', lambda e: sync_from_entry())


def on_slider_change(value: float) -> None:
    int_value = int(round(value))
    value_label.configure(text=f'{int_value}%')
    entry_var.set(str(int_value))


slider.configure(command=on_slider_change)

# ============================================================
# Result inside a bordered frame
# ============================================================
result_frame = ctk.CTkFrame(
    app,
    fg_color='transparent',
    border_width=2,
    border_color='gray',
    corner_radius=12,
    width=200,
    height=80,
)
result_frame.pack(pady=(15, 10))
result_frame.pack_propagate(False)

result_label = ctk.CTkLabel(
    result_frame,
    text='',
    font=ctk.CTkFont(size=36, weight='bold'),
)
result_label.place(relx=0.5, rely=0.5, anchor='center')


def roll() -> None:
    global _last_was_yes
    percent = slider_var.get()
    r = random.randint(1, 100)
    is_yes = r <= percent
    _last_was_yes = is_yes
    answer = t['yes'] if is_yes else t['no']
    color = GREEN if is_yes else RED
    result_label.configure(text=answer, text_color=color)
    result_frame.configure(border_color=color)


# ============================================================
# Roll button
# ============================================================
button_roll = ctk.CTkButton(
    app,
    text=t['button_roll'],
    command=roll,
    width=170,
    height=50,
    font=ctk.CTkFont(size=18, weight='bold'),
    fg_color=DARK_GREEN,
    hover_color=GREEN,
)
button_roll.pack(pady=(5, 10))

# ============================================================
app.mainloop()
