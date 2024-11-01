text = "а ну тут крч текст я че знаю где тут надо буквы а ставить"

first_a_index = text.find('а')
last_a_index = text.rfind('а')

substring = text[first_a_index + 1:last_a_index]

reversed_substring = substring[::-1]

result = text[:first_a_index + 1] + reversed_substring + text[last_a_index:]

print(result)
