from gpiozero import PWMLED
from signal import pause
from gpiozero_ps.generators import triangular, gaussian, maxed, squared
from gpiozero_ps.console import ProgressBarOutput
from gpiozero.tools import clamped, scaled
from itertools import tee


slow = clamped(scaled(
    triangular(gaussian(30, 5), gaussian(30, 5), gaussian(0.7, 0.1)),
    0.1, 0.5, 0, 1), 0, 1)

fast = clamped(triangular(gaussian(6, 2), gaussian(2, 1), gaussian(0.8, 0.06), gaussian(5, 5)), 0, 1)

(fastR, fastY, fastPB) = tee(fast, 3)
(slowR, slowPB) = tee(slow, 2)

(sourceR, sourcePB) = tee(squared(maxed(slowR, fastR)), 2)
sourceY = squared(scaled(fastY, 0, 0.2, 0, 1))

pb = ProgressBarOutput(length=100)
pb.source = sourcePB

led_red = PWMLED(24)
led_red.source = sourceR

led_yellow = PWMLED(25)
led_yellow.source = sourceY

pause()
