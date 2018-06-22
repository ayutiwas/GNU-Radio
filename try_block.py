#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Try Block
# Generated: Fri Nov 10 11:18:09 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy
import sip
import sys
from gnuradio import qtgui


class try_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Try Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Try Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "try_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

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
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=10,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=10,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	upsamp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(False)



        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, upsamp_rate, 0.5e6, 1000, firdes.WIN_HAMMING, 6.76))
        self.digital_constellation_modulator_1 = digital.generic_mod(
          constellation=variable_constellation_1,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.digital_constellation_modulator_0 = digital.generic_mod(
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
        	noise_voltage=1,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1+1j, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_skiphead_0_0 = blocks.skiphead(gr.sizeof_gr_complex*1, 1024)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((10, ))
        self.blocks_head_0_0 = blocks.head(gr.sizeof_gr_complex*1, 10000000)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 5000000)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_1 = analog.sig_source_f(upsamp_rate, analog.GR_SQR_WAVE, -1, 0, 0)
        self.analog_random_source_x_1 = blocks.vector_source_b(map(int, numpy.random.randint(0, 255, 10000000)), True)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 255, 10000000)), True)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.blocks_throttle_1, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_head_0_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.channels_fading_model_1, 0))
        self.connect((self.blocks_skiphead_0_0, 0), (self.blocks_head_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.digital_constellation_modulator_1, 0))
        self.connect((self.channels_channel_model_0, 0), (self.blocks_skiphead_0_0, 0))
        self.connect((self.channels_fading_model_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.digital_constellation_modulator_1, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "try_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

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
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

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
        self.qtgui_sink_x_0.set_frequency_range(0, self.upsamp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.upsamp_rate, 0.5e6, 1000, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1.set_sampling_freq(self.upsamp_rate)


def main(top_block_cls=try_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
