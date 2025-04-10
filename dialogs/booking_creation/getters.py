from datetime import datetime, timedelta

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from dialogs.booking_creation import consts


async def select_date_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    i18n: TranslatorRunner,
    **kwargs,
):
    page = dialog_manager.start_data.get('dates_page')
    days_on_page = []
    days_off = consts.DATES_ON_PAGE * (page + 1)

    if (
        end_range := (page + 1) * consts.DATES_ON_PAGE
    ) > consts.MAX_NUMBER_OF_DATES:
        end_range = consts.MAX_NUMBER_OF_DATES

    for i in range(consts.DATES_ON_PAGE * page, end_range):
        days_on_page.append(
            (
                (datetime.today() + timedelta(days=i)).strftime('%d.%m'),
                (datetime.today() + timedelta(days=i)).date(),
            )
        )
    return {
        'select_date_text': i18n.booking.creation.select.date(),
        'main_menu': i18n.back(),
        'days_for_booking': days_on_page,
        'have_next': days_off < consts.MAX_NUMBER_OF_DATES,
        'have_previous': days_off > consts.DATES_ON_PAGE,
        'next': i18n.next(),
        'previous': i18n.previous(),
    }


async def select_time_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    i18n: TranslatorRunner,
    **kwargs,
):
    page = dialog_manager.start_data.get('times_page')

    times_on_page = consts.BUTTONS_TIMES[
        page * consts.TIMES_ON_PAGE : (page + 1) * consts.TIMES_ON_PAGE
    ]

    return {
        'select_time_text': i18n.booking.creation.select.time(),
        'back': i18n.back(),
        'times_for_booking': times_on_page,
        'have_next': times_on_page[-1][1] + consts.TIMES_ON_PAGE
        < consts.TIME_CLOSE,
        'have_previous': times_on_page[0][1] - consts.TIMES_ON_PAGE
        >= consts.TIME_OPEN,
        'next': i18n.next(),
        'previous': i18n.previous(),
    }


async def ask_name_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    i18n: TranslatorRunner,
    **kwargs,
):
    return {'ask_name': i18n.ask.name(), 'back': i18n.back()}
