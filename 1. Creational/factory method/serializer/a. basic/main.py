import serializer_demo as sd

if __name__ == '__main__':
    song = sd.Song('1', 'Water of Love', 'Dire Straits')
    serializer = sd.SongSerializer()
    print(serializer.serialize(song, 'JSON'))
    print(serializer.serialize(song, 'XML'))
    print(serializer.serialize(song, 'YAML'))