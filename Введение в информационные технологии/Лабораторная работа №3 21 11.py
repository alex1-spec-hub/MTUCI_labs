print('выбирите тип чтения:"построчное" "цельное"')
read=input()
read2=input()
read3='цельное'
read4='построчное'
if read2==read3:
    def read_file(filename):
        with open(filename, 'r') as file:
            content = file.read()
        return content
print(read_file('example.txt'))
if read==read4:
    def read_file(filename):
        with open('example.txt', 'r') as file:
            for line in file:
                return line
print(read_file('example.txt'))
if read!=read4 or read2!=read3:
    print('ошибка')

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def read_line(filename):
    with open(filename, 'r') as file:
        for line in file:
            return line

print('выберите тип чтения: "построчное" "цельное"')
r1=int(input())
r3=('построчное')
r4=('цельное')
if r1 == 1:
    print(read_file('example.txt'))
elif r1 == 2:
    print(read_line('example.txt'))
else:
    print("sdasdasd")
