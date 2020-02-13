'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

mounth = (Jan, Feb, Marc, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec)
season_list = ['winter': 0, 
               'spring': 1, 
               'summer': 2, 
               'autum': 3]

while True:
  user_mounth_num = input 'Введите номер месяца'
  try:
    user_mounth_num = int(user_mounth_num)
    if user_mounth_num > 12 or user_month_num < 0:
  except:
    print 'Ошибка введенных данных'
    continue

season_idx = user_mounth_num // 3 % 4
for key, value in season_list.items():
  if user_mount_num in value:
    print key
  break
