def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
    except Exception as e:
        print(f"Файл {file_name} не був відкритий! Помилка: {e}")
        return None
    else:
        print(f"Файл {file_name} був відкритий!")
        return file

#частина а: Створення файлу TF26_1 з рядками латинських букв різної довжини.
file1_name = "TF26_1.txt"
file2_name = "TF26_2.txt"

file_1_w = open_file(file1_name, "w")
if file_1_w:
    file_1_w.write("Hello\nWorld\nPython\nProgramming\nis\nFUN")
    print("Інформація була успішно додана до TF26_1.txt!")
    file_1_w.close()
    print("Файл TF26_1.txt був закритий!")

#частина б: Читання вмісту TF26_1, заміна великих літер на малі, запис у TF26_2.
file_1_r = open_file(file1_name, "r")
file_2_w = open_file(file2_name, "w")

if file_1_r and file_2_w:
    content = file_1_r.read().lower()  #замінюємо великі літери на малі.
    file_2_w.write(content)
    print("Вміст з малими літерами був успішно записаний до TF26_2.txt!")
    file_1_r.close()
    file_2_w.close()
    print("Файли TF26_1.txt та TF26_2.txt були закриті!")

#частина в: Читання вмісту TF26_2 і виведення його по рядках.
file_2_r = open_file(file2_name, "r")
if file_2_r:
    print("Вміст файлу TF26_2.txt:")
    for line in file_2_r:
        print(line.strip())
    file_2_r.close()
    print("Файл TF26_2.txt був закритий!")
