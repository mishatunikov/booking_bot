from datetime import datetime, timedelta

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from .consts import MAX_NUMBER_OF_DATES, DATES_ON_PAGE


async def main_page_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    i18n: TranslatorRunner,
    **kwargs,
):
    page = dialog_manager.start_data.get('dates_page')
    days_for_booking = []
    days_off = DATES_ON_PAGE * (page + 1)

    if (end_range := (page + 1) * DATES_ON_PAGE) > MAX_NUMBER_OF_DATES:
        end_range = MAX_NUMBER_OF_DATES

    for i in range(DATES_ON_PAGE * page, end_range):
        days_for_booking.append(
            ((datetime.today() + timedelta(days=i)).strftime('%d.%m'), i)
        )

    return {
        'main_page_text': i18n.booking.creation.main.page(),
        'main_menu': i18n.cancel(),
        'days_for_booking': days_for_booking,
        'have_next': days_off < MAX_NUMBER_OF_DATES,
        'have_previous': days_off > DATES_ON_PAGE,
        'next': i18n.next(),
        'previous': i18n.previous(),
    }
