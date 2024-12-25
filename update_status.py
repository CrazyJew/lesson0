


status_dict = {"1" : "Выполнено", "2" : "Отложено", "3" : "В процессе"}
print(*status_dict.items())
status = input("Выберите статус заметки из предложенных выше нажав соотвествующию цифру: ")
while True:
    if status in "1":
        status = status_dict["1"]
        print(status)
    elif status in "2":
        status = status_dict["2"]
        print(status)
    elif status in "3":
        status = status_dict["3"]
        print(status)
    else:
        print("некоректный ввод")
        continue


