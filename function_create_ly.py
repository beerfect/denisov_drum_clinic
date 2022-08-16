from schemes import draw_schemes

# НАСТРОИЛИ
beats_in_bar = 4 # размер 3/4/5 четвертей
pulsation = 4 # 3/4/5/6/7  значит триоли/16е/квинтоли/секстоли/септоли
notes_grouped_by = '100' # группы из 2/3/4/5/6/7 нот
bars_in_etude = 4 # количество тактов
file_number = 1
cliclic_part = 'easy'


                
pulsation_for_title = {
    '3': 'Triplets',
    '4': 'Sixteens',
    '5': 'Quintuplets',
    '6': 'Sixteen triplets',
    '7': 'Septolies'    
}




def create_dot_ly_file(beats_in_bar, pulsation,notes_grouped_by, bars_in_etude,file_number, cliclic_part):
    # ЗАПИЛИЛИ ОБЪЕКТ PIECE
    piece = [[[0 for note in range(pulsation)] for beat in range(beats_in_bar)] for bar in range(bars_in_etude)]
    counter = 0

    for counter_bar, bar in enumerate(piece):
        for counter_beat, beat in enumerate(bar):
            for counter_note, note in enumerate(beat):
                if notes_grouped_by[counter] == '1':
                    piece[counter_bar][counter_beat][counter_note] = 1            
                counter += 1
                if counter == len(notes_grouped_by):
                    counter = 0

    # print(piece)

    title = f'{pulsation_for_title[str(pulsation)]} by {len(notes_grouped_by)} in {beats_in_bar}/4'
    # print(title)
    
    filename = '_'.join([str(file_number).rjust(2, '0'), cliclic_part,pulsation_for_title[str(pulsation)],'by',str(len(notes_grouped_by)),notes_grouped_by,'in',str(beats_in_bar)+'4'])
    # print(filename)
    f= open(f"Sheet music/{cliclic_part}/{filename}.ly","w")
    version = '\\version "2.20.0" \n'
    f.write(f"{version}")
    f= open(f"Sheet music/{cliclic_part}/{filename}.ly","a")
    header = """
    \\header{{
        title = "{0}"
        subtitle = "notes grouping = '{1}'"
        subsubtitle = "{2} #{3}"
        composer = "Dmitriy Denisov"  
    }}

    \layout {{
        indent = #0
    }}

    """.format(title, notes_grouped_by,cliclic_part, file_number)
    f.write(header)

############################################
#               Note filling
############################################
    score = r'''\markup {
        Note filling
    }

    \relative c'{
    \set fontSize = 1
    \clef percussion 
    \stemUp
    '''

    score += f'''
    \\time {beats_in_bar}/4
    \\repeat volta 4'''
    score += ' {\n\n'

    counter = 0 
    for bar in piece:
        score += '\t'
        for beat in bar:
            draw_scheme = ''
            for note in beat:
                draw_scheme += 'o'
            # print(draw_scheme)
            beat_score = ''
            # открываем нечетные группировки
            if pulsation == 3 and draw_scheme != 'o__' and draw_scheme != '___': beat_score += '\\tuplet 3/2 {'
            if pulsation == 5 and draw_scheme != 'o____' and draw_scheme != '_____': beat_score += '\\tuplet 5/4 {'
            if pulsation == 6 and draw_scheme != 'o_____' and draw_scheme != '______': beat_score += '\\tuplet 6/4 {'
            if pulsation == 7 and draw_scheme != 'o______' and draw_scheme != '_______': beat_score += '\\tuplet 7/4 {'
        # counter = 0 
            for note in draw_schemes[str(pulsation)][draw_scheme]:
                beat_score += f'{note}'    
                if notes_grouped_by[counter] == '1':   
                    beat_score += '^> '    
                else:
                    beat_score += '   '  
                # beat_score += ' '
                counter += 1
                if counter == len(notes_grouped_by):
                    counter = 0
            
            # закрываем нечетные группировки
            if pulsation == 3 and draw_scheme != 'o__' and draw_scheme != '___': beat_score += '} '
            if pulsation == 5 and draw_scheme != 'o____' and draw_scheme != '_____': beat_score += '}'
            if pulsation == 6 and draw_scheme != 'o_____' and draw_scheme != '______': beat_score += '}'
            if pulsation == 7 and draw_scheme != 'o______' and draw_scheme != '_______': beat_score += '}'
            # print(beat_score)
            score += beat_score
        score += '\n'

    score += '''
        }
    }'''
    f.write(score)
    # print('DONE')

##################################################################
    score = r'''

    \markup {
        No filling
    }

    \relative c'{
    \set fontSize = 1
    \clef percussion 
    \stemUp
    '''

    score += f'''
    \\time {beats_in_bar}/4
    \\repeat volta 4'''
    score += ' {\n\n'

    for bar in piece:
        score += '\t'
        for beat in bar:
            draw_scheme = ''
            for note in beat:
                if note == 1:
                    draw_scheme += 'o'
                else:
                    draw_scheme += '_'
        
            beat_score = ''
        
            # открываем нечетные группировки
            if pulsation == 3 and draw_scheme != 'o__' and draw_scheme != '___': beat_score += '\\tuplet 3/2 {'
            if pulsation == 5 and draw_scheme != 'o____' and draw_scheme != '_____': beat_score += '\\tuplet 5/4 {'
            if pulsation == 6 and draw_scheme != 'o_____' and draw_scheme != '______': beat_score += '\\tuplet 6/4 {'
            if pulsation == 7 and draw_scheme != 'o______' and draw_scheme != '_______': beat_score += '\\tuplet 7/4 {'

            # print(draw_schemes[str(pulsation)][draw_scheme])
            for note in draw_schemes[str(pulsation)][draw_scheme]:
                if note.startswith('r'):
                    beat_score += f'{note} '
                
                # # погнали присоединять мелизмы
                else:
                    beat_score += f'{note}'    
                
                
                    beat_score += ' '

                

            # закрываем нечетные группировки
            if pulsation == 3 and draw_scheme != 'o__' and draw_scheme != '___': beat_score += '} '
            if pulsation == 5 and draw_scheme != 'o____' and draw_scheme != '_____': beat_score += '}'
            if pulsation == 6 and draw_scheme != 'o_____' and draw_scheme != '______': beat_score += '}'
            if pulsation == 7 and draw_scheme != 'o______' and draw_scheme != '_______': beat_score += '}'

            # print(beat_score)
            score += beat_score

        score += '\n'

    score += '''
        }
    }'''

    f.write(score)
    print('SUCCEFULLY CREATED ', filename,'.ly',sep='')
#############################################################













# create_dot_ly_file(beats_in_bar, pulsation,notes_grouped_by, bars_in_etude,file_number, cliclic_part)