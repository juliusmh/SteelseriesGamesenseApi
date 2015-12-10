# PyGameSense
Control your Steelseries gear using Python. This is very Beta. Only Device added at the Moment is the Steelseries Rival but it is very easy to add custom devices. Color Handlers are written in a <code>json</code> format wich is described <a href="https://github.com/SteelSeries/gamesense-sdk/blob/master/doc/api/writing-handlers-in-json.md">here</a>

To connect to the Gamesense Service, we must get the port (It seems like Steelseries api can only be accesed from localhost). Thats why we have to parse "C:/ProgramData/SteelSeries/SteelSeries Engine 3/coreProps.json" to get the port (<a href="https://github.com/juliusmh/PyGameSense/blob/master/ChangeColorExample.py">Example</a>)
