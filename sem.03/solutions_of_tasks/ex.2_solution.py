# Задача №2
# От текста, предоставен по-долу, образувайте низа
# "Python is used to build websites and software, automate tasks, and conduct data analysis."

# За да не броим индекс по индекс ще използваме метода .index() -> връща първата позиция на
# написаната комбинация от символи в дадения низ
# Синтаксис: str.index("content in the paragraph")

paragraph = "Python is a computer programming language often used to build websites and software, " \
            "automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it " \
            "can be used to create a variety of different programs and isn't specialized for any specific problems."

print(paragraph[0:10] + paragraph[48:127])
print(paragraph.index('Python is a general'))