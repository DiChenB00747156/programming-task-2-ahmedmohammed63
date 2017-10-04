with open('Crime.csv','r+') as f:
     f_contents = f.readlines()
     count_a_1 = 0
     count_a_2 = 0
     count_a_3 = 0
     count_b = 0
     count_c_1 = 0
     count_c_2 = 0
     count_d = 0
     for line in f_contents:
         s = line.split(',')
         my_dict = dict()
         key_1 = "ASSAULT\n"
         key_2 = "THEFT OF VEHICLE\n"
         key_3 = "THEFT FROM VEHICLE\n"
         key_4 = "BREAK AND ENTER\n"
         if key_1 in s and s[-2] == '1430':
            count_a_1 += 1
            crime_code_a1 = s[-2]
         elif key_1 in s and s[-2] == '1420':
            count_a_2 += 1
            crime_code_a2 = s[-2]
         elif key_1 in s and s[-2] == '1460':
            count_a_3 += 1
            crime_code_a3 = s[-2]
         elif key_2 in s:
            count_b += 1
            crime_code_b = s[-2]
         elif key_3 in s and s[-2] == '2142':
            count_c_1 += 1
            crime_code_c1 = s[-2]
         elif key_3 in s and s[-2] == '2132':
            count_c_2 += 1
            crime_code_c2 = s[-2]
         elif key_4 in s:
            count_d += 1
            crime_code_d = s[-2]
     my_dict[key_1] = ("CODE", crime_code_a1,"COUNT",  count_a_1),("CODE", crime_code_a2,"COUNT",  count_a_2),("CODE", crime_code_a3,"COUNT", count_a_3)
     my_dict[key_2] = "CODE", crime_code_b, "COUNT",  count_b
     my_dict[key_3] = ("CODE", crime_code_c1,"COUNT", count_c_1),("CODE", crime_code_c2,"COUNT", count_c_2)
     my_dict[key_4] = "CODE", crime_code_d,"COUNT",  count_d
     print(my_dict)
