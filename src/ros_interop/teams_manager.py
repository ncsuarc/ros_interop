import rospy
from ros_interop.srv import TeamResponse
from ros_interop.msg import * 
from geographic_msgs.msg import GeoPoint

class TeamsManager():

    def __init__(self,interop_client) -> None:
        self.interop_client = interop_client

    def router(self,req):
        type = req.request_type.request_type
        if type == RequestType.GET:
            return self.get_teams()
        else:
            return None
    def get_teams(self):
        teams_data = self.interop_client.get_teams()
        teams = TeamResponse()
        teams.team_list = []
        for one_team in teams_data:
            team_data = one_team['team']
            msg = TeamStatus()
            team_info = TeamID()
            team_info.id = team_data["id"]
            team_info.username = team_data['username']
            team_info.name = team_data['name']
            team_info.university = team_data['university']
            msg.Team = team_info
            msg.in_air = one_team['inAir']
            if bool(msg.in_air):
                altitude = 10
                geopointer = GeoPoint(10,10,10)
                msg.telemetry = telemetry(geopointer, altitude) 
            else:
                msg.telemetry = telemetry(GeoPoint(0,0,0),0)
            teams.team_list.append(msg)
        return teams