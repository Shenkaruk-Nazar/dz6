import inspect
import colorama
print("--------------------Провірка чи є colorama модулем--------------------")
print(inspect.ismodule(colorama))
print("--------------------Провірка чи є colorama классом--------------------")
print(inspect.isclass(colorama))
print("--------------------Провірка чи є colorama функцією--------------------")
print(inspect.isfunction(colorama))
print("--------------------Дослідження імені--------------------")
print(colorama.__name__)
print("--------------------Дізнатись всі атрибути та методи--------------------")
for method in dir(colorama):
    print(method)
print("--------------------Наявність атрибуту чи методу--------------------")
print(hasattr(colorama, 'reverse'))
print(hasattr(colorama, 'index'))