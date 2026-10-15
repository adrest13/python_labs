from src.lib.text import normalize, tokenize, count_freq, top_n

text = open(0, encoding='UTF-8').read()
if text.strip() == '':
    raise ValueError('There is no code')
flag = 0    #для задачи со звездочкой


normal = normalize(text)
tokens = tokenize(normal)
cnt = count_freq(tokens)
top = top_n(cnt)


print(f'''
Всего слов: {len(tokens)}
Уникальных слов: {len(cnt)}
Топ-5:''')
if not(flag): # для задачи А
    for tops in top:
        print(f'{tops[0]}:{tops[1]}')
else:   #для задачи со звездочкой
    mx_len = max(max([len(x[0]) for x in top]), len('слово'))
    print(f'{"слово":<{mx_len}} | частота')
    print('-' * len(f'{"слово":<{mx_len}} | частота'))
    for x in top:
        print(f'{x[0]:<{mx_len}} | {x[1]}')
    print('...')