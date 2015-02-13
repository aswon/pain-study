import oculus
import viz

def initVR():
    """Initializes tracking and Oculus Rift"""
    hmd = oculus.Rift()
    viz.link(hmd.getSensor(), viz.MainView) #also we'll need to add tracking once PPT2 is up and running

def initModels():
    """Loads all of the models in the room"""

    # TODO: put pain scale on table (and build in real world) Andrea
    table = viz.addChild('table.osgb')
    table.setPosition(0,0.25,0)
    table.setEuler(0,0,0)

    # also chairs (two) Andrea
    chair = viz.addChild('chair.osgb')
    chair.setPosition(0,.375,0)
    chair.setEuler(0,0,0)

    # TODO: make version of lab room- Andrea
    cube = viz.addChild('PPT2.osgb')
    cube.setPosition(0,0.5,0)

    # TODO: make version of other lab room- Andrea
    cube = viz.addChild('PPTOhio.osgb')
    cube.setPosition(0,0.5,0)

def initKeyBindings():
    """Key bindings for program"""
    #vizact.onkeydown('n',avatarNod)
    vizact.onkeydown('a',avatarAlive)
    vizact.onkeydown('n',avatarNod)
    vizact.onkeydown('i',#insert "Hand in" in data)
    vizact.onkeydown('o',#insert "Hand out" in data)
    vizact.onkeydown('r',Recording)

def addConfederate(one that is selected in text box): #Pavitra and Alyssa
    """ <Place function description here> """
    # TODO: apply idling/seated animations to avatars
    # TODO: avatar look to participant and mimic head movements (4 second lag)
    # vizact.onkeydown('a',avatarAlive)
    # vizact.onkeydown('n',avatarNod)
    pass

def avatarComesAlive():
    """ <Place function description here> """
    print('Avatar Alive')
    # TODO: insert "Alive" in recorded data- to be coordinated with Mariano later
    # TODO: avatar idles body animation

def avatarNod():
    """ <Place function description here> """
    print('Avatar Nod')
    # TODO: insert "Nod" in recorded data- to be coordinated with Mariano later
    # TODO: avatar nods

def recording():
    """ <Place function description here> """
    print('Recording')
    # TODO: record head XYZ, head pitch yaw roll, and all print commands
    # TODO: also record audio to be synchronized

if __name__ == 'main':
    # Program execution starts here

    #input box to ask ID
    #input box to ask which avatar participant selected, addConfederate
    #input box to ask which world, addWorld
    #initialize slider

    initVR()
    viz.go()
    initModels()
    initKeypresses()


