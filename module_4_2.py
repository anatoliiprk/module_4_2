print()
print('Домашнее задание по уроку "Пространство имён"')
print('----------')

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
print('----------')