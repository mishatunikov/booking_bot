from datetime import datetime, timedelta

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from .consts import MAX_NUMBER_OF_DATES, DATES_ON_PAGE


async def select_date_getter(
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
            (
                (datetime.today() + timedelta(days=i)).strftime('%d.%m'),
                (datetime.today() + timedelta(days=i)).date(),
            )
        )
    return {
        'select_date_text': i18n.booking.creation.select.date(),
        'main_menu': i18n.back(),
        'days_for_booking': days_for_booking,
        'have_next': days_off < MAX_NUMBER_OF_DATES,
        'have_previous': days_off > DATES_ON_PAGE,
        'next': i18n.next(),
        'previous': i18n.previous(),
    }
