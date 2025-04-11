intro =
    { $name }, добро пожаловать!👋

main-menu-back = Вы вернулись в главное меню 🏠

main-menu-selection = Выберите действие ⭐️:

main-menu =
    {$start_data ->
        [one] <b>{ $name }</b>, добро пожаловать!👋
        *[other] Вы вернулись в главное меню 🏠
    }

    <b>Выберите действие ⭐️</b>

booking-creation-select-date = Выберите доступную дату бронирования 📅
booking-creation-select-time = Выберите доступное время бронирования ⏰

ask-name = На чьё имя забронировать столик? 😌

incorrect-input-name =
    Некорректный ввод.
    Имя должно состоять только из букв.
    Длина должна находится в пределах 20 буквенных символов.

    Повторите попытку 🙌

no-text-input =
    К сожалению, я не понимаю 🤷‍♂️

select-person-count =
    Выберите количество персон 👥

booking-information =
    Дата и время: <b>{ $date }</b>
    Имя (на кого оформлена бронь): <b>{ $name }</b>
    Количество персон: <b>{ $persons_count }</b>

booking-confirmation =
    Проверьте правильность бронирования:

    { $booking_info }

    Все верно? ☝️

success-booking =
    Бронирование прошло успешно! 🎉

    Будем вас ждать 😇

user-booking-empty =
    У вас нет активных бронирований 🙅

    Вы можете это исправить прямо сейчас 😉📝

booking-detail-view =
    <b>{ $counter }</b>

    Информация о бронировании 📑

    { $booking_info }

booking-cancel-confirm =
    <b>Отменить бронирование? 📝</b>

    { $booking_info }

success-booking-cancel =
    Ваша бронь успешно отменена ✔

process-change-booking =
    { $booking_info }

    <b>Что бы вы хотели изменить в бронировании❓</b>