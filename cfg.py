# BASIC SETUP
START = (140, 110)
TARGET = (1150, 750)
OBS_DIM = 20
OBS_NUM = 5
STEP_SIZE = 25

# MAP POINT LIST
LINES = [((90, 0), (90, 300)),
         ((190, 0), (190, 300)),
         ((190, 300), (800, 300)),
         ((800, 300), (1100, 50)),
         ((1100, 50), (1200, 50)),
         ((0, 300), (90, 300)),
         ((0, 400), (300, 400)),
         ((300, 400), (300, 800)),
         ((400, 400), (400, 700)),
         ((400, 400), (550, 400)),
         ((550, 400), (700, 700)),
         ((650, 400), (800, 400)),
         ((650, 400), (800, 700)),
         ((400, 700), (700, 700)),
         ((800, 700), (1100, 700)),
         ((1100, 700), (1100, 150)),
         ((800, 400), (1100, 150))]

# TRIANGLE OUT CHECKLIST (random point should not generate in these areas)
OUT_TRI_1_POINTS = ((550, 400), (550, 700), (700, 700))
OUT_TRI_2_POINTS = ((650, 400), (800, 400), (800, 700))
OUT_TRI_3_POINTS = ((800, 400), (1100, 400), (1100, 150))
OUT_TRI_4_POINTS = ((1100, 50), (800, 50), (800, 400))
OUT_TRI_LIST = [OUT_TRI_1_POINTS, OUT_TRI_2_POINTS, OUT_TRI_3_POINTS, OUT_TRI_4_POINTS]

# RECTANGLE OUT CHECKLIST (random point should not generate in these areas)
OUT_RECT_1 = ((0, 0), (90, 300))  # top-x, top-y, width, height
OUT_RECT_2 = ((190, 0), (610, 300))
OUT_RECT_3 = ((800, 0), (400, 50))
OUT_RECT_4 = ((0, 400), (300, 400))
OUT_RECT_5 = ((400, 400), (150, 300))
OUT_RECT_6 = ((800, 400), (300, 300))
OUT_RECT_LIST = [OUT_RECT_1, OUT_RECT_2, OUT_RECT_3, OUT_RECT_4, OUT_RECT_5, OUT_RECT_6]
