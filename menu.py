import random


def get_food_list(current_weather):
  rain = "파전,부대찌개,칼국수,수제비,우동,잔치국수,해물탕,아구찜".split(',')
  sunny = "스테이크,피자,햄버거,스파게티,샌드위치,반미,덮밥,스시".split(',')

  if current_weather['main'] == 'Rain':
    food_list = random.sample(rain, k=len(rain))
  else:
    food_list = random.sample(sunny, k=len(sunny))

  return food_list
