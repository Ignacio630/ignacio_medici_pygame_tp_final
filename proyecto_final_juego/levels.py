from config import *
level_map_1 = [
    'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC',
    'C                                                                  C',
    'C                                                                  C',
    'C                                                                  C',
    'C                                                                  C',
    'C                                       L    E   L                 C',
    'C                                        CCCCCCCC                  C',
    'C                            L    E    L                           C',
    'C                            CCCCCCCCCC                            C',
    'C               CCC                                                C',
    'C               CCC                                                C',
    'C    P    F     CCC                            L     E      L      C',
    'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCD'
]

level_map_2 = [
    'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC',
    'CCCCCCCCCC                                                                  C',
    'CCCCCCCCCC                                                                  C',
    'CCCCCCCCCC                                                                  C',
    'CCCCCCCCCC                                                                  C',
    'CCCCCCCCCC                                            L     E      L        C',
    'CCCCCCCCCC                                             CCCCCCCCCCCC         C',
    'CCCCCCCCCC                            L    E    L                           C',
    'CCCCCCCCCC                            CCCCCCCCCC                            C',
    'CCCCCCCCCC                                                                  C',
    'CCCCCCCCCC                                                                  C',
    'CCCCCCCCCC    P                                                             C',
    'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCD',
    'CCCCCCCCCCTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTD',
    'CCCCCCCCCCTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTD'
]

level_map_3 = [
    'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC',
    'C                                                                  C',
    'C                                                                  C',
    'C                                                                  C',
    'C                                              L     E      L      C',
    'C                                               CCCCCCCCCCCC       C',
    'C                                                                  C',
    'C                               L     E      L                     C',
    'C                                CCCCCCCCCCCC                      C',
    'C                       CCC                                        C',
    'C                       CCC                                        C',
    'C    P         F        CCC                                        C',
    'ICCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCD',
    'ITTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTD',
    'ITTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTD'
]


RESOLUTION_WIDTH = 1200
RESOLUTION_HEIGHT = len(level_map_1) * 52
# #Menu
MENU_WIDTH = 400
MENU_HEIGHT = RESOLUTION_HEIGHT

#setup menu
SETUP_MAIN_MENU = ["title","load_game","options","exit"]
SETUP_OPTIONS_MENU = ["sonido","volver"]
SETUP_LEVELS_MENU = ["level_1","level_2","level_3","exit"]