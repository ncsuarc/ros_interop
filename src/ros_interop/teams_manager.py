import rospy
from ros_interop.srv import Team,TeamResponse
from ros_interop.msg import * 


class TeamsManager():

    def __init__(self) -> None:
        pass

    def router(self,req):
        type = req.type
        if type == "GET":
            return self.get_teams()
        else:
            return None
    def get_teams(self):
        print("Get Teams Called")
        teams = []
        msg = TeamStatus()
        id = TeamID()
        id.id = 1
        id.username = 'hello'
        id.name = 'pack'
        id.university = "ncsu"
        msg.Team = id
        msg.in_air = False
        teams = TeamResponse()
        teams.team_list = []
        teams.team_list.append(msg)
        teams.team_list.append(msg)
        return teams