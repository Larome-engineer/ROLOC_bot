from repository.AppFormRepository import AppFormRepository


def get_all_by_status(status):
    forms = AppFormRepository.get_all_forms_by_status(status)
    if forms is None:
        return f"❌ Заявок co статусом: '{status}' не существует"

    f_li = []
    for i in forms:
        f_li.append(str(i[0]))

    if status == 'В обработке':
        b = ' Заявка#'.join(f_li).replace(' ', "\n")
        if b == '':
            text = '<strong>ВСЕ ЗАЯВКИ ИСПОЛНЕНЫ</strong> ✅'
        else:
            text = "<strong>🕔 ЗАЯВКИ В ОБРАБОТКЕ</strong>\n\n" + f"<ins>Заявка#{' Заявка#'.join(f_li)}</ins>".replace(' ', "\n")
    elif status == 'Исполнена':
        b = ' Заявка#'.join(f_li).replace(' ', "\n")
        if b == '':
            text = '<strong>ВСЕ ЗАЯВКИ В ОБРАБОТКЕ</strong> 🕔'
        else:
            text = "<strong>✅ ИСПОЛНЕННЫЕ ЗАЯВКИ</strong>\n\n" + f"<ins>Заявка#{' Заявка#'.join(f_li)}</ins>".replace(' ', "\n")
    else:
        text = f"❌ Заявок co статусом: <strong>{status}</strong> не существует"

    return text


def get_by_id(form_id: int):
    form = AppFormRepository.get_form_by_id(form_id)
    if form is None:
        return f"❌ Заявок с ID: <strong>{form_id}</strong> не существует"
    form_dict = {
        "<ins>AppForm</ins>": form_id,
        "▫️ Вид услуги": form[0],
        "▫️ Статус заявки": form[1],
        "▫️ Оплата": form[2],
        "▫️ Стоимость": form[3],
        "▫️ Скорость": form[4],
        "▫️ Контакты": [form[5], form[6], form[7]],
        "▫️ Пожелания": form[8]
    }
    formatted_values = [
        f"{k}: {' | '.join(v) if isinstance(v, list) else v}" for k, v in form_dict.items()
    ]
    return '\n'.join(formatted_values)


def change_status(form_status: str, form_id: int):
    AppFormRepository.change_form_status(form_status, form_id)


def change_pay_info(form_pay_info: str, form_id: int):
    AppFormRepository.change_form_pay_info(form_pay_info, form_id)
