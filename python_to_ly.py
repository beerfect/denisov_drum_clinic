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
  subsubtitle = "offset = {2}, fill = {3}"
  composer = "Dmitriy Denisov"  
}}
""".format(settings.title, settings.notes_grouped_by ,settings.offset, settings.fill)


f.write(header)

######################## SCORE start ##########################
# score = r'''
# \score {
#   \new RhythmicStaff {
#     \set fontSize = -5'''

score = r'''
 \relative c'{
    \set fontSize = 1
    \clef percussion 
    \stemUp
    '''

###############################################################

score += f'''
\\time {settings.beats_in_bar}/4
\\repeat volta 4'''
score += ' {\n\n'

if settings.fill == 'rests':
  for bar in settings.piece:
    score += '\t'
    for beat in bar:
      draw_scheme = ''
      for note in beat:
        if note == 1:
          draw_scheme += 'o'
        else:
          draw_scheme += '_'
      # print(draw_scheme)

      beat_score = ''
      
      # открываем нечетные группировки
      if settings.pulsation == 3 and draw_scheme != 'o__' and draw_scheme != '___': beat_score += '\\tuplet 3/2 {'
      if settings.pulsation == 5 and draw_scheme != 'o____' and draw_scheme != '_____': beat_score += '\\tuplet 5/4 {'
      if settings.pulsation == 6 and draw_scheme != 'o_____' and draw_scheme != '______': beat_score += '\\tuplet 6/4 {'
      if settings.pulsation == 7 and draw_scheme != 'o______' and draw_scheme != '_______': beat_score += '\\tuplet 7/4 {'

      print(draw_schemes[str(settings.pulsation)][draw_scheme])
      for note in draw_schemes[str(settings.pulsation)][draw_scheme]:
        # print(note)
        # # паузы просто переписываем
        if note.startswith('r'):
          beat_score += f'{note} '
          
        # # погнали присоединять мелизмы
        else:
        #   # нота
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


if settings.fill == 'notes':

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

######################## SCORE end ###########################
# score += r'''\bar "|."
# }'''
##############################################################

f.write(score)
print('COMPLETED: python_to_ly.py')