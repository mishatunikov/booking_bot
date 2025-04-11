from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner


async def update_booking_getter(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    **kwargs,
):
    booking_info = dialog_manager.start_data.get('selected_booking')

    return {
        'update_booking_text': i18n.process.change.booking(
            booking_info=booking_info
        ),
        'update_date': i18n.update.date(),
        'update_time': i18n.update.time(),
        'update_persons_count': i18n.update.count.person(),
        'update_name': i18n.update.name(),
        'cancel_update': i18n.cancel(),
    }
