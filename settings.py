#Display settings

DEFAULT_IMAGE_SIZE=(300,300)
FPS=144
HEIGHT=1000
WIDTH=1600
START_X,START_Y=0,-300
X_OFFSET,Y_OFFSET=20,0

BG_IMAGE_PATH='graphics/0/bg.png'
GAME_INDICES=[1,2,3] #there are 0 and 4 outside of the playing area
SYMBOLS_PATH='graphics/0/symbols'

FONT_STYLE='graphics/font/RobotoCondensed-LightItalic.ttf'
FONT_SIZE=32
BIG_FONT_SIZE=48
#Slot symbols
symbols={
    'diamond':f"{SYMBOLS_PATH}/0_diamond.png",
    'floppy':f"{SYMBOLS_PATH}/0_floppy.png",
    'hourglass':f"{SYMBOLS_PATH}/0_hourglass.png",
    'seven':f"{SYMBOLS_PATH}/0_seven.png",
    'telephone':f"{SYMBOLS_PATH}/0_telephone.png",
}