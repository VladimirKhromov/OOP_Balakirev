from string import ascii_lowercase, digits

class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size = 10):
        self.check_name(name)
        self.name = name  
        self.size = size
        

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if len(name) >= 3 and len(name) < 50:
            if frozenset(name) < frozenset(cls.CHARS_CORRECT):
                return True
        raise ValueError('некорректное имя поля')



class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size = 10):
        self.check_name(name)
        self.name = name  
        self.size = size

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if len(name) >= 3 and len(name) < 50:
            if frozenset(name) < frozenset(cls.CHARS_CORRECT):
                return True
        raise ValueError('некорректное имя поля')


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])



login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()



