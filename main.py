import csv
import re


def write_holiday_cities(first_letter):
    have_visit = set()
    wish_visit = set()
    list_travel = []


    with (open('travel-notes.csv', 'r', newline='', encoding='UTF8') as file_read):
        reader = csv.reader(file_read)

        for list in reader:

            if list[0].startswith(first_letter):
                param = r"\w+(?:(?:[^;]*\[[^][]*])+[^;]*|[^;']+)"
                list_travel.append(list)

                city = re.findall(param, list[1])
                for cities in city:
                    have_visit.add(cities)
                print(have_visit)

                city = re.findall(param, list[2])
                for cities in city:
                    wish_visit.add(cities)
                    print(wish_visit)


    all_cities = have_visit.union(wish_visit)
    don_visit = (all_cities.difference(have_visit))
    next_visit = sorted(don_visit)[0]

    with (open('holiday.csv', 'w', newline='', encoding='UTF8') as file_out):
        w = csv.writer(file_out)
        w.writerow([f' Города,в которых студенты с именем на {first_letter} уже были '.join(sorted(have_visit))])
        w.writerow(['Города, которые студенты хотят посетить:'.join(sorted(wish_visit))])
        w.writerow(['Посетят следующим:', next_visit])
        w.writerow(['В этих городах студенты еще не были'.join(sorted(don_visit))])


letter = 'Lisa'
city_letter = write_holiday_cities(letter)




