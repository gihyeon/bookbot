def get_num_words(text: str) -> str:
    return len(text.split())


def get_num_chars_dict(text: str) -> dict:
    text_lower = text.lower()
    unique_chars = set(text_lower)
    num_chars = {}
    
    for char in unique_chars:
        num_chars[char] = text_lower.count(char)

    return num_chars


def sort_on_num(d: dict) -> int:
        return d['num']


def get_num_chars_list(num_chars: dict) -> list:
    num_chars_list = []
    for char in num_chars:
        num_chars_list.append({'char': char, 'num': num_chars[char]})
    
    num_chars_list.sort(reverse=True, key=sort_on_num)
    return num_chars_list
