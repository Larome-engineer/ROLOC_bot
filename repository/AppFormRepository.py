import sqlite3 as db
from models.AppForm import AppForm
from data.config import DB_PATH

# c = db.connect(DB_PATH)
# cursor = c.cursor()
# cursor.execute("""drop table application""")
# c.commit()
# cursor.execute("""
# CREATE TABLE application(
#     form_id integer primary key autoincrement,
#     form_service text not null,
#     form_status text not null,
#     form_pay_info text not null,
#     form_cost text not null,
#     form_speed text not null,
#     form_name text not null,
#     form_email text not null,
#     form_phone text not null,
#     form_wishes text not null
# );
# """)
# c.commit()
# cursor.close()


class AppFormRepository:
    @staticmethod
    def create_form(app_form: AppForm):
        with db.connect(DB_PATH) as connection:
            connection.cursor().execute("""
            insert into application (
                    form_service, 
                    form_status, 
                    form_pay_info, 
                    form_cost,
                    form_speed, 
                    form_name, 
                    form_email, 
                    form_phone, 
                    form_wishes
                ) values (?, ?, ?, ?, ?, ?, ? ,?, ?)
                """, (app_form.form_type[0], app_form.status[0], app_form.pay_info, app_form.cost[0],
                      app_form.speed[0], app_form.name[0], app_form.email[0], app_form.phone[0], app_form.wishes))
            connection.commit()

    @staticmethod
    def get_all_forms_by_status(status):
        with db.connect(DB_PATH) as connection:
            return connection.cursor().execute(
                """select form_id from application where form_status = ?""",
                (status,)).fetchall()

    @staticmethod
    def get_form_by_id(form_id: int):
        with db.connect(DB_PATH) as connection:
            return connection.cursor().execute(
                """select form_service, form_status, form_pay_info, form_cost,
                    form_speed, form_name, form_email, form_phone, form_wishes from application where form_id = ?""",
                (form_id,)).fetchone()

    @staticmethod
    def change_form_status(form_status: str, form_id: int):
        with db.connect(DB_PATH) as connection:
            connection.cursor().execute(
                """update application set form_status = ? where form_id = ?""", (form_status, form_id)
            )

            connection.commit()

    @staticmethod
    def change_form_pay_info(form_pay_info: str, form_id: int):
        with db.connect(DB_PATH) as connection:
            connection.cursor().execute(
                """update application set form_pay_info = ? where form_id = ?""", (form_pay_info, form_id)
            )

            connection.commit()

    @staticmethod
    def get_last_id():
        with db.connect(DB_PATH) as connection:
            return connection.cursor().execute(
                """select form_id from application order by form_id desc limit 1"""
            ).fetchone()[0]
