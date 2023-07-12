import mido
from pynput.keyboard import Controller

keyboard = Controller()
notes = []
accords = []
current_notes = []


FIRST_E_PIANO_NOTE = 12
PIANO_NOTES = ['C', '#C', 'D', '#D', 'E', 'F', '#F', 'G', '#G', 'A', '#A', 'B']

#safe note on notes to current notes, when len is above 1 accord is played (timestamp?)
# iterate over accords and compare with current_notes
def main():
    global current_notes
    read_notes()
    read_accords()
    with mido.open_input() as inport:
        for msg in inport:
            if(msg.type == 'note_on'):
                keyboard.press(notes[msg.note - FIRST_E_PIANO_NOTE])
                keyboard.release(notes[msg.note - FIRST_E_PIANO_NOTE])
                print(get_note_value(msg.note))

def read_notes():
    global notes
    with open('notes.txt', encoding='utf8') as file:
        for line in file:
            line = line.strip('\n')
            notes.append(line)

def read_accords():
    global accords
    with open('accords.txt', encoding='utf8') as file:
        for line in file:
            line = line.strip('\n')
            tokens = line.split()
            accords.append({
                'word': tokens[0],
                'notes': tokens[1:]
            })

def get_note_value(note):
    note -= FIRST_E_PIANO_NOTE
    octave = int(note / 12)
    note -= octave * len(PIANO_NOTES)
    return PIANO_NOTES[note]

main()