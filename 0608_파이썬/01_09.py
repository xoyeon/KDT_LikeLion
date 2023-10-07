file = open('자기소개.txt', 'r', encoding = 'utf-8')
lines = file.readlines()
str_lines = str(lines)
for i in lines:
    print(i, end='')
word = input('\n\n찾으려는 단어를 입력하세요 : ')
# print(str_lines)
split_lines = str_lines.split()
count = 0
for i in range(len(split_lines)):
    if word in split_lines[i]:
        count += 1
print('찾으려는 단어는', count, '개 입니다.')
file.close()