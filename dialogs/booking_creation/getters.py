from datetime import datetime, timedelta

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from dialogs.booking_creation import consts


async def select_date_getter(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    **kwargs,
):
    page = dialog_manager.start_data.get('dates_page')
    days_on_page = []
    days_off = consts.DATES_ON_PAGE * (page + 1)
    date_diff = datetime.now().hour + 1 >= consts.TIME_CLOSE
    if (
        end_range := (page + 1) * consts.DATES_ON_PAGE
    ) > consts.MAX_NUMBER_OF_DATES:
        end_range = consts.MAX_NUMBER_OF_DATES

    for i in range(consts.DATES_ON_PAGE * page, end_range):
        days_on_page.append(
            (
                (datetime.today() + timedelta(days=i + date_diff)).strftime(
                    consts.DATE_PATTERN_DISPLAY
                ),
                (datetime.today() + timedelta(days=i + date_diff)).date(),
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
    i18n: TranslatorRunner,
    **kwargs,
):
    page = dialog_manager.start_data.get('times_page')
    start_range_time = consts.TIME_OPEN
    current_hour = datetime.now().hour
    reserved_date = datetime.strptime(
        dialog_manager.dialog_data.get('reserved_date'), consts.DATE_PATTERN
    )
    if reserved_date.day == datetime.now().day and (
        current_hour > consts.TIME_OPEN
    ):
        start_range_time = current_hour + 1

    buttons_ids = [
        (f'{time}:00', time)
        for time in range(start_range_time, consts.TIME_CLOSE)
    ]
    return {
        'select_time_text': i18n.booking.creation.select.time(),
        'back': i18n.back(),
        'times_for_booking': buttons_ids,
        'have_next': buttons_ids[-1][1] + consts.TIMES_ON_PAGE
        < consts.TIME_CLOSE,
        'have_previous': all(
            [
                buttons_ids[0][1] - consts.TIMES_ON_PAGE >= consts.TIME_OPEN,
                buttons_ids[0][1] > current_hour + 1,
            ]
        ),
        'next': i18n.next(),
        'previous': i18n.previous(),
    }


async def ask_name_getter(
    i18n: TranslatorRunner,
    **kwargs,
):
    return {'ask_name': i18n.ask.name(), 'back': i18n.back()}


async def select_persons_getter(
    i18n: TranslatorRunner,
    **kwargs,
):
    count_persons = [(num, num) for num in range(1, consts.RANGE_PERSONS + 1)]
    return {
        'select_persons_count': i18n.select.person.count(),
        'back': i18n.back(),
        'count_persons': count_persons,
    }


async def confirm_booking_getter(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    **kwargs,
):
    name = dialog_manager.dialog_data.get('reservation_name')
    reserved_data = dialog_manager.dialog_data.get('reserved_date')
    reserved_time = dialog_manager.dialog_data.get('reserved_time')
    persons_count = dialog_manager.dialog_data.get('person_count')

    booking_info = i18n.booking.information(
        name=name,
        date=f'{reserved_data} {reserved_time}',
        persons_count=persons_count,
    )

    return {
        'confirm_booking_text': i18n.booking.confirmation(
            booking_info=booking_info
        ),
        'not_confirm': i18n.click.no(),
        'confirm': i18n.click.yes(),
    }


async def success_booking_getter(
    i18n: TranslatorRunner,
    **kwargs,
):
    return {
        'success_booking_text': i18n.success.booking(),
        'back_to_main_menu': i18n.back.to.main.menu(),
    }
