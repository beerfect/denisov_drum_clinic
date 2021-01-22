bars_in_etude = 8 # количество тактов
beats_in_bar = 4 # размер 3/4/5 четвертей
pulsation = 3 # 3/4/5/6/7  значит триоли/16е/квинтоли/секстоли/септоли
notes_grouped_by = '10100' # группы из 2/3/4/5/6/7 нот
offset = 0 # сместить на offset нот вперед















































################################################################
#                   ЭТО УЖЕ НЕ НАСТРОЙКИ
################################################################

piece = [[[0 for note in range(pulsation)] for beat in range(beats_in_bar)] for bar in range(bars_in_etude)]
counter = 0 + offset

for counter_bar, bar in enumerate(piece):
    for counter_beat, beat in enumerate(bar):
        for counter_note, note in enumerate(beat):
            if notes_grouped_by[counter] == '1':
                piece[counter_bar][counter_beat][counter_note] = 1            
            counter += 1
            if counter == len(notes_grouped_by):
                counter = 0
                
pulsation_for_title = {
    '3': 'Triplets',
    '4': 'Sixteens',
    '5': 'Quintiplets',
    '6': 'Sixteen triplets',
    '7': 'Septoles'    
}

title = f'{pulsation_for_title[str(pulsation)]} by {len(notes_grouped_by)} in {beats_in_bar}/4'