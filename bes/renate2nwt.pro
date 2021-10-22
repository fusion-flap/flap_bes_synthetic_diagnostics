;********************************************************************************************************
; Name: renate2nwt.pro
;
; PURPOSE
; =======
; This program converts data exported from RENATE synthetic diagnostic to sav output to NTI Wavelet Tools compatible sav.
;
; INPUTS
; =======
; filename:               Name of text file to convert with path
;
; OUTPUT
; =======
; .sav file in a format cmpatible with NWT
; 
; USAGE
; =======
; renate2nwt,'/data/.nobackup/balazsp/Trunk/output/99995_JT60SA_1_200_101_synth_diag_output.sav'
; 
;********************************************************************************************************
pro renate2nwt, filepathname
  
  restore,filepathname
    
  output_filename = filepathname+'_nwt.sav'
   
  channel_size = 96
  rows = 4 
  
  data = transpose(data)
  timeax = t_axis
  phi = fltarr(channel_size)
  theta = [0.02+fltarr(channel_size/rows),0.011+fltarr(channel_size/rows),-0.003+fltarr(channel_size/rows),-0.011+fltarr(channel_size/rows)] ; z coordinates in meters
  shotnumber = long(shot_data.shot_number)
  expname = shot_data.appliance_name+'_'+string(shot_data.shot_index)+'_'+shot_data.sol_scenario
  channels = string(indgen(channel_size))
  coord_history = 'Approximate z value from the observed quadrilaterals figure'
  data_history = 'RENATE-JOREK simulation'
  
  save, data, timeax, phi, theta, shotnumber, expname, channels, coord_history, data_history,$
      filename=output_filename
      
  print, 'RENATE-JOREK data written to ' + output_filename
      
end