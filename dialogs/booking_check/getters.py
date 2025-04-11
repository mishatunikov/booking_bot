from aiogram.types import User

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User as UserModel, Reserve
from dialogs.consts import PATTERN_DATE


async def main_page_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    i18n: TranslatorRunner,
    user: UserModel,
    **kwargs,
):
    reserves = user.reserves
    booking_exist = bool(reserves)
    booking_not_exist = not booking_exist
    booking_number = dialog_manager.start_data.get('booking_number')
    booking_info = booking_detail_info = None

    if booking_exist:
        reserve: Reserve = reserves[booking_number]
        booking_info = i18n.booking.information(
            date=f'<b>{reserve.reservation_time.strftime(PATTERN_DATE)}</b>',
            name=f'<b>{reserve.reservation_name}</b>',
            persons_count=f'<b>{reserve.person_count}</b>',
        )
        booking_detail_info = i18n.booking.detail.view(
            counter=f'<b>{booking_number + 1}/{len(reserves)}</b>',
            booking_info=booking_info,
        )
        dialog_manager.dialog_data.update(
            {
                'selected_booking_info': booking_info,
                'selected_reverse_id': reserve.id,
            }
        )
    else:
        booking_detail_info = i18n.user.booking.empty()

    return {
        'booking_detail_info': booking_detail_info,
        'previous': i18n.previous(),
        'next': i18n.next(),
        'cancel': i18n.cancel.booking(),
        'have_next': len(reserves) - 1 > booking_number,
        'have_previous': booking_number,
        'booking_exist': booking_exist,
        'back': i18n.back(),
    }


async def confirm_cancel_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    i18n: TranslatorRunner,
    user: UserModel,
    **kwargs,
):

    return {
        'cancel_confirmation_text': i18n.booking.cancel.confirm(
            booking_info=dialog_manager.dialog_data.get(
                'selected_booking_info'
            )
        ),
        'confirm_cancel': i18n.click.yes(),
        'not_confirm_cancel': i18n.click.no(),
    }


async def success_cancel_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    i18n: TranslatorRunner,
    **kwargs,
):
    return {
        'success_cancel_booking': i18n.success.booking.cancel(),
        'back_to_main_menu': i18n.back.to.main.menu(),
    }
