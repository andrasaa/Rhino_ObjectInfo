import Rhino
import scriptcontext
import rhinoscriptsyntax as rs

def GetObjectInfo():
    obj = rs.GetObject ( message=None, filter=0, preselect=False, select=False, custom_filter=None, subobjects=True)
    # Group name:
    group  = rs.ObjectGroups(obj) # Related group name of the selected object 
    # Object type:
    obj_coerce  = rs.coercerhinoobject(obj)
    obj_type    = obj_coerce.ObjectType
    # Object Layer:
    layer = rs.ObjectLayer(obj, layer=None)
    # Sub object | edge index:
    edgeIndex = None
    if obj:
        edge = obj.Edge()
        if edge:
            edgeIndex =  edge.EdgeIndex
    # Object Name:
    obj_name = rs.ObjectName ( obj, None )
    if obj_name=="":
        obj_name = "No name"
    # Object Id:
    obj_id =  rs.coerceguid(obj)
    # Message:
    if edgeIndex != None:
        message = "Edge index: {}".format(edgeIndex)
    else:
        message = "This is a: {} object \nName: {} \nId: {} \nGroup(s): {} \nLayers: {} ".format(obj_type,obj_name,obj_id,group1,layer)
    # 
    prompt = rs.MessageBox (message, buttons=0, title=None)
    # 
    return obj_type,obj_name,obj_id,group1,layer,edgeIndex
if __name__ == "__main__":
    GetObjectInfo()
