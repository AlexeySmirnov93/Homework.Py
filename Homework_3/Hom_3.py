# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.
# Ввод:
# текст отсюда(https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%80%D0%BB%D0%B8,_%D0%A1%D0%B8%D0%BB%D1%8C%D0%B2%D0%B0%D0%BD%D1%83%D1%81)

# Вывод:

# Слово "в", 22 раз
# Слово "и", 11 раз
# Слово "году", 9 раз
# Слово "с", 4 раз
# Слово "морли", 4 раз
# Слово "по", 3 раз
# Слово "степень", 3 раз
# Слово "института", 3 раз
# Слово "был", 3 раз
# Слово "памятников", 3 раз

import re
from collections import Counter

text = """Сильва́нус Гри́зуолд Мо́рли (англ. Sylvanus Griswold Morley; 1883—1948) — американский археолог, эпиграфист и майянист, 
внёсший значительный вклад в изучение доколумбовой цивилизации майя в первой половине XX века.
Его учениками являлись Татьяна Проскурякова и Эрик Томпсон[2]. 
Кроме того, в 1917—1919 годах Морли был агентом американского военно-морского министерства в Мексике, Гондурасе и Никарагуа, 
расследуя деятельность немецких шпионов и антиамериканскую деятельность, из-за чего подвергся нападкам со стороны Ф. 
Боаса за «профанацию науки», служившей прикрытием для контрразведки[3].
Будущий майянист родился в семье преподавателя химии Пенсильванского военного колледжа[en]; 
по воле отца в 1904 году получил степень бакалавра гражданской инженерии. 
После смерти родителя поступил в Гарвардский университет, где изучал антропологию и египтологию. 
С детства интересуясь цивилизациями Центральной Америки, в университете он обратился к изучению американистики, 
получив по этой специальности магистерскую степень (1908) и членство Американского института архитекторов,
но докторскую диссертацию так и не защитил (в 1921 году Пенсильванский военный колледж присвоил ему докторскую степень honoris causa). 
Первые полевые исследования Морли провёл в Нью-Мексико и был связан с этим штатом всю последующую жизнь. 
В 1910—1912 годах вёл раскопки в Киригуа, там же впервые проводил реставрацию памятников Древней Америки (в 1935 году выпустил путеводитель по руинам). 
В 1921 году удостоен почётного гражданства муниципалитета Санта-Роса-де-Копан. 
В 1914 году впервые вёл работы в Чичен-Ице на средства Института Карнеги, до 1929 года руководил археологическим отделом Института, 
определяя его программу, в 1924—1940 годах возглавлял стационарную экспедицию на городище Чичен-Ицы. 
В 1916 году открыл руины Вашактуна — одного из древнейших городов майя. 
Параллельно С. Морли начал программу всестороннего изучения надписей майя, лично занимаясь поиском и съёмкой эпиграфических памятников. 
В 1915 году опубликовал «Введение в изучение иероглифов майя», 
и в 1920-м «Надписи Копана» — первую сводную публикацию эпиграфических памятников с одного городища; 
в 1937—1938 году выпустил пятитомные «Надписи Петена», за которые был удостоен гватемальского Ордена Кетцаля и премии Колумбийского университета. 
Морли интересовался хронологией, отождествил иероглифы, обозначающие 360-дневный цикл (тун), его начало и завершение, и циклы в пять и десять тунов. 
В 1930-е годы широко занимался популяризацией культуры древних майя. 
Его обобщающая книга «Древние майя» (1946) заложила стандарт подобного рода публикаций и переиздавалась шесть раз, 
не считая перевода на испанский язык[4]. В 1947 году Сильванус Морли был назначен директором Музея Нью-Мексико в Санта-Фе.
Скончался от сердечного заболевания."""

words = re.findall(r'\b\w+\b', text.lower())
new_text = Counter(words).most_common(10)
print(new_text)
for i in new_text:
    print(f'Слово: {str(*[i])[1:-1]} раз')