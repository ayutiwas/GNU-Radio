#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Oct 20 16:47:56 2017
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy


class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 10
        self.samp_rate = samp_rate = int(0.5E6)
        self.bps = bps = 4

        self.variable_constellation_2 = variable_constellation_2 = digital.constellation_16qam().base()


        self.variable_constellation_1 = variable_constellation_1 = digital.constellation_16qam().base()

        self.upsamp_rate = upsamp_rate = samp_rate * 8 * sps / bps

        ##################################################
        # Blocks
        ##################################################
        self.digital_constellation_modulator_1 = digital.generic_mod(
          constellation=variable_constellation_1,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.channels_fading_model_1 = channels.fading_model( 8, 0, False, 4.0, 0 )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0.1,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1+1j, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_skiphead_0_0 = blocks.skiphead(gr.sizeof_gr_complex*1, 1024)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_head_0_0 = blocks.head(gr.sizeof_gr_complex*1, 50000000)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/wsrg/verilog/research-ayush/matlab/MU_Detection/base_band.dat', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.analog_sig_source_x_1 = analog.sig_source_c(upsamp_rate, analog.GR_COS_WAVE, 0, 0.31623, 0)
        self.analog_random_source_x_1 = blocks.vector_source_b(map(int, numpy.random.randint(0, 255, 10000000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_1, 0), (self.blocks_throttle_1, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_head_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.channels_fading_model_1, 0))
        self.connect((self.blocks_skiphead_0_0, 0), (self.blocks_head_0_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.digital_constellation_modulator_1, 0))
        self.connect((self.channels_channel_model_0, 0), (self.blocks_skiphead_0_0, 0))
        self.connect((self.channels_fading_model_1, 0), (self.channels_channel_model_0, 0))
        self.connect((self.digital_constellation_modulator_1, 0), (self.blocks_multiply_xx_1, 0))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_upsamp_rate(self.samp_rate * 8 * self.sps / self.bps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_upsamp_rate(self.samp_rate * 8 * self.sps / self.bps)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)

    def get_bps(self):
        return self.bps

    def set_bps(self, bps):
        self.bps = bps
        self.set_upsamp_rate(self.samp_rate * 8 * self.sps / self.bps)

    def get_variable_constellation_2(self):
        return self.variable_constellation_2

    def set_variable_constellation_2(self, variable_constellation_2):
        self.variable_constellation_2 = variable_constellation_2

    def get_variable_constellation_1(self):
        return self.variable_constellation_1

    def set_variable_constellation_1(self, variable_constellation_1):
        self.variable_constellation_1 = variable_constellation_1

    def get_upsamp_rate(self):
        return self.upsamp_rate

    def set_upsamp_rate(self, upsamp_rate):
        self.upsamp_rate = upsamp_rate
        self.analog_sig_source_x_1.set_sampling_freq(self.upsamp_rate)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
