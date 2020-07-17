#! /usr/bin/env python

import rospy
from enum import Enum
from JobManager.Job import Job
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
import time
from simple_sim.srv import AssignJobToMex,AssignJobToMexResponse 

class MExStatus(Enum):
    """ Class that acts as Enumerator for Mobile Executor (MEx) status. """
    STANDBY = 0
    CHARGING = 1
    ASSIGNED = 2
    EXECUTING_TASK = 3
    ERROR = 4

class MobileExecutor:
    """ Class with Mobile Executor (MEx) information (MEx id, status, assigned job id) """
    def __init__(self, id, status=MExStatus.STANDBY, job_id=None):
        self.id = id                # Unique identifier for this MEx, e.g. "rdg01"
        self.status = status        # Status of the MEx (STANDBY, CHARGING, ASSIGNED, EXECUTING_TASK, ERROR)
        self.job_id = job_id        # The unique id of the job the MEx is assigned to.
    def mex_info(self):
        print('Mobile executor #' + str(self.id) + '\nStatus: ' + str(self.status.name) + '\nJob_id: ' + str(self.job_id) + '\n')
        #rospy.loginfo('Mobile executor #' + str(self.id) + '\nStatus: ' + str(self.status.name) + '\nJob_id: ' + str(self.job_id) + '\n')
        #mexinfo = ('Mobile executor #' + str(self.id) + '\nStatus: ' + str(self.status.name) + '\nJob_id: ' + str(self.job_id) + '\n')
        #return mexinfo
#--------------------MEX initialization--------------------------
rdg01 = MobileExecutor('rdg01')
#rdg01.mex_info()

rdg02 = MobileExecutor('rdg02')
#rdg02.mex_info()

rdg03 = MobileExecutor('rdg03')
#rdg03.mex_info()

mex_list = [rdg01, rdg02, rdg03]
#---------------------------------------------------------------

def my_callback_1(request):
    #all_mex_with_status = []
    for i in mex_list:
        #all_mex_with_status.append(i.mex_info())
        i.mex_info()
    #print(all_mex_with_status)
    return EmptyResponse()
#service to provide all mex with status

def assign_job(request):
    assignment = False
    for i in mex_list:
        if i.id == request.mex_id:
            i.job_id = request.job_id
            i.status = MExStatus.ASSIGNED
            assignment = True
        #else:
        #    break
    if assignment == True:
        response = AssignJobToMexResponse()
        response.success = True
    else:
        response = AssignJobToMexResponse()
        response.success = False
    return response

def de_assign_job(request):
    de_assignment = False
    for i in mex_list:
        if i.id == request.mex_id:
            i.job_id = None
            i.status = MExStatus.STANDBY
            de_assignment = True
    if de_assignment == True:
        response = AssignJobToMexResponse()
        response.success = True
    else:
        response = AssignJobToMexResponse()
        response.success = False
    return response

rospy.init_node('get_mex_list_service_server')

get_mex_list_service = rospy.Service('/get_mex_list', Empty , my_callback_1) # create the Service called my_service with the defined callback

assign_job_to_mex_service = rospy.Service('/assign_job_to_mex', AssignJobToMex, assign_job)

de_assign_job_from_mex_service = rospy.Service('/de_assign_job_from_mex', AssignJobToMex, de_assign_job)

rospy.spin() # maintain the service open.



"""
class MexType(Enum):
    
    AGV_TRANSPORT = 0
    AGV_MOBILE_MANIPULATOR = 1
    AGV_MACHINERY = 2
    FORKLIFT = 3

class MexServiceStatus(Enum):
    
    OUT_OF_SERVICE = 0
    IN_SERVICE = 1

class MexInServiceStatus(Enum):
    
    BUSY = 0
    AVALIABLE = 1
    NONE = 2

class Mex:
    def __init__(self, id, m_type):
        self.mex_id = id
        self.mex_type = m_type
        self.service_status = MexServiceStatus.OUT_OF_SERVICE
        self.in_service_status = MexInServiceStatus.NONE
        self.current_job = None
    def mex_info(self):
        print('Mobile executor #' + str(self.mex_id) + ' info:\nType: ' + str(self.mex_type.name) + '\nService status: ' + str(self.service_status.name) + '\nIn service status: ' + str(self.in_service_status.name) + '\nCurrent job: ' + str(self.current_job) + '\n')

robot1 = Mex('rdg01', MexType.AGV_TRANSPORT)
#robot1.mex_info()
robot2 = Mex('rdg02', MexType.AGV_TRANSPORT)
robot2.service_status = robot2.service_status.IN_SERVICE
robot2.in_service_status = robot2.in_service_status.BUSY
robot2.current_job = '003'
#robot2.mex_info()

mex_list = [robot1.mex_id, robot2.mex_id]

def my_callback_1(request):
   print(mex_list)
   return EmptyResponse() # the service Response class, in this case EmptyResponse

rospy.init_node('get_mex_list_service_server', anonymous=True)

my_service = rospy.Service('/get_mex_list', Empty , my_callback_1) # create the Service called my_service with the defined callback
pub = rospy.Publisher('avaliable_mex_list', list, )

rospy.spin() # maintain the service open."""