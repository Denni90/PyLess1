# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def is_str(x):
    xyz = ["X", "Y", "Z"]
    lst = [input(f"Введите значение {xyz[i]}: ") for i in range(x)]
    return lst


def is_predicante(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

statement = is_str(3)

if is_predicante(statement) == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")