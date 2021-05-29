import songs
import serializers

if __name__ == '__main__':
    song = songs.Song('1', 'Water of Love', 'Dire Straits')
    serializer = serializers.ObjectSerializer()
    print(serializer.serialize(song, 'JSON'))
    print(serializer.serialize(song, 'XML'))
    print(serializer.serialize(song, 'YAML'))