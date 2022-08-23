import string
import random
import time
  
categories = {
    'user' : ['USER_ID', 'AGE', 'GENDER', 'MEMBERSHIP_STATUS'],
    'item' : ['ITEM_ID', 'PRICE', 'CATEGORY_L1', 'CATEGORY_L2', 'CATEGORY_L3', 'AGE', 'GENDER', 'TIMESTAMP', 'RATING'],
    'user-item' : ['USER_ID', 'ITEM_ID', 'TIMESTAMP', 'EVENT_TYPE']
}

# USER
# user_id
length_user_id = 5
number_user_id = 100
list_user_id = []
timestamp = str(int(time.time()))

for x in range(number_user_id):
    list_user_id.append(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_user_id)))

# age
ages = [10, 20, 30, 40, 50, 60]
random_ages = random.choices(ages, [10, 20, 50, 50, 20, 10], k=number_user_id)
list_age = list(map(str,[i for i in random_ages]))

# gender
genders = ['M', 'F']
list_gender = random.choices(genders, [40, 60], k=number_user_id)

# membership
memberships = [1, 2, 3, 4, 5, 6]
list_membership = list(map(str,(random.choices(memberships, [30, 20, 15, 10, 5, 5], k=number_user_id))))

with open('data_user.csv', 'w') as f:
    f.write(','.join(categories['user']) + '\n') # Category
    
    for item in  zip(list_user_id, list_age, list_gender, list_membership):
        f.write(','.join(item) + '\n')
    
# ITEM
list_product_category = [
    ['가공식품', '조미료', '종합조미료'],
    ['가공식품', '조미료', '소스'],
    ['가공식품', '조미료', '장류'],
    ['가공식품', '조미료', '향신료'],
    ['가공식품', '조미료', '유지류'],
    ['가공식품', '유제품', '우유'],
    ['가공식품', '유제품', '요구르트'],
    ['가공식품', '유제품', '유가공품'],
    ['가공식품', '축산가공식품', '햄'],
    ['가공식품', '축산가공식품', '조미육가공'],
    ['가공식품', '축산가공식품', '기타'],
    ['가공식품', '수산가공식품', '건어물'],
    ['가공식품', '수산가공식품', '해조류'],
    ['가공식품', '수산가공식품', '기타'],
    ['가공식품', '대용식재료', '면류'],
    ['가공식품', '대용식재료', '기타'],
    ['가공식품', '통조림', '농산물'],
    ['가공식품', '통조림', '수산물'],
    ['가공식품', '통조림', '축산물'],
    ['가공식품', '통조림', '기타'],
    ['일상용품', '위생용품', '면도위생용품'],
    ['일상용품', '화장품', '스킨케어화장품'],
    ['일상용품', '화장품', '메이크업화장품'],
    ['일상용품', '화장품', '헤어케어화장품'],
    ['일상용품', '화장품', '네일케어화장품'],
    ['일상용품', '화장품', '면도용화장품'],
    ['일상용품', '화장품', '방향용화장품'],
    ['일상용품', '화장품', '체취방지용화장품'],
    ['일상용품', '화장품', '남성화장품'],
]
list_ITEM_ID = []
list_food_line = []
list_beauty_line = []
with open('data_food.txt', 'r') as f:
    lines = f.readlines()
    list_product_line = list(map(lambda s: s.strip(), lines))

with open('data_beauty.txt', 'r') as f:
    lines = f.readlines()
    list_beauty_line.extend(list(map(lambda s: s.strip(), lines)))
        
with open('data_item.csv', 'w') as f:
    f.write(','.join(categories['item']) + '\n') # Category
    
    idx = 0
    
    for line in list_product_line:
        category = list_product_category[idx]
        for product in line.split(','):
            product = product.strip()
            list_ITEM_ID.append(product)
            f.write(','.join([product, '1000', category[0], category[1], category[2], '0', 'null', timestamp, str(random.randint(1, 5))]) + '\n')
        idx += 1

    for line in list_beauty_line:
        category = list_product_category[idx]
        for product in line.split(','):
            gender = 'M' if '남성' in product else 'F'
            product = product.strip()
            list_ITEM_ID.append(product)
            f.write(','.join([product, '1000', category[0], category[1], category[2], str(random.choice([10, 20, 30, 40, 50, 60])), gender, timestamp, str(random.randint(1, 5))]) + '\n')
        idx += 1

# USER_ITEM
length_user_item = 20000
event_type = ['View', 'AddToCart', 'Purchase', 'Search']
list_event_type = random.choices(event_type, [50, 20, 10, 20], k=length_user_item)
list_user_id = random.choices(list_user_id, k=length_user_item)
list_ITEM_ID = random.choices(list_ITEM_ID, k=length_user_item)

with open('data_user-item.csv', 'w') as f:
    f.write(','.join(categories['user-item']) + '\n') # Category
    
    for item in  zip(list_user_id, list_ITEM_ID, [timestamp for _ in range(length_user_item)], list_event_type):
        f.write(','.join(item) + '\n')    
