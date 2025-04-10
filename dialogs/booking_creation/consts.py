DATES_ON_PAGE = 3
MAX_NUMBER_OF_DATES = 7

TIMES_ON_PAGE = 6
TIME_OPEN = 10
TIME_CLOSE = 22

WIDTH_TIME_BUTTONS = 3

BUTTONS_TIMES: list[tuple[str, int]] = [
    (f'{time}:00', time) for time in range(TIME_OPEN, TIME_CLOSE)
]
