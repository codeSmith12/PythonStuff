

pos = mc.player.getTilePos()
height = 20
for i in range(height):
    mc.setBlocks(pos.x-1-i, pos.y-1-i, pos.z-1-i,  pos.x+1+i, pos.y-1-i, pos.z+1+i, 41)
for i in range(height-2):
    mc.setBlocks(pos.x-1-i, pos.y-2-i, pos.z-1-i,  pos.x+1+i, pos.y-2-i, pos.z+1+i, 0)
