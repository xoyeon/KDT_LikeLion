all_data = []
for i in range(2, 9):
    tmp = '//*[@id="country-table"]/div/div/table/tbody/tr/td[{}]'.format(i)
    # print(tmp)
    sel_ele = driver.find_elements_by_xpath(tmp)

    column_data = []
    for one in sel_ele:
        # print(one.text)
        column_data.append(one.text)

    print(len(sel_ele))
    all_data.append(column_data)
    print(column_data)
    print()

all_data