morze = {'А': '•—', 'Б': '—•••', 'В': '•——', 'Г': '——•', 'Д': '—••', 'Е': '•', 'Ё': '•',
         'Ж': '•••—', 'З': '——••', 'И': '••', 'Й': '•———', 'К': '—•—', 'Л': '•—••', 'М': '——',
         'Н': '-•', 'О': '—•', 'П': '•——•', 'Р': '•—•', 'С': '•••', 'Т': '—', 'У': '••—', 'Ф': '••—•',
         'Х': '••••', 'Ц': '—•—•', 'Ч': '———•', 'Ш': '———', 'Щ': '——•—', 'Ъ': '———•', 'Ы': '—•——',
         'Ь': '—••—', 'Э': '••—••', 'Ю': '••——', 'Я': '•—•—'
         }
# Реализация морзянки русского алфавита, не включая цифры и знаки

def input_and_morze():
    print('Какую строку хотите перевести ?')
    line = input()
    i = 0
    morze_line = str()
    for i in range(len(line)):
        morze_line = morze_line +' '+ morze.get(line[i])
    print(morze_line)


if __name__ == '__main__':
    input_and_morze()
