from pydub import AudioSegment


sound = AudioSegment.from_mp3("The Key/The Key.mp3")


#miliseconds in the sound track
episode1_time =  (4 * 60 + 30) * 1000
episode2_time =  (8 * 60 + 8) * 1000

episode1_sound = sound[:episode1_time]
episode2_sound = sound[episode1_time:episode2_time]
episode3_sound = sound[episode2_time:len(sound)]

print (len(sound))
# remain_sound = sound[episode1_time:len(sound)]

episode1_sound.export("The Key/theKey_part1.mp3", format="mp3")
episode2_sound.export("The Key/theKey_part2.mp3", format="mp3")
episode3_sound.export("The Key/theKey_part3.mp3", format="mp3")



