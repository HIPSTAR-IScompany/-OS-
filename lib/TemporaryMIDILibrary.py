# Temporary MIDI Library
class SimpleMIDI:
    def __init__(self):
        self.header = b'MThd' + bytes([0, 0, 0, 6]) + bytes([0, 1, 0, 1, 0, 96])
        self.tracks = []

    def add_note(self, note, duration, velocity=64):
        track_data = bytes([0x90, note, velocity]) + bytes([0x80, note, velocity])
        self.tracks.append(track_data)

    def save(self, filename):
        with open(filename, 'wb') as f:
            f.write(self.header)
            for track in self.tracks:
                f.write(b'MTrk' + len(track).to_bytes(4, 'big') + track)
