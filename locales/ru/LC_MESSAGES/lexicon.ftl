intro =
    { $name }, добро пожаловать!👋

main-menu-back = Вы вернулись в главное меню 🏠

main-menu-selection = Выберите действие ⭐️:

main-menu =
    {$start_data ->
        [one] { $name }, добро пожаловать!👋
        *[other] Вы вернулись в главное меню 🏠
    }

    Выберите действие ⭐️

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

booking-confirmation =
    Проверьте правильность бронирования:

    Дата и время: { $date }
    Имя (на кого оформлена бронь): { $name }
    Количество персон: {$persons_count}

    Все верно? ☝️

success-booking =
    Бронирование прошло успешно! 🎉
    Будем вас ждать 😇

user-booking-empty =
    У вас нет активных бронирований 🙅

    Вы можете это исправить прямо сейчас 😉📝


booking-information =
    Дата и время: { $date }
    Имя (на кого оформлена бронь): { $name }
    Количество персон: {$persons_count}

booking-detail-view =
    { $counter }

    Информация о бронировании 📑

    { $booking_info }

booking-cancel-confirm =
    <b>Отменить бронирование? 📝</b>

    { $booking_info }

success-booking-cancel =
    Ваша бронь успешно отменена ✔