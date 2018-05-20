def get_date_today():
    return (2013, 10, 30)

class Artist(object):
    def __init__(self, name, dob):
         
        self.name=name
        self.dob=dob
    
    def age(self):
        dob=self.dob
        today=get_date_today()
        delta_year=today[0]-dob[0]
        if today[1]>dob[1] or (today[1]==dob[1] and today[2]>dob[2]):
            return delta_year
        else:
            return delta_year-1

    def get_name(self):
         
        return self.name

        
    def get_dob(self):
         
        return self.dob


class Duration(object):
    def __init__(self, minutes, seconds):
         
        self.minutes=minutes
        self.seconds=seconds
        self.total_seconds=minutes*60+seconds
    
    def __str__(self):
        if len(str(self.get_minutes()))==1:
            minstr='0'+str(self.get_minutes())
        else:
            minstr=self.get_minutes()
        if len(str(self.get_seconds()))==1:
            secstr='0'+str(self.get_seconds())
        else:
            secstr=self.get_seconds()

        return str(minstr)+":"+str(secstr)
    
    def __add__(self,object):
        return Duration(self.get_minutes()+object.get_minutes(),self.get_seconds()+object.get_seconds())
    
    def get_minutes(self):
        return self.total_seconds//60
    
    def get_seconds(self):
        return self.total_seconds%60
        

class Song(object):
    def __init__(self, artist, title, duration):
         
        self.artist=artist
        self.title=title
        self.duration=duration
        
    
    def get_artist(self):
        
        return self.artist
        
    
    def get_title(self):
         
        return self.title
        
        
    def get_duration(self):
         
        return self.duration
        

class Album(object):
    def __init__(self, artist, title):
         
        self.artist=artist
        self.title=title
        self.collection=[]

    def add_song(self, song):
         
        self.collection.append(song)
        
    def total_runtime(self):
        if self.collection==[]:
            return Duration(0,0)
        else:
            result=Duration(0,0)
            for song in self.collection:
                result+=song.get_duration()
            return result

