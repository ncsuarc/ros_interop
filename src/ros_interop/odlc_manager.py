from urllib.request import Request
import rospy
from ros_interop.msg import *
from ros_interop.srv import ODLCResponse, ODLCsResponse, ImageResponse
from interop_clients.api import Odlc, OdlcColor, OdlcOrientation, OdlcShape, OdlcType


class ODLCManager:
    def __init__(self, interop_client) -> None:
        self.interop_client = interop_client
        pass

    def router_ODLC(self, req):
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

    def router_ODLCs(self, req):
        type = req.request_type.request_type
        if type == RequestType.GET:
            return self.get_targets(req)
        else:
            return None

    def router_ODLC_image(self, req):
        type = req.request_type.request_type
        if type == RequestType.GET:
            return self.get_target_image(req)
        elif type == RequestType.PUT:
            return self.put_target_image(req)
        else:
            return None

    def get_target_image(self, req):
        id = req.id
        image = self.interop_client.get_odlc_image(id)
        response = ImageResponse()
        response.id = id
        image_data_list = list(bytearray(image))
        response.image_data = image
        return response

    def put_target_image(self, req):

        id = req.id
        image_data = req.image_data
        self.interop_client.put_odlc_image(id,image_data)
        return ImageResponse(id = id)

    def delete_target_image(self, req):
        pass

    def get_targets(self, req):
        missionID = req.mission_id
        if missionID == 0:
            targets_info = self.interop_client.get_odlcs()
        else:
            targets_info = self.interop_client.get_odlcs(missionID)
        response = ODLCsResponse(targets_info=[])
        for target_info in targets_info:
            targetObj = singleODLC()
            targetObj.mission = target_info["mission"]
            targetObj.type = odlc_type(OdlcType[target_info["type"]].value)
            targetObj.latitude = target_info["latitude"]
            targetObj.longitude = target_info["longitude"]
            targetObj.orientation = odlc_orientation(
                OdlcOrientation[target_info["orientation"]].value
            )
            targetObj.shape = odlc_shape(OdlcShape[target_info["shape"]].value)
            if "alphanumeric" in target_info.keys():
                targetObj.alphanumeric = target_info["alphanumeric"]
            else:
                targetObj.alphanumeric = ""
            targetObj.shape_color = Color(OdlcColor[target_info["shapeColor"]])
            targetObj.alphanumeric_color = Color(
                OdlcColor[target_info["alphanumericColor"]]
            )
            targetObj.description = target_info["description"]
            targetObj.autonomous = target_info["autonomous"]
            response.targets_info.append(targetObj)
        return response
        pass

    def get_target(self, req):
        target_id = req.id
        target_info = self.interop_client.get_odlc(target_id)
        msg1 = ODLCResponse()
        msg1.id = target_info["id"]
        msg = singleODLC()
        msg.mission = target_info["mission"]
        msg.type = odlc_type(OdlcType[target_info["type"]].value)
        msg.latitude = target_info["latitude"]
        msg.longitude = target_info["longitude"]
        msg.orientation = odlc_orientation(
            OdlcOrientation[target_info["orientation"]].value
        )
        msg.shape = odlc_shape(OdlcShape[target_info["shape"]].value)
        if "alphanumeric" in target_info.keys():
            msg.alphanumeric = target_info["alphanumeric"]
        else:
            msg.alphanumeric = ""
        msg.shape_color = Color(OdlcColor[target_info["shapeColor"]])
        msg.alphanumeric_color = Color(OdlcColor[target_info["alphanumericColor"]])
        msg.description = target_info["description"]
        msg.autonomous = target_info["autonomous"]
        msg1.target_info = msg
        return msg1

    def post_target(self, req):
        target_info = req.post_target_info

        target_details = {}
        target_details["mission"] = target_info.mission
        target_details["type"] = target_info.type.odlc_type
        target_details["latitude"] = target_info.latitude
        target_details["longitude"] = target_info.longitude
        target_details["orientation"] = target_info.orientation.direction
        target_details["shape"] = target_info.shape.shape
        # target_details['alphanumeric'] = target_info.alphanumeric
        target_details["shape_color"] = target_info.shape_color.color_num
        target_details["alphanumeric_color"] = target_info.alphanumeric_color.color_num
        target_details["description"] = target_info.description
        target_details["autonomous"] = target_info.autonomous
        out = self.interop_client.post_odlc(target_details)
        response = ODLCResponse(out, req.post_target_info)
        return response

    def put_target(self, req):
        target_id = req.id
        target_info = req.post_target_info
        new_target_details = {}
        new_target_details["mission"] = target_info.mission
        new_target_details["type"] = target_info.type.odlc_type
        new_target_details["latitude"] = target_info.latitude
        new_target_details["longitude"] = target_info.longitude
        new_target_details["orientation"] = target_info.orientation.direction
        new_target_details["shape"] = target_info.shape.shape
        # new_target_details['alphanumeric'] = target_info.alphanumeric
        new_target_details["shape_color"] = target_info.shape_color.color_num
        new_target_details[
            "alphanumeric_color"
        ] = target_info.alphanumeric_color.color_num
        new_target_details["description"] = target_info.description
        new_target_details["autonomous"] = target_info.autonomous
        changed_target_details = {
            k: v for k, v in new_target_details.items() if not (v == 0 or v == "")
        }
        old_target = self.interop_client.get_odlc(target_id)
        new_target = {}
        for k, v in old_target.items():
            if k in changed_target_details.keys():
                new_target[k] = changed_target_details[k]
            else:
                new_target[k] = old_target[k]
        del new_target["id"]
        # self.interop_client.session.patch(self.interop_client.url + "/api/odlcs" )
        out = self.interop_client.put_odlc(target_id, new_target)
        response = ODLCResponse(id=req.id)
        return response

    def delete_target(self, req):
        target_id = req.id
        out = self.interop_client.delete_odlc(req.id)
        response = ODLCResponse(req.id, None)
        return response
