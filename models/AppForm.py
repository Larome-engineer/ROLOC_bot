from fpdf import FPDF
from data.config import FONT_BOLD_PATH, FONT_MONO_PATH


class AppForm(FPDF):
    bold_size = 16
    mono_size = 14
    bold_name = 'DejaVuB'
    mono_name = 'DejaVuM'

    def __init__(self, form_type: str, status: str, pay_info: str, cost: str,
                 speed: str, name: str, email: str, phone: str, communication: str, wishes: str):
        super().__init__()
        self.__form_type = form_type,
        self.__status = status,
        self.__pay_info = pay_info
        self.__cost = cost,
        self.__speed = speed,
        self.__name = name,
        self.__email = email,
        self.__phone = phone,
        self.__communication = communication,
        self.__wishes = wishes

    # GETTERS AND SETTERS
    @property
    def form_type(self):
        return self.__form_type

    @form_type.setter
    def form_type(self, var):
        self.__form_type = var

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, var):
        self.__status = var

    @property
    def pay_info(self):
        return self.__pay_info

    @pay_info.setter
    def pay_info(self, var):
        self.__pay_info = var

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, var):
        self.__cost = var

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, var):
        self.__speed = var

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, var):
        self.__name = var

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, var):
        self.__email = var

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, var):
        self.__phone = var

    @property
    def communication(self):
        return self.__communication

    @communication.setter
    def communication(self, var):
        self.__communication = var

    @property
    def wishes(self):
        return self.__wishes

    @wishes.setter
    def wishes(self, var):
        self.__wishes = var

    # PERFORM APP FORM
    def add_fonts(self):
        self.add_font(self.bold_name, '', FONT_BOLD_PATH, uni=True)
        self.add_font(self.mono_name, '', FONT_MONO_PATH, uni=True)

    def add_type(self):
        self.set_font(self.bold_name, size=self.bold_size)
        self.cell(0, 30, txt='Вид услуги', ln=1, align='L')
        self.set_font(self.mono_name, size=self.mono_size)
        self.cell(0, -15, txt=f'{self.__form_type[0]}', ln=1, align='L')

    def add_status(self):
        self.set_font(self.bold_name, size=self.bold_size)
        self.cell(0, 40, txt='Статус заявки', ln=1, align='L')
        self.set_font(self.mono_name, size=self.mono_size)
        self.cell(0, -25, txt=f'{self.__status[0]}', ln=1, align='L')

    def add_pay_info(self):
        self.set_font(self.bold_name, size=self.bold_size)
        self.cell(0, 50, txt='Оплата', ln=1, align='L')
        self.set_font(self.mono_name, size=self.mono_size)
        self.cell(0, -35, txt=f'{self.__pay_info}', ln=1, align='L')

    def add_cost(self):
        self.set_font(self.bold_name, size=self.bold_size)
        self.cell(0, 60, txt='Стоимость', ln=1, align='L')
        self.set_font(self.mono_name, size=self.mono_size)
        self.cell(0, -45, txt=f'{self.__cost[0]}', ln=1, align='L')

    def add_speed(self):
        self.set_font(self.bold_name, size=self.bold_size)
        self.cell(0, 70, txt='Скорость', ln=1, align='L')
        self.set_font(self.mono_name, size=self.mono_size)
        self.cell(0, -55, txt=f'{self.__speed[0]}', ln=1, align='L')

    def add_contact_info(self):
        self.set_font(self.bold_name, size=self.bold_size)
        self.cell(0, 90, txt='Контакты', ln=1, align='L')
        self.set_font(self.mono_name, size=self.mono_size)
        self.cell(0, -75, txt=f'Имя: {self.__name[0]}', ln=1, align='L')
        self.set_font(self.mono_name, size=self.mono_size)
        self.cell(0, 90, txt=f'Почта: {self.__email[0]}', ln=1, align='L')
        self.set_font(self.mono_name, size=self.mono_size)
        self.cell(0, -75, txt=f'Телефон: {self.__phone[0]} ({self.__communication[0]})', ln=1, align='L')

    def add_wishes(self):
        self.set_font(self.bold_name, size=self.bold_size)
        self.cell(0, 105, txt='Пожелания', ln=1, align='L')

        self.ln(-47)

        self.set_font(self.mono_name, size=self.mono_size)
        self.multi_cell(0, 6, txt=f'{self.__wishes}', align='J')
