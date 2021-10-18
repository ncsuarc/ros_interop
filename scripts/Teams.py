import rospy
from ros_interop.srv import Team
from ros_interop.msg import TeamStatus,TeamID,Id


class Teams():

    def __init__(self) -> None:
        pass

    def getTeams(req):
        
        return







def get_teams(req):
    print("Get Teams Called")
    teams = []
    msg = TeamStatus()
    id = TeamID()
    id.Id = Id()
    id.Id.Id = i
    id.username = 'hello'
    id.name = 'pack'
    id.university = "ncsu"
    msg.Team = id
    msg.in_air = False
    return msg

def teams_server():
    rospy.init_node('teams_server')
    s = rospy.Service('getTeams', Team, get_teams)
    rospy.spin()

if __name__ == '__main__':
    teams_server()
    