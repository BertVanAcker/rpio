#**********************************************************************************
# * Copyright (C) 2024-present Bert Van Acker (B.MKR) <bert.vanacker@uantwerpen.be>
# *
# * This file is part of the roboarch R&D project.
# *
# * RAP R&D concepts can not be copied and/or distributed without the express
# * permission of Bert Van Acker
# **********************************************************************************
from rpio.parsers.parsers import *


# 1. Setup the robochart parser
parser = robochart_parser(MAPLEK='input/MAPLE-K.rct',Monitor='input/Monitor.rct',Analysis='input/Analysis.rct',Plan='input/Plan.rct',Legitimate='input/Legitimate.rct',Execute='input/Execute.rct',Knowledge='input/Knowledge.rct')

x=1