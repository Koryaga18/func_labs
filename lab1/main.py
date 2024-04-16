def find_longest_string(strings):
    filtered_strings = filter(lambda s: len(s) > 10, strings)
    longest_string = max(filtered_strings, key=len)
    return longest_string

input_strings = ["Мало", "Не Очень Мало", "Уже Побольше Символов", "Очень Много Символов В Этой Строке"]
result = find_longest_string(input_strings)

if result:
    print("Самая длинная строка:", result)
else:
    print("Нет строк длиннее 10 символов.")
