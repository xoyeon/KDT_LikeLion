# top1 = 'toto'
# def nameprint():
#     # global top2
#     top2 = 'banana'
#     print("지역 탑 :", top2)
#
# nameprint()
# print("전국 탑 :", top2)

top3 = 'toto'
def nameprint():
    global top3
    top3 = 'banana'
    print("지역 탑 : ", top3)

nameprint()
print("전국 탑 :", top3)