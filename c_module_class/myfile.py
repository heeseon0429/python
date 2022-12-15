# import  mymodule

# print('오늘의 날씨 : ', mymodule.get_weather())
# print('오늘은 ', mymodule.get_date(), '요일입니다')


# import  mymodule as mm

# print('오늘의 날씨 : ', mm.get_weather())
# print('오늘은 ', mm.get_date(), '요일입니다')


from mypackage.mymodule import get_weather, get_date

print('오늘의 날씨 : ', get_weather())
print('오늘은 ', get_date(), '요일입니다')