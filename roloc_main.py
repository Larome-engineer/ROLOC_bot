import asyncio, logging, sys
from roloc_create import dp, roloc_bot

from handlers.admin import admin_router

from handlers.menu import menu_router
from handlers.form import form_router

from handlers.common.help import help_router
from handlers.common.start import start_router
from handlers.common.about import about_router
from handlers.common.back import back_to_router


async def main():
    dp.include_routers(
        start_router,
        about_router,
        back_to_router,
        help_router,
        menu_router,
        form_router,
        admin_router
    )

    await dp.start_polling(roloc_bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')
