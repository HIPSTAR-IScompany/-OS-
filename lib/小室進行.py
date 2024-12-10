from midiutil import MIDIFile

# MIDIファイルを作成
midi = MIDIFile(1)
track = 0
time = 0
channel = 0
tempo = 120
volume = 100
midi.addTempo(track, time, tempo)

# 小室進行 (Am-F-G-C)
progression = [
    [57, 60, 64],  # Am
    [53, 57, 60],  # F
    [55, 59, 62],  # G
    [48, 52, 55],  # C
]

# 進行を4回繰り返し
for i in range(4):
    for chord in progression:
        for note in chord:
            midi.addNote(track, channel, note, time, 1, volume)
        time += 1

# ファイル保存
with open("komuro_progression.mid", "wb") as output_file:
    midi.writeFile(output_file)
