"""
Скачайте файл по ссылке: https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt
"""

with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(f'Длина получившейся строки: {len(content)}')
    print(f'Количество слов в тексте: {len(content.split())}')
    change_text = content.replace('.', '!')
    f_new = open('referat2.txt', 'w', encoding='utf-8')
    f_new.write(change_text)