import requests

class SpotifyDataCollector:
    def __init__(self):
        self.auth = self.__auth()
        
    def __auth(self):
        CLIENT_ID="971b395363e040948f69f0103aefc7fc"
        CLIENT_SECRET="c1b761cac6054b76945cd89fa2e5824a"

        headers = {
        "Content-Type": "application/x-www-form-urlencoded"
        }
    
        data = {
            "grant_type": "client_credentials",
            "client_id" : CLIENT_ID,
            "client_secret" : CLIENT_SECRET
        }
    
        request = requests.post("https://accounts.spotify.com/api/token",
                                headers=headers,
                                data=data)
        json = request.json()
    
        return "Bearer " + json["access_token"]
    
    def get_playlist(self, playlistId):
        header = {"Authorization": self.auth}
        playlist = requests.get(f"https://api.spotify.com/v1/playlists/{playlistId}",headers=header)    
        jsonP = playlist.json()
        return(jsonP)
    
    def get_tracks_name(self, playlistJson):
        tracks = playlistJson["tracks"]["items"]
        tracksName = list()
        counter = 0
        for i in tracks:
            try:
                track = i["track"]["name"]
                artist = i["track"]["artists"][0]["name"]
                tracksName.append((track, artist))
                counter+=1
            except:
                continue
        return tracksName
    
    def reload_auth(self):
        self.auth = self.__auth()