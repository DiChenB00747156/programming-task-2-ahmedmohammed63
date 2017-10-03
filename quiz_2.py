with open('Crime.csv','r+') as f:
     f_contents = f.readlines()
     count_a = 0
     count_b = 0
     count_c = 0
     count_d = 0
     for line in f_contents:
         s = line.split(',')
         my_dict = dict()
         key_1 = "ASSAULT\n"
         key_2 = "THEFT OF VEHICLE\n"
         key_3 = "THEFT FROM VEHICLE\n"
         key_4 = "BREAK AND ENTER\n"
         if key_1 in s:
            count_a += 1
            crime_code_a = s[-2]
         elif key_2 in s:
            count_b += 1
            crime_code_b = s[-2]
         elif key_3 in s:
            count_c += 1
            crime_code_c = s[-2]
         elif key_4 in s:
            count_d += 1
            crime_code_d = s[-2]
     my_dict[key_1] = crime_code_a, count_a
     my_dict[key_2] = crime_code_b, count_b
     my_dict[key_3] = crime_code_c, count_c
     my_dict[key_4] = crime_code_d, count_d
     print(my_dict)
