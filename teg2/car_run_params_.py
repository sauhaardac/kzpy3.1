# This is used to specifiy caffe mode and data file name information


from kzpy3.utils import time_str
from kzpy3.utils import opjh
import os

print "***************** car_run_params.py"

computer_name = "MR_Unknown"
try:  
   computer_name = os.environ["COMPUTER_NAME"]
except KeyError: 
   print """********** Please set the environment variable computer_name ***********
   e.g.,
   export COMPUTER_NAME="Mr_Orange"
   """


####################### general car settings ################
#
for i in range(5):
	print('*************' + computer_name + '***********')
Direct = 1.
Follow = 0.
Play = 0.
Furtive = 0.
Caf = 1.0
Racing = 0.0
Location = 'Smyth_tape'

solver_file_path = opjh("kzpy3/caf5/z2_color/solver_live.prototxt")
weights_file_path = opjh("kzpy3/caf6/z2_color_more/z2_color_more.caffemodel")


weights_file_path = opjh("kzpy3/caf6/z2_color_more/z2_color_more_2.caffemodel")

weights_file_path = opjh("kzpy3/caf7/z2_color/z2_color_state_1_5_6_7_iter_4000000.caffemodel")
weights_file_path = opjh("kzpy3/caf7/z2_color/z2_color_state_1_5_6_7_iter_6000000.caffemodel")
weights_file_path = opjh("kzpy3/caf7/z2_color/z2_color_state_1_5_6_7_iter_10900000.caffemodel")
#weights_file_path = opjh("kzpy3/caf7/z2_color/z2_color_state_1_5_6_7_iter_8000000.caffemodel")
#weights_file_path = opjh("kzpy3/caf6/z2_color_more/z2_color_more_3.caffemodel")
weights_file_path = opjh("kzpy3/caf7/z2_color/solver_state_1_5_6_7_plus_extra_Smyth_racing_iter_400000.caffemodel")
#weights_file_path = opjh("kzpy3/caf5/z2_color/z2_color.caffemodel")
verbose = False

steer_gain = 1.0


#
###################################################################

####################### specific car settings ################
#
if computer_name == 'Mr_Orange':
	motor_gain = 1.0
	pass
if computer_name == 'Mr_Silver':
	motor_gain = 1.0
	pass
if computer_name == 'Mr_Blue':
	motor_gain = 1.3
	pass
if computer_name == 'Mr_White':
	motor_gain = 1.0
	pass
if computer_name == 'Mr_Black':
	motor_gain = 1.4
	pass
if computer_name == 'Mr_Teal':
	motor_gain = 1.0
	pass
if computer_name == 'Mr_Audi':
	motor_gain = 1.0
	pass
if computer_name == 'Mr_Purple':
	motor_gain = 1.0
	pass
if computer_name == 'Mr_LightBlue':
	motor_gain = 1.0
	pass
if computer_name == 'Mr_Yellow':
	motor_gain = 1.0
	pass

#
###################################################################
# motor_gain = 1.0 # override individual settings

if Direct == 1:
	task = 'direct'
elif Play == 1:
	task = 'play'
elif Follow == 1:
	task = 'follow'
elif Furtive == 1:
	task = 'furtive'
elif Racing == 1:
	task = 'racing'
else:
	assert(False)


foldername = ''
if Follow == 1:
	foldername = 'follow_'

model_name = solver_file_path.split('/')[-2]

if Caf == 1:
	foldername = foldername + 'caffe2_' + model_name +'_'

foldername = foldername + task + '_'

foldername = foldername + Location + '_'

foldername = foldername + time_str() + '_'

foldername = foldername + computer_name





GPS2_lat_orig = 37.881404 #-999.99
GPS2_long_orig = -122.2743327 #-999.99
GPS2_radius = 0.0004

MLK_pm_lat,MLK_pm_lon = 37.881556,-122.278434
MLK_pm2_lat,MLK_pm2_lon = 37.881496, -122.278552 # 12 meters from pitcher's mound.

RFS_lat,RFS_lon = 37.91590,-122.3337223
RFS_lat2,RFS_lon2 = 37.915846, -122.333404 # 28 meters from field center.

M_1408_lat,M_1408_lon = 37.881401062, -122.27230072 #37.8814082,-122.2722957

miles_per_deg_lat = 68.94
miles_per_deg_lon_at_37p88 = 54.41
meters_per_mile = 1609.34

GPS2_lat_orig = M_1408_lat
GPS2_long_orig = M_1408_lon
GPS2_radius_meters = 800000000


RFS_start_lat,RFS_start_lon = 37.916731,-122.334096
RFS_end_lat,RFS_end_lon = 337.918258,-122.3342703

GPS2_radius_meters = 938442714

def lat_lon_to_dist_meters(lat_A,lon_A,lat_B,lon_B):
        dx = (lat_A-lat_B)*miles_per_deg_lat*meters_per_mile
        dy = (lon_A-lon_B)*miles_per_deg_lon_at_37p88*meters_per_mile
        return np.sqrt(dx**2+dy**2)





