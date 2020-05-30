class GameObject:
  def __init__(self,Transform,Rendereur,componentList):
    self.transform = Transform
    self.renderer = Rendereur
    self.components = componentList

class Vector2:
  def __init__(self,x,y):
    self.x = x
    self.y = y
class Rotation:
  def __init__(self,angle):
    self.angle = angle

class Transform:
  def __init(self,position,rotation,scale):
    self.position = Vector2(position)
    self.rotation = rotation
    self.scale = scale

