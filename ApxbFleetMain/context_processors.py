from django.conf import settings
from django.utils.translation import get_language_info


def language_info(request):
    language_code = request.LANGUAGE_CODE
    language_info = get_language_info(language_code)
    return {
        'current_language_info': language_info,
    }


def language_info_list(request):
    language_list = []
    for code, language in settings.LANGUAGES:
        try:

            language_list.append({
                'code': code,
                'name': language,

            })
        except KeyError:
            # Handle unknown language code
            language_list.append({
                'code': code,
                'name': 'IsiNdebele',

            })
    return language_list
