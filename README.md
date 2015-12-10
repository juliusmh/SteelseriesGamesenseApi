# PyGameSense
<pre>PyGameSense requieres <a href="http://docs.python-requests.org/en/latest/">Requests</a></pre>
Control your Steelseries gear using Python. This is very Beta. Only device added at the Moment is the Steelseries Rival but it is very easy to add custom devices. Handlers are written in a <code>json</code> format wich is described <a href="https://github.com/SteelSeries/gamesense-sdk/blob/master/doc/api/writing-handlers-in-json.md">here</a>

To connect to the Gamesense Service, we must get the port (It seems like Steelseries api can only be accesed from localhost). Thats why we have to parse "C:/ProgramData/SteelSeries/SteelSeries Engine 3/coreProps.json" to get the port (<a href="https://github.com/juliusmh/PyGameSense/blob/master/ChangeColorExample.py">Example</a>)

<h2>Colors</h2>
Some colors are defined in <code>PyGameSense.Colors</code>. Others are triplets like (r,g,b) (0,0,0) -> (255,255,255)

<h2>Creating handlers</h2>
Read the <a href="https://github.com/SteelSeries/gamesense-sdk/blob/master/doc/api/writing-handlers-in-json.md">official docs first</a>. A handler in Python is always and array containing a dict like so:
<p><code> handler = [{"device-type" : device_type, "zone" : zone, "mode": mode}] </code></p>
It is possible to use the helper function <code>build_handler</code> like so:
<pre>#GradientHandler      
handler = self.build_handler("rgb-2-zone", "two", "color", {"gradient" : {"zero" : {"red" : 0, "green" : 0, "blue":0}, "hundred" :{"red" : r, "green" : g, "blue":b}}})

#StaticColorHandler   
handler = self.build_handler("rgb-2-zone", "two", "color", {"red" : r, "green" :g, "blue":b})</pre>

<h2>Look at the code </h2>
Take a look at the code. It is easy to understand and is friendly for newbies creating simple effects like the rgb rainbow that is already predefined. 

<h2>Credits</h2>
Project by Julius Hinze 2015. Feel free to clone and use the code as you want.
