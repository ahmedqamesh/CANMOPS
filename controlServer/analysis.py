from __future__ import division
import numpy as np
import logging
import numba
import tables as tb
from scipy.optimize import curve_fit
class Analysis(object):
    
    def __init__(self):
        pass
    # Conversion functions
    def adc_conversion(self, adc_channels_reg="V", value=None,resistor_ratio = 1):
        '''
        the function will convert each ADC value into a reasonable physical quantity
        > MOPS has 12 bits ADC value ==> 2^12 = 4096 (this means that we can read from 0 -> 4096 different decimal values)
        > The full 12 bits ADC covers up to 850mV
        >This means that each ADC value corresponds to 850/4096 = 0.207 mV for 1 bit this is the resolution of the ADC)
        > The true voltage on each ADC is V = value * resistance
        Example: 
        Each ADC value should be multiplied by 0.207 to give the answer in mV
        To measure Voltage: the value should be multiplied by 40 (Resistor ratio)
        '''
        if value is not None:
            if adc_channels_reg == "V":
                value = value * 850/4096 * 10e-6 *resistor_ratio
            elif adc_channels_reg == "T":
                value = value * 850/4096 * 10e-6 *resistor_ratio
            else:
                value = value * 850/4096 * resistor_ratio
        return value
    def convertion(self,value =None):
        return value
    
    def NTC_convertion(self,value =None):
        '''
        To convert ADC data to temperature you first find the thermistor resistance and then use it to find the temperature.
        https://www.jameco.com/Jameco/workshop/techtip/temperature-measurement-ntc-thermistors.html
        Rt = R0 * (( Vs / Vo ) - 1) 
        
        '''
       
        return value
if __name__ == "__main__":
        pass
