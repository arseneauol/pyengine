class GameObject:
  def __init__(self,transform,rendereur,componentList):
    self.transform = transform
    self.renderer = rendereur
    self.components = componentList
  def update(self):
    for component in self.components:
      component.update()
  def Render(self):
    self.renderer.draw()
class Vector2:
  def __init__(self,x,y):
    self.x = x
    self.y = y
class Rotation:
  def __init__(self,angle):
    self.angle = angle
class Transform:
  def __init__(self,position,rotation,scale):
    self.position = position
    self.rotation = rotation
    self.scale = scale
class Renderer:
  def __init__(self,sprite):
    self.sprite =sprite
  def draw(self):
    sprite = 1 
class Scene:
  def __init__(self, lisOfgameObeject):
    self.gameObjects = lisOfgameObeject
  def update(self):
    for gameObject in self.gameObjects:
      gameObject.update()
class Sprite:
  def __init__(self,image):
    self.image =image;
