#task 1 , result: 15750
# import find_number_of_people
# import d_load_csv

# matura = d_load_csv.load_csv('matura.csv')
# print(find_number_of_people.proceed_in_year(matura,region = "Lubuskie", passs = "przystąpiło", year = "2018" ))


#task 2, result: 77879
# import find_number_of_people
# import d_load_csv

# matura = d_load_csv.load_csv('matura.csv')
# print(find_number_of_people.proceed_all_years(matura,region = "Lubuskie", passs = "przystąpiło", sex = "both"))


#task 3, result: 61883
# import find_number_of_people
# import d_load_csv

# matura = d_load_csv.load_csv('matura.csv')
# print(find_number_of_people.pass_all_years(matura,region = "Lubuskie", passs = "zdało", sex = "both"))


#task 4, result: 79.46 %
import find_number_of_people
import d_load_csv

matura = d_load_csv.load_csv('matura.csv')
print(find_number_of_people.proceed_vs_pass(matura,region = "Lubuskie"))