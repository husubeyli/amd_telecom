import string
from unidecode import unidecode


def slugify(title):
    symbol_mapping = (
        ('ə', 'e'),
        ('ı', 'i'),
        ('ö', 'o'),
        ('ğ', 'g'),
        ('ü', 'u'),
        ('ş', 's'),
        ('ç', 'c'),
        (' ', '-'),
    )
    # print(title.get('title'), 'cina')
    print(type(title), 'cina')
    title_url = title.strip().lower()
    for before, after in symbol_mapping:
        title_url = title_url.replace(before, after)
    for symbol in title_url:
        if symbol in string.punctuation:
            title_url = title_url.replace(symbol,'-')
    title_url = title_url.strip('-')
    title_url_list = list(title_url)
    for i in range(len(title_url_list)):
        if title_url_list[i] == '-' and title_url_list[i+1] == '-':
            title_url_list[i] = ''
    title_url = ''.join(title_url_list)
    return unidecode(title_url)