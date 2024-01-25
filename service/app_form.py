from models.AppForm import AppForm
from data.config import PDF_FORM_SAVE
from repository.AppFormRepository import AppFormRepository


def create_form(
        form_type: str,
        status: str,
        pay: str,
        cost: str,
        speed: str,
        name: str,
        email: str,
        phone: str,
        communication: str, wishes: str
):
    form = AppForm(form_type, status, pay, cost, speed, name, email, phone, communication, wishes)
    AppFormRepository.create_form(app_form=form)
    return __generate_pdf(form, AppFormRepository.get_last_id())


def __generate_pdf(app_form: AppForm, form_id: int):
    app_form.add_fonts()
    app_form.add_page()
    app_form.add_type()
    app_form.add_status()
    app_form.add_pay_info()
    app_form.add_cost()
    app_form.add_speed()
    app_form.add_contact_info()
    app_form.add_wishes()

    name = f'{PDF_FORM_SAVE} {form_id}.pdf'

    app_form.output(name)

    return name, form_id
