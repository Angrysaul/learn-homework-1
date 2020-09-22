# """

# Домашнее задание №1

# Цикл for: Оценки

# * Создать список из словарей с оценками учеников разных классов 
#   школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# * Посчитать и вывести средний балл по всей школе.
# * Посчитать и вывести средний балл по каждому классу.
# """


# средний балл по каждому классу = sum['scores']/len['scores'] = avg_class
# средний балл по школе = sum(avg_class) from school_list/ их количество
# dict_scores = school_list для всех словарей в списке, в скобках указываем нужный ключ

school_list = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '5a', 'scores': [3,4,3,4,1]},
    {'school_class': '6a', 'scores': [2,4,4,3,2]},
]
def avg_class(scores_list):
    list_sum = 0
    for score in scores_list:
        list_sum +=score
    score_avg = list_sum/len(scores_list)
    return(score_avg)

school_avg = 0
for dict_scores in school_list:
    mark_avg = avg_class(dict_scores['scores'])
    class_name = dict_scores['school_class']
    school_avg += mark_avg
    print(f"Класс {class_name}: средний балл: {mark_avg}")
school_mean = school_avg/len(school_list)    
print(f"Средний балл по школе: {school_mean}")    

# avg_score = sum(school_list[0]['scores'])/len(school_list[0]['scores'])


# if __name__ == "__main__":
#     main()
