from IPython.display import HTML, Audio, clear_output, Image
from google.colab.output import eval_js
from base64 import b64decode, b64encode
import numpy as np
from scipy.io.wavfile import read as wav_read
import io
import ffmpeg
from google.colab import files
import os
import cv2

import shutil
from google.colab import drive

import moviepy.editor as mp

from IPython.core.display import display

from ghc.l_ghc_cf import l_ghc_cf

# Copyright

copyright = '<div style="background-color: #dff2bf; border: 1px solid rgb(79, 138, 16); color: #4f8a10; padding: 10px;"><div class="separator" style="clear: both; direction: rtl; text-align: left;"><span style="font-family: arial; font-size: medium;">Этот код создан AndikSoft</span></div><div class="separator" style="clear: both; direction: rtl; text-align: left;"><span style="font-family: arial; font-size: medium;"><br /></span></div><div class="separator" style="clear: both; direction: rtl; text-align: left;"><div class="separator" style="clear: both; text-align: center;"><a href="https://www.youtube.com/@AndikSoft" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" data-original-height="170" data-original-width="600" height="170" src="https://andiksoft.ru/wp-content/uploads/2023/01/05.png" width="600" /></a></div></div><div class="separator" style="clear: both; direction: rtl; text-align: left;"><span style="font-family: arial; font-size: medium;"><br /></span></div><div style="direction: rtl; text-align: left;"><span style="font-family: arial; font-size: medium;">✅&nbsp;<a href="https://www.youtube.com/@AndikSoft" target="_blank">Нажмите здесь</a>&nbsp;Больше объяснений на моем канале. ✅</span></div></div>'
display(HTML(copyright))