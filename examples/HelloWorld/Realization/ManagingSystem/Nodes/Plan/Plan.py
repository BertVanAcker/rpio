# **********************************************************************************
# * Copyright (C) 2024-present Bert Van Acker (B.MKR) <bert.vanacker@uantwerpen.be>
# *
# * This file is part of the roboarch R&D project.
# *
# * RAP R&D concepts can not be copied and/or distributed without the express
# * permission of Bert Van Acker
# **********************************************************************************
from rpio.clientLibraries.rpclpy.node import Node
from messages import *
import time
#<!-- cc_include START--!>
# user includes here
#<!-- cc_include END--!>

#<!-- cc_code START--!>
# user code here
#<!-- cc_code END--!>

class Plan(Node):

    def __init__(self, config='config.yaml',verbose=True):
        super().__init__(config=config,verbose=verbose)

        self._name = "Plan"
        self.logger.info("Plan instantiated")

        #<!-- cc_init START--!>
        # user includes here
        #<!-- cc_init END--!>

    # -----------------------------AUTO-GEN SKELETON FOR planner-----------------------------
    def planner(self,msg):
        anomaly = self.knowledge.read("anomaly",queueSize=1)
        _NewPlanMessage = NewPlanMessage()
        _Direction = Direction()

        #<!-- cc_code_planner START--!>

        # user code here for planner

        _NewPlanMessage._NewPlan= "SET VALUE"    # datatype: Boolean
        _Direction._omega= "SET VALUE"    # datatype: Float_64
        _Direction._duration= "SET VALUE"    # datatype: Float_64

        #<!-- cc_code_planner END--!>

        _success = self.knowledge.write(cls=_NewPlanMessage)
        _success = self.knowledge.write(cls=_Direction)

    def register_callbacks(self):
        self.register_event_callback(event_key='anomaly', callback=self.planner)     # LINK <eventTrigger> anomaly
        self.register_event_callback(event_key='anomaly', callback=self.planner)        # LINK <inport> anomaly

def main(args=None):

    node = Plan(config='config.yaml')
    node.register_callbacks()
    node.start()

if __name__ == '__main__':
    main()
    try:
       while True:
           time.sleep(1)
    except:
       exit()