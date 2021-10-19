import os
import sys
import scipy.io

try:
    import flap
except ImportError:
    sys.path.append(os.getcwd()+'..//flap')


class RenateSignal(object):
    def __init__(self, path=''):
        self.renate_data = scipy.io.readsav(path)


"""
def DataObject_from_1D_RENATEsav(path,exp_id='',data_title=''):

    sav = scipy.io.readsav(path)
	
    raw_data=sav['data']
    raw_time=sav['t_axis']
	
    time_ax=flap.Coordinate(name='Time',
	                        unit='s',
	                        mode=flap.CoordinateMode(equidistant=True),
							start=0,
							step=raw_time[1]-raw_time[0],
	                        dimension_list=[0],
	                        shape=raw_time.shape)                  
	
    ch_ax=flap.Coordinate(name='Channel',
						  mode=flap.CoordinateMode(equidistant=True),
						  start=0,
						  step=1,
		                  dimension_list=[1],
	                      shape=raw_data.shape[1])
	
    exp_info=flap.Coordinate(name='Info',
							 shape=[],
							 values=sav['shot_data'])
	
    dataobj=flap.DataObject(data_array=raw_data,
	                        data_unit=flap.Unit(name='Ph current',unit='1/s'),
	                        exp_id=exp_id, 
	                        data_title=data_title,
	                        coordinates=[time_ax,ch_ax,exp_info],
	                        data_shape=raw_data.shape)
	
    return dataobj
"""
