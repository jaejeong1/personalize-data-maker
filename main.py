import string
import random
import time

categories = { # 데이터 전체 카테고리
    'user' : ['USER_ID', 'AGE', 'GENDER'],
    'item' : ['ITEM_ID', 'PRICE', 'CATEGORY_L1', 'CATEGORY_L2', 'CATEGORY_L3', 'AGE', 'GENDER', 'TIMESTAMP', 'RATING'],
    'user-item' : ['USER_ID', 'ITEM_ID', 'TIMESTAMP']
}

# USER
# user_id
length_user_id = 5 # 생성될 user id의 길이
number_user_id = 100 # 생성될 user id의 갯수
list_user_id = []
timestamp = str(int(time.time()))

for x in range(number_user_id): # 랜덤 문자열(영문+숫자) 생성해 user id로 만듬
    list_user_id.append(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_user_id)))

# age
ages = [10, 20, 30, 40, 50, 60] # 연령대는 10 ~ 60 범위
random_ages = random.choices(ages, [10, 20, 50, 50, 20, 10], k=number_user_id) # 생성될 user id의 갯수만큼 10~60 범위에서 샘플링
list_age = list(map(str,[i for i in random_ages]))

# gender
genders = ['M', 'F']
list_gender = random.choices(genders, [40, 60], k=number_user_id)

# membership
# memberships = [1, 2, 3, 4, 5, 6]
# list_membership = list(map(str,(random.choices(memberships, [30, 20, 15, 10, 5, 5], k=number_user_id))))

with open('data_user.csv', 'w') as f:
    f.write(','.join(categories['user']) + '\n') # Category
    
    for item in  zip(list_user_id, list_age, list_gender):
        f.write(','.join(item) + '\n')
    
# ITEM
list_scent = [
    "Bergamot", "Grapefruit", "Yuja", "Lavender", "Rosemary", "Verbena", "Recharging", "Sandalwood", "Pine", "Relaxing", "Neroli"
]
list_ITEM_ID = []

with open('data_item.csv', 'w') as f:
    f.write(','.join(categories['item']) + '\n') # Category

    for scent in list_scent:
        list_ITEM_ID.append(scent)
        f.write(','.join([scent, '1000', scent, '0', 'null', timestamp, str(random.randint(1, 5))]) + '\n')

# USER_ITEM
length_user_item = 20000
# 실사용 환경 조성위해 이벤트 종류를 가중치를 두어 샘플링
list_user_id = random.choices(list_user_id, k=length_user_item)
list_ITEM_ID = random.choices(list_ITEM_ID, k=length_user_item)

with open('data_user-item.csv', 'w') as f:
    f.write(','.join(categories['user-item']) + '\n') # Category
    
    for item in  zip(list_user_id, list_ITEM_ID, [timestamp for _ in range(length_user_item)]):
        f.write(','.join(item) + '\n')    
