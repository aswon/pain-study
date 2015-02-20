import oculus
import viz
import vizinput
import random
import datetime

# key presses
# r - reset
# d - data
# i - hand in
# o - hand out

MODEL_ARRAY = ['Models/dojo.osgb', 'Models/PPT2.osgb'] #TODO Andrea change scale PPT2 and door texture

dateTime = datetime.datetime.now()
participantID = str(dateTime)
participantID = participantID.replace(":", "-").replace(' ','_').split(".")[0]
print participantID

def initVR():
    """Initializes tracking and Oculus Rift"""
    hmd = oculus.Rift()
    hmd_sensor = hmd.getSensor()
    hmd_sensor.reset()
    PPT_HOSTNAME = '171.64.32.54'
    vrpn = viz.add('vrpn7.dle')
    headTracker = vrpn.addTracker('PPT0@' + PPT_HOSTNAME, 0)
    headPPT = viz.mergeLinkable(headTracker,hmd_sensor)
    hmd_link = viz.link(headPPT, viz.MainView)
    vizact.onkeydown('r', hmd.getSensor().reset)

def initModels():
    """Loads all of the models in the room"""
    randomSeed = random.randint(0,len(MODEL_ARRAY)-1)
    worldModel = MODEL_ARRAY[randomSeed]
    cube = viz.addChild(worldModel)
    cube.setPosition(0,0,0)
    
# ---- handInData ----
def handInData():
    print 'hand in'
    #write "hand in" and timestamp in second recording file

# ---- handOutData ----
def handOutData():
	print 'hand out'
	#write "hand out" and timestamp to second recording file

def initKeyBindings():
    """Key bindings for program"""
    #vizact.onkeydown('n',avatarNod)
    vizact.onkeydown('i',#insert "Hand in" in data)
    vizact.onkeydown('o',#insert "Hand out" in data)
    vizact.onkeydown('d',Recording)

def recording():
    """ <Place function description here> """
    print('Recording')
    # TODO: record head XYZ and head pitch yaw roll to file "ParticipantID_Movement.dat"
    # TODO: record keypresses to file "ParticipantID_Events.dat"

initVR()
viz.go()
initModels()
initKeyBindings()

# TODO: initialize slider (we may not be using the slider in this quarter's study)

