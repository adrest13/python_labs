import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''
    This function normalizes the text
        
    Input data: str
    Output data: str
    '''
    text1 = text
    if casefold:
        text1 = text1.casefold()
    else:
        text1 = text1.lower()
    if yo2e:
        text1 = text1.replace('ё', 'е').replace('Ё', 'Е')
    text1 = ' '.join(text1.split())
    return text1

def tokenize(text: str) -> list[str]:
    '''
    This function splits the text based on non-alphanumeric indicators
            
    Input data: str
    Output data: list[str]
    '''
    return re.findall(r'\w+(?:-\w+)*', text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    '''
    This function counts simbols
            
    Input data: list[str]
    Output data: dict[str, int]
    '''
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    '''
    This function sorts dict's first n elements
    Input data: dict[str, int]
    Output data: list[tuple[str, int]]
    '''
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]

if __name__ == '__main__':
    # normalize
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"

    # tokenize
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]

    # count_freq + top_n
    freq = count_freq(["a","b","a","c","b","a"])
    assert freq == {"a":3, "b":2, "c":1}
    assert top_n(freq, 2) == [("a",3), ("b",2)]

    # тай-брейк по слову при равной частоте
    freq2 = count_freq(["bb","aa","bb","aa","cc"])
    assert top_n(freq2, 2) == [("aa",2), ("bb",2)]

    print("Accepted")

    print(fr'''
    normalize
    "ПрИвЕт\nМИр\t" -> {normalize("ПрИвЕт\nМИр\t")}
    "ёжик, Ёлка" -> {normalize("ёжик, Ёлка")}
    "Hello\r\nWorld" -> {normalize("Hello\r\nWorld")}
    "  двойные   пробелы  " -> {normalize("  двойные   пробелы  ")}
    ''')

    print(fr'''
    tokenize
    "привет мир" -> {tokenize("привет мир")}
    "hello,world!!!" -> {tokenize("hello,world!!!")}
    "по-настоящему круто" -> {tokenize("по-настоящему круто")}
    "2025 год" -> {tokenize("2025 год")}
    "emoji 😀 не слово" -> {tokenize("emoji 😀 не слово")}
    ''')

    print(fr'''
    count_freq + top_n
    Токены ["a","b","a","c","b","a"] -> частоты {count_freq(["a", "b", "a", "c", "b", "a"])};
    top_n(..., n=2) -> {top_n(count_freq(["a", "b", "a", "c", "b", "a"]), 2)}
    При равенстве частот: токены ["bb","aa","bb","aa","cc"] -> {count_freq(["bb", "aa", "bb", "aa", "cc"])};
    top_n(..., n=2) → {top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), 2)}
    ''')