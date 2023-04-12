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
    """"
    Represents a musical note in terms of pitch and perspective.

    Attributes:
    -----------
    pitch : str
        The pitch of the note, represented as a string (e.g. "C", "D#", "Gb").
    perspective : str
        The pitch perspective of the note, represented as "#" for sharp or "b" for flat.
    """
    
    position = 0
    perspective = ""
    
    
    def __init__(self, position, perspective = None):
        if isinstance(position, str):
            self.position = POSITIONS[position]
            if perspective != None:
                self.perspective = perspective
            elif position[-1] in ("#", "b"):
                self.perspective = position[-1]
            else:
                self.perspective = None
        elif isinstance(position, int) and 0 <= position <= 11:
            self.position = position
            self.perspective = perspective
        
    def __invert__(self):
        if self.perspective == "b":
            self.perspective = "#"
        elif self.perspective == "#":
            self.perspective = "b"
            
        else:
            self.perspective = None
            
        return Note(self.position, self.perspective)
        
    def __add__(self, num):
        self.position = (self.position + num) % 12
        return Note(self.position, self.perspective)

    def __sub__(self, num):
        self.position = abs((self.position - num) % 12)
        return Note(self.position, self.perspective)

    def __rshift__(self, other):
        if isinstance(other, Note): 
            rdistance = (self.position - other.position) % 12
        return rdistance

    def __lshift__(self, other):
        if isinstance(other, Note): 
            ldistance = (other.position - self.position) % 12
        return ldistance

    def __repr__(self): #idk how to do ths one and if this naming is correct
        return f"Note({self.position}, {self.perspective!r})"
    
    def __str__(self):
        pitch_names = PITCHES[self.position]
        if self.perspective is None:
            if len(pitch_names) == 1:
                return pitch_names[0]
            else:
                return f"{pitch_names[0]}/{pitch_names[1]}"
        elif self.perspective == "#":
            return pitch_names[0] if "#" in pitch_names[0] else pitch_names[1]
        elif self.perspective == "b":
            return pitch_names[0] if "b" in pitch_names[0] else pitch_names[1]
    
    