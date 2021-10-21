import rospy
from ros_interop.srv import Team
from ros_interop.msg import TeamStatus,TeamID,Id,TeamsResponse


class Teams():

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
        id.Id = Id()
        id.Id.Id = 1
        id.username = 'hello'
        id.name = 'pack'
        id.university = "ncsu"
        msg.Team = id
        msg.in_air = False
        teams = TeamsResponse()
        teams.team_list = []
        teams.team_list.append(msg)
        teams.team_list.append(msg)
        return teams

class odlcs():
    def __init__(self) -> None:
        pass
    def router(self,req):
        type = req.type
        if type == "GET":
            return self.get_targets(req)
        else:
            return None
    def get_targets(self,req):
        print("Get Targets Called")

class odlc():
    def __init__(self) -> None:
        pass
    def router(self,req):
        type = req.type
        if type == "GET":
            return self.get_targets(req)
        else:
            return None
    def get_target(self,req):
        print("Get Target Called")


def judges_server():
    rospy.init_node('judges_server')
    teamObj = Teams()
    s = rospy.Service('teams', Team, teamObj.router)
    rospy.spin()

if __name__ == '__main__':
    judges_server()
    