file1 = 'Renn Qin on Behance.png'
backup = "Renn Qin on Behance_back.png"
infile = open(file1,'rb')
outfile = open(backup,'wb')
while True :
    copy_buffer = infile.read(1024)
    if not copy_buffer :   # 읽어올 내용이 없으면(이미지내용)
       break
    outfile.write(copy_buffer)

infile.close()
outfile.close()
print("복사완료")