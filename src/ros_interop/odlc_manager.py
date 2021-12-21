import rospy
from ros_interop.msg import *
from ros_interop.srv import ODLCResponse
from interop_clients.api import Odlc, OdlcColor, OdlcOrientation, OdlcShape, OdlcType

class ODLCManager():
    def __init__(self,interop_client) -> None:
        self.interop_client = interop_client
        pass
    def router_ODLC(self,req):
        type = req.request_type.request_type
        if type == RequestType.GET: 
            return self.get_target(req)
        elif type == RequestType.POST:
            return self.post_target(req)
        elif type == RequestType.PUT:
            return self.put_target(req)
        elif type == RequestType.DELETE:
            return self.delete_target(req)
        else:
            return None
    def router_ODLCs(self,req):
        pass
    def get_target(self,req):
        target_id = req.id
        print("Get Target Called")
        target_info = self.interop_client.get_odlc(target_id)
        msg1 = ODLCResponse()
        msg1.id = target_info['id']
        msg = singleODLC()
        msg.mission = target_info['mission']
        msg.type = odlc_type(OdlcType[target_info['type']].value)
        msg.latitude = target_info['latitude']
        msg.longitude = target_info['longitude']
        msg.orientation = odlc_orientation(OdlcOrientation[target_info["orientation"]].value)
        msg.shape = odlc_shape(OdlcShape[target_info['shape']].value)
        if 'alphanumeric' in target_info.keys():
            msg.alphanumeric = target_info['alphanumeric']
        else:
            msg.alphanumeric = ''
        msg.shape_color = Color(OdlcColor[target_info['shapeColor']])
        msg.alphanumeric_color = Color(OdlcColor[target_info['alphanumericColor']])
        msg.description = target_info['description']
        msg.autonomous  = False
        msg1.target_info = msg
        return msg1
    
    def post_target(self,req):
        target_info = req.post_target_info

        target_details = {}
        target_details['mission'] = target_info.mission
        target_details['type'] = target_info.type.odlc_type
        target_details['latitude'] = target_info.latitude
        target_details['longitude'] = target_info.longitude
        target_details['orientation'] = target_info.orientation.direction
        target_details['shape'] = target_info.shape.shape
        #target_details['alphanumeric'] = target_info.alphanumeric
        target_details['shape_color'] = target_info.shape_color.color_num
        target_details['alphanumeric_color'] = target_info.alphanumeric_color.color_num
        target_details['description'] = target_info.description
        target_details['autonomous'] = target_info.autonomous
        out = self.interop_client.post_odlc(target_details)
        response = ODLCResponse(out,req.post_target_info)
        return response
    def put_target(self,req):
        target_details = {}
        target_info = req.post_target_info
        target_details = {}
        target_details['mission'] = target_info.mission
        target_details['type'] = target_info.type.odlc_type
        target_details['latitude'] = target_info.latitude
        target_details['longitude'] = target_info.longitude
        target_details['orientation'] = target_info.orientation.direction
        target_details['shape'] = target_info.shape.shape
        #target_details['alphanumeric'] = target_info.alphanumeric
        target_details['shape_color'] = target_info.shape_color.color_num
        target_details['alphanumeric_color'] = target_info.alphanumeric_color.color_num
        target_details['description'] = target_info.description
        target_details['autonomous'] = target_info.autonomous
        out_target_details = {}
        #target_details = {k:v for k,v in target_details.items() if not (v==0 or v=='')}
        out = self.interop_client.put_odlc(req.id,target_details)
        print(out_target_details)
        response = ODLCResponse(req.id,target_info)
        return response
    def delete_target(self,req):
        target_id = req.id
        out = self.interop_client.delete_odlc(req.id)
        response = ODLCResponse(req.id,None)
        return response
