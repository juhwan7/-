name = "다빈치"
birth_year = 2010
this_year = 2023
height = 158.3
hobby = "영화 감상"
my_str2 = "%s이는 %s년생으로 올해 %d살 입니다. \
        \n%s이의 키는 %s이고, 취미는 %s입니다."

print(my_str2 % (name, birth_year, (this_year - birth_year + 1), name, height, hobby))

# 다빈치이는 2010년생으로 올해 14살 입니다.
# 다빈치이의 키는 158.300000이고, 취미는 영화 감상입니다.
