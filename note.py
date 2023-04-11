POSITIONS = {
    "A" :  0,
    "A#":  1,
    "Bb":  1,
    "B" :  2,
    "C" :  3,
    "C#":  4,
    "Db":  4,
    "D" :  5,
    "D#":  6,
    "Eb":  6,
    "E" :  7,
    "F" :  8,
    "F#":  9,
    "Gb":  9,
    "G" : 10,
    "G#": 11,
    "Ab": 11
}

PITCHES = {
    0:  ["A"],
    1:  ["A#", "Bb"],
    2:  ["B"],
    3:  ["C"],
    4:  ["C#", "Db"],
    5:  ["D"],
    6:  ["D#", "Eb"],
    7:  ["E"],
    8:  ["F"],
    9:  ["F#", "Gb"],
    10: ["G"],
    11: ["G#", "Ab"]
}


class Note:
    
    position = 0
    perspective = ""
    
    def __init__(self, position, perspective = None):
        if isinstance(position, str):
            if self.position.len > 1:
                self.perspective = self.position[1]
            self.position = POSITIONS[position] 
        else:
            self.position = position
        
        self.perspective = perspective
        
    def __invert__(self):
        return Note(
            if self.perspective == 'b':
                return self.perspective == '#'
            elif self.perspective == '#':
                return self.perspective == 'b'
            else:
                return None
        )
        
    def __add__(self, num):
        placeholder = (self.position + num) / 12
        addNote = (placeholder, self.perspective)
        return addNote

    def __sub__(self, num):
        placeholder = abs(self.position - num) / 12
        subNote = (placeholder, self.perspective)
        return subNote

    def __rightShift__(self, other): 
        rdistance = abs(self.position - other.position) / 12
        return rdistance

    def __leftShift__(self, other): 
        ldistance = abs(other.position - self.position) / 12
        return ldistance

    def __repr__(self): #idk how to do ths one and if this naming is correct
        return f"Note({self.position}, {self.perspective!r})"
            
    
    