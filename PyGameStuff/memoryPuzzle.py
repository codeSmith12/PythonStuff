import pygame, sys, random
from pygame.locals import *

FPS = 165
windowWidth = 1280
windowHeight = 960
revealSpeed = 8
boxSize = 80
gapSize = 10
boardWidth = 5
boardHeight = 4

assert(boardWidth * boardHeight) % 2 == 0, 'Board needs to have even number of boxes for pairs of matches'
xMargin = int((windowWidth - (boardWidth * (boxSize + gapSize))) / 2)
yMargin = int((windowHeight - (boardHeight * (boxSize + gapSize))) / 2)

GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255,255,0)
ORANGE = (255,128,0)
PURPLE = (255,0,255)
CYAN = (0, 255, 255)

bgColor = NAVYBLUE
lightBgColor = GRAY
boxColor = WHITE
highlightColor = BLUE
donut = "donut"
square = "square"
diamond = "diamond"
lines = "lines"
oval = "oval"

allColors = (RED,GREEN,BLUE,YELLOW,ORANGE,PURPLE,CYAN)
allShapes = (donut, square, diamond, lines, oval)
assert len(allColors) * len(allShapes) * 2 >= boardWidth * boardHeight, "Board is too big for the number of shapes / colors defined"

def main():
    global fpsClock, displaySurf
    pygame.init()
    fpsClock = pygame.time.Clock()
    displaySurf = pygame.display.set_mode((windowWidth, windowHeight))

    mouseX = 0

    fpsClock = pygame.time.Clock()
    displaySurf = pygame.display.set_mode((windowWidth, windowHeight))

    mouseX = 0
    mouseY = 0
    pygame.display.set_caption("Memory Game")
    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None

    displaySurf.fill(bgColor)
    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False

        displaySurf.fill(bgColor)
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
                mouseClicked = True
        boxX, boxY = getBoxAtPixel(mouseX, mouseY)
        if boxX != None and boxY != None:
            # the mouse is currently over a box
            if not revealedBoxes[boxX][boxY]:
                drawHighlightBox(boxX, boxY)
            if not revealedBoxes[boxX][boxY] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxX, boxY)])
                revealedBoxes[boxX][boxY] = True

                if firstSelection == None:
                    firstSelection = (boxX, boxY)
                else: # the current box was the second box clicked
                        # Check if there is a match between the two icons.
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxX, boxY)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        # icons dont match, recover both selections
                        pygame.time.wait(1000)
                        coverBoxesAnimation(mainBoard, [(firstSelection[0],firstSelection[1]), (boxX, boxY)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxX][boxY] = False
                    elif hasWon(revealedBoxes):
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)

                        # Reset board
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        # Show the fully unrevealed board for a second.
                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        # Replay the start game animation
                        startGameAnimation(mainBoard)
                    firstSelection = None
            pygame.display.update()
            fpsClock.tick(FPS)

def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(boardWidth):
        revealedBoxes.append([val] * boardHeight)
    return revealedBoxes

def getRandomizedBoard():
    icons = []
    for color in allColors:
        for shape in allShapes:
            icons.append((shape, color))
    random.shuffle(icons)
    numIconsUsed = int(boardWidth * boardHeight / 2)

    icons = icons[:numIconsUsed] * 2
    random.shuffle(icons)

    board = []
    for x in range(boardWidth):
        column = []
        for y in range(boardHeight):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board

def splitIntoGroupsOf(groupSize, theList):
    # splits list into a list of lists, where the ineer lists have
    # at most groupsize number of items
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i+groupSize])
    return result

def leftTopCoordsOfBox(boxX, boxY):
    # convert board coordinates to pixel coordinates
    left = boxX * (boxSize + gapSize) + xMargin
    top = boxY * (boxSize + gapSize) + yMargin
    return (left, top)

def getBoxAtPixel(x,y):
    for boxX in range(boardWidth):
        for boxY in range(boardHeight):
            left, top = leftTopCoordsOfBox(boxX, boxY)
            boxRect = pygame.Rect(left, top, boxSize, boxSize)
            if boxRect.collidepoint(x,y):
                return (boxX, boxY)
    return (None,None)

def drawIcon(shape, color, boxX, boxY):
    quarter = int(boxSize * .25)
    half = int(boxSize * .5)

    # get pixel coords from box coords
    left, top = leftTopCoordsOfBox(boxX, boxY)

    #draw the shapes
    if shape == donut:
        pygame.draw.circle(displaySurf, color, (left + half, top + half), half-5)
        pygame.draw.circle(displaySurf, bgColor, (left + half, top + half), quarter-5)
    elif shape == square:
        pygame.draw.rect(displaySurf, color, (left+quarter, top+quarter, boxSize-half, boxSize -half))
    elif shape == diamond:
        pygame.draw.polygon(displaySurf, color, ((left+half, top), (left + boxSize - 1, top+half), (left+half, top+boxSize-1), (left, top+half)))
    elif shape == lines:
        for i in range(0, boxSize, 4):
            pygame.draw.line(displaySurf, color, (left,top+i), (left+i, top))
            pygame.draw.line(displaySurf, color, (left+i,top + boxSize -1), (left+boxSize-1, top+i))
    elif shape == oval:
        pygame.draw.ellipse(displaySurf, color, (left, top + quarter, boxSize, half))

def getShapeAndColor(board, boxX, boxY):
    return board[boxX][boxY][0],board[boxX][boxY][1]

def drawBoxCovers(board, boxes, coverage):
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        pygame.draw.rect(displaySurf, bgColor, (left, top, boxSize, boxSize))
        shape, color = getShapeAndColor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])
        if coverage > 0:
            pygame.draw.rect(displaySurf, boxColor, (left, top, coverage, boxSize))
            pygame.display.update()
            fpsClock.tick(FPS)

def revealBoxesAnimation(board, boxesToReveal):
    for coverage in range(boxSize, (-revealSpeed) - 1, - revealSpeed):
        drawBoxCovers(board,boxesToReveal, coverage)

def coverBoxesAnimation(board, boxesToCover):
    for coverage in range(0, boxSize + revealSpeed, revealSpeed):
        drawBoxCovers(board, boxesToCover, coverage)

def drawBoard(board, revealed):
    for boxX in range(boardWidth):
        for boxY in range(boardHeight):
            left, top = leftTopCoordsOfBox(boxX,boxY)
            if not revealed[boxX][boxY]:
                pygame.draw.rect(displaySurf, boxColor, (left, top, boxSize, boxSize))
            else:
                shape, color = getShapeAndColor(board, boxX, boxY)
                drawIcon(shape, color, boxX, boxY)
def drawHighlightBox(boxX, boxY):
    left, top = leftTopCoordsOfBox(boxX, boxY)
    pygame.draw.rect(displaySurf, highlightColor, (left -5, top - 5, boxSize + 10, boxSize+10), 4)

def startGameAnimation(board):
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(boardWidth):
        for y in range(boardHeight):
            boxes.append( (x,y) )
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8, boxes)

    drawBoard(board, coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board, boxGroup)
        coverBoxesAnimation(board, boxGroup)

def gameWonAnimation(board):

    coveredBoxes = generateRevealedBoxesData(True)
    color1 = lightBgColor
    color2 = bgColor

    for i in range(13):
        color1, color2 = color2, color1
        displaySurf.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)

def hasWon(revealedBoxes):
    for i in revealedBoxes:
        if False in i:
            return False
    return True

if __name__ ==  '__main__':
    main()
