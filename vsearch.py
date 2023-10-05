def search4vowels(word: str) -> set:
    """Возвращает гласные найденные в указаном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Возвращает множество букв из letters,
    в указанной фразе."""
    return set(letters).intersection(set(phrase))
