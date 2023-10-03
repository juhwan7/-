name = "다빈치"
birth_year = 2010
this_year = 2023
height = 158.3
hobby = "영화 감상"
my_str3 = "{}이는 {}년 생으로 올해{}살 입니다.\
    \n{}이의 키는{}이고, 취미는 {}입니다."
print(my_str3.format(name, birth_year, (this_year - birth_year + 1), name, height, hobby))
