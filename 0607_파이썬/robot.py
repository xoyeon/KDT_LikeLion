while 1:
    talk = input('로봇에게 말을 해보세요 : ')
    robot = ['안녕?', '반가워', '오늘 날씨가 어때?', '오늘 날짜가 어떻게 돼?', '만나서 반가웠어']
    if talk in robot:
        if talk == '안녕?':print('안녕~')
        elif talk == '반가워': print('나도 반가워')
        elif talk == '오늘 날씨가 어때?': print('오늘 날씨는 맑아')
        elif talk == '오늘 날짜가 어떻게 돼?': print('오늘 날짜는 6월 7일 이야')
        elif talk == '만나서 반가웠어': print('그래 다음에 봐')
    else:
        print('대답할 수 없어요.')
        print('잘가')
        break