from function_create_ly import(create_dot_ly_file)



difficult = 'Elementary' 

# elementary_exercisec = [
#     (3, 3, '10', 4, 1, difficult),
#     (3, 3, '1000', 4, 2, difficult),
#     (3, 3, '1100', 4, 3, difficult),
#     (3, 3, '1110', 4, 4, difficult),
#     (4, 4, '100', 3, 5, difficult),
#     (4, 4, '110', 3, 6, difficult),
#     (4, 4, '100000', 3, 7, difficult),
#     (4, 4, '110000', 3, 8, difficult),
#     (4, 4, '101000', 3, 9, difficult),
#     (4, 4, '111000', 3, 10, difficult),
#     (4, 4, '111100', 3, 11, difficult),
#     (4, 4, '111010', 3, 12, difficult),
#     (3, 5, '10',2 , 13, difficult),
#     (3, 7, '10',2 , 14, difficult)
# ]

# for ex in elementary_exercisec:
#     create_dot_ly_file(*ex)


difficult = 'Intermediate'
# beats_in_bar = 4

# intermediate_exircises = [
    # (beats_in_bar, 3, '10000',5 ,1, difficult),
    # (beats_in_bar, 3, '10100',5 ,2, difficult),
    # (beats_in_bar, 3, '11100',5 ,3, difficult),
    # (beats_in_bar, 3, '11010',5 ,4, difficult),
    # (beats_in_bar, 3, '11110',5 ,5, difficult),
    # (beats_in_bar, 3, '1000000',7 ,6, difficult),
    # (beats_in_bar, 3, '1010100',7 ,7, difficult),
    # (beats_in_bar, 3, '1101100',7 ,8, difficult),
    # (beats_in_bar, 3, '1101010',7 ,9, difficult),
    # (beats_in_bar, 3, '1111010',7 ,10, difficult),
    # (beats_in_bar, 3, '1110110',7 ,11, difficult),
    # (beats_in_bar, 4, '10000',5 ,12, difficult),
    # (beats_in_bar, 4, '10100',5 ,13, difficult),
    # (beats_in_bar, 4, '11100',5 ,14, difficult),
    # (beats_in_bar, 4, '11010',5 ,15, difficult),
    # (beats_in_bar, 4, '11110',5 ,16, difficult),
    # (beats_in_bar, 4, '100101',3 ,17, difficult),
    # (beats_in_bar, 4, '1000000',7 ,18, difficult),
    # (beats_in_bar, 4, '1010100',7 ,19, difficult),
    # (beats_in_bar, 4, '1101100',7 ,20, difficult),
    # (beats_in_bar, 4, '1101010',7 ,21, difficult),
    # (beats_in_bar, 4, '1111010',7 ,22, difficult),
    # (beats_in_bar, 4, '1110110',7 ,23, difficult),
    # (beats_in_bar, 5, '100',3 , 24, difficult),
    # (beats_in_bar, 5, '1000',2 , 25, difficult),
    # (beats_in_bar, 6, '10000',5 , 26, difficult),
    # (beats_in_bar, 6, '10100',5 , 27, difficult),
    # (beats_in_bar, 6, '1000000',7 , 28, difficult),
    # (beats_in_bar, 6, '1010100',7 , 29, difficult),
    # (beats_in_bar, 7, '100',3 , 30, difficult),    
    # (beats_in_bar, 7, '1000',3 , 31, difficult)
# ]

# for ex in intermediate_exircises:
#     create_dot_ly_file(*ex)


#(beats_in_bar, pulsation, notes_grouped_by, bars_in_etude, file_number, difficult)

difficult = 'Master'

master_exircises = [
    # (3, 5,'100101', 4, 1, difficult),
    # (4, 5,'111000', 6, 2, difficult),
    (5, 5,'110100', 6, 3, difficult), 
    # (3, 5,'1100100', 7, 4, difficult),
    # (4, 5,'1101100', 7, 5, difficult),
    # (5, 5,'1110100', 7, 6, difficult),
    # (3, 7,'11100', 5, 7, difficult),
    # (4, 7,'11111010', 2, 8, difficult),
    (5, 7,'101100', 6, 9, difficult)
]

for ex in master_exircises:
    create_dot_ly_file(*ex)