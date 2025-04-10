from fluent_compiler.bundle import FluentBundle

from fluentogram import TranslatorHub, FluentTranslator


def create_translator_hub() -> TranslatorHub:
    """Создает объект TranslatorHub."""
    translator_hub = TranslatorHub(
        {
            'ru': ('ru',),
        },
        [
            FluentTranslator(
                locale='ru',
                translator=FluentBundle.from_files(
                    locale='ru-RU',
                    filenames=[
                        'locales/ru/LC_MESSAGES/lexicon.ftl',
                        'locales/ru/LC_MESSAGES/buttons.ftl',
                    ],
                ),
            ),
        ],
        root_locale='ru',
    )

    return translator_hub
