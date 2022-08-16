import settings
from schemes import draw_schemes

f= open("piece.ly","w")
version = '\\version "2.20.0" \n'
f.write(f"{version}")
f= open("piece.ly","a")
header = """
\\header{{
    title = "{0}"
    subtitle = "notes grouping = '{1}'"
    composer = "Dmitriy Denisov"  
}}

\layout {{
    indent = #0
}}

""".format(settings.title, settings.notes_grouped_by)
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
\\time {settings.beats_in_bar}/4
\\repeat volta 4'''
score += ' {\n\n'

counter = 0 + settings.offset
for bar in settings.piece:
  score += '\t'
  for beat in bar:
    draw_scheme = ''
    for note in beat:
        draw_scheme += 'o'
    # print(draw_scheme)
    beat_score = ''
    # открываем нечетные группировки
    if settings.pulsation == 3 and draw_scheme != 'o__' and draw_scheme != '___': beat_score += '\\tuplet 3/2 {'
    if settings.pulsation == 5 and draw_scheme != 'o____' and draw_scheme != '_____': beat_score += '\\tuplet 5/4 {'
    if settings.pulsation == 6 and draw_scheme != 'o_____' and draw_scheme != '______': beat_score += '\\tuplet 6/4 {'
    if settings.pulsation == 7 and draw_scheme != 'o______' and draw_scheme != '_______': beat_score += '\\tuplet 7/4 {'
  # counter = 0 + settings.offset
    for note in draw_schemes[str(settings.pulsation)][draw_scheme]:
      beat_score += f'{note}'    
      if settings.notes_grouped_by[counter] == '1':   
        beat_score += '^> '    
      else:
        beat_score += '   '  
      # beat_score += ' '
      counter += 1
      if counter == len(settings.notes_grouped_by):
        counter = 0
      
    # закрываем нечетные группировки
    if settings.pulsation == 3 and draw_scheme != 'o__' and draw_scheme != '___': beat_score += '} '
    if settings.pulsation == 5 and draw_scheme != 'o____' and draw_scheme != '_____': beat_score += '}'
    if settings.pulsation == 6 and draw_scheme != 'o_____' and draw_scheme != '______': beat_score += '}'
    if settings.pulsation == 7 and draw_scheme != 'o______' and draw_scheme != '_______': beat_score += '}'
    # print(beat_score)
    score += beat_score
  score += '\n'

score += '''
  }
}'''
f.write(score)

#############################################################
                    # No filling
#############################################################

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
\\time {settings.beats_in_bar}/4
\\repeat volta 4'''
score += ' {\n\n'

for bar in settings.piece:
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
    if settings.pulsation == 3 and draw_scheme != 'o__' and draw_scheme != '___': beat_score += '\\tuplet 3/2 {'
    if settings.pulsation == 5 and draw_scheme != 'o____' and draw_scheme != '_____': beat_score += '\\tuplet 5/4 {'
    if settings.pulsation == 6 and draw_scheme != 'o_____' and draw_scheme != '______': beat_score += '\\tuplet 6/4 {'
    if settings.pulsation == 7 and draw_scheme != 'o______' and draw_scheme != '_______': beat_score += '\\tuplet 7/4 {'

    print(draw_schemes[str(settings.pulsation)][draw_scheme])
    for note in draw_schemes[str(settings.pulsation)][draw_scheme]:
      if note.startswith('r'):
        beat_score += f'{note} '
          
      # # погнали присоединять мелизмы
      else:
        beat_score += f'{note}'    
          
          
        beat_score += ' '

        

      # закрываем нечетные группировки
    if settings.pulsation == 3 and draw_scheme != 'o__' and draw_scheme != '___': beat_score += '} '
    if settings.pulsation == 5 and draw_scheme != 'o____' and draw_scheme != '_____': beat_score += '}'
    if settings.pulsation == 6 and draw_scheme != 'o_____' and draw_scheme != '______': beat_score += '}'
    if settings.pulsation == 7 and draw_scheme != 'o______' and draw_scheme != '_______': beat_score += '}'

      # print(beat_score)
    score += beat_score

  score += '\n'

score += '''
  }
}'''

f.write(score)


#############################################################
number = '13'
print('Easy_',number,'_', settings.pulsation_for_title[str(settings.pulsation)],'_by_',settings.pulsation,'_grouped_',settings.notes_grouped_by,'_in_',settings.beats_in_bar,'4',sep='')
