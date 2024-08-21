menu={"짬뽕":'7,000',"짜장면":'7,500',"탕수육 소":'21,000',"볶음밥":'7,000',"탕수육 대":'37,000',"간짜장":'8,000'}
print(menu)
selected=input("메뉴를 선택하여 주십시오.")
if selected in menu:
    print(f"해당 메뉴의 가격은 {menu[selected]}원 입니다.")
else:
    print(f"{selected}이/가 갱신되었습니다.")
    print("가격을 설정해 주십시오.(원 단위)")
    menu[selected]=input()
    print(f"현재 메뉴판은 {menu} 입니다")