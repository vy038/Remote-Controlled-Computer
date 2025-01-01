# Remote-Controlled-Computer
The objective of this was to experiment with connecting an Arduino serial input with a computer output, in this case being able to execute any command on cmd. An IR sensor would be hooked up to an Arduino, which will receive a signal from a button press, and will use that to send a specific serial message to a port. From that port, the python script running in the background will read the input, and will perform a specified cmd command depending on the message, or button pressed. Different buttons on the remote will perform different functions on a computer when pressed (e.g. power off, log out, all basic commands that can be run from cmd). This proved impractical however, as both programs have to be running in the background for it to work.
