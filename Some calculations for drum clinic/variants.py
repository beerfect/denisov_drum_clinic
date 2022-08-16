razmeras = ['3/4','4/4','5/4']
pulsations = ['triplets','sixteens','quintiplest','sixteen_triplets', 'septolies']

group_2 = ['10']
group_3 = ['100', '110']
group_4 = ['1000', '1100', '1010', '1110']
group_5 = ['10000', '11000', '10100', '11100', '11010', '11110']
group_6 = ['100000', '110000', '101000', '111000', '100100', '110100', '101100', '111100', '101010', '111010', '110110', '111110']
group_7 = ['1000000', '1100000', '1010000', '1110000', '1001000', '1101000', '1011000', '1111000', '1100100', '1010100', '1110100', '1101100', '1011100', '1111100', '1101010', '1111010', '1110110', '1111110']

groups = [group_2, group_3, group_4, group_5, group_6, group_7]

i = 0
for razmer in razmeras:
    print()
    for pulsation in pulsations:
        print()
        for group in groups:
            print()
            for subgroup in group:
                print(razmer, pulsation, 'by',len(subgroup), subgroup)
                i += 1
print(i)