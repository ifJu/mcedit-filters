# Filter By ifJu
# -- Command Block --
# Manage command blocks with the MCEdit filter ! (command, name)

from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_String

displayName = "Command Block"

inputs = (
	("Get infos : ", True),
	("Set command : ", False),
	("Set name : ", False),
	("New command :", "string"),
	("New name :", "string"),
)

formatCode = unichr(167)

def perform(level, box, options):
	infos = options["Get infos : "]
	setcmd = options["Set command : "]
	setname = options["Set name : "]
	newcmd = options["New command :"]
	newname = options["New name :"]
	x = box.minx
	y = box.miny
	z = box.minz
	mx = box.maxx-1
	my = box.maxy-1
	mz = box.maxz-1
	if z == mz and y == my and x == mx:
		if level.blockAt(x, y, z) == 137:
			for (chunk, slices, point) in level.getChunkSlices(box):
				for t in chunk.TileEntities:
					if t["id"].value == "Control":
						if setname:
							t["CustomName"] = TAG_String(newname)
						chunk.dirty = True
						
						if setcmd:
							t["Command"] = TAG_String(newcmd)

						curcmd = t["Command"].value
						curname = t["CustomName"].value
						datavalue = level.blockDataAt(x, y, z)

						if infos:
							raise Exception("Block: 137 ( minecraft:command_block )\nData value: " + str(datavalue) + "\nName: " + str(curname) + "\nCommand: " + str(curcmd))
		else:
			raise Exception("The box does'nt contain a command block ! :(")
	else:
		raise Exception("The box is too big ! ( max 1x1x1 ) :(")
