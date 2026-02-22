import getchoice
import runchoice


actionchoice, devicechoice = getchoice.action_and_device()

runchoice.run_it(actionchoice, devicechoice)
