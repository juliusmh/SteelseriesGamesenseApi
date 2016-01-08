# -------------------------------------------------------------------------------
# Name:        PYTHON_GAMESENSE
#
# Author:      Julius
#
# Created:     25/11/2015
# Copyright:   (c) Julius 2015
#
# GradientHandler      handler = self.build_handler("rgb-2-zone", "two", "color", {"gradient": {"zero": {"red": 0, "green": 0, "blue": 0}, "hundred": {"red": r, "green": g, "blue":b}}})
# StaticColorHandler   handler = self.build_handler("rgb-2-zone", "two", "color", {"red": r, "green": g, "blue":b})
# -------------------------------------------------------------------------------

import requests
import time


# STATIC COLORS
class Colors:
    WHITE  = (255, 255, 255)
    BLACK  = (0, 0, 0)
    RED    = (255, 0, 0)
    GREEN  = (0, 255, 0)
    BLUE   = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PINK   = (255, 0, 255)
    CYAN   = (0, 255, 255)


# GAMESENSEBRIDGE MAIN CLASS
class GameSenseBridge:
    # -----INIT-----
    def __init__(self,  gs_ip, gs_port):
        # ESTABLISH OUR CONNECTION TO STEELSERIES SERVER
        self.gs_port = gs_port
        self.gs_ip = gs_ip
        self.gsurl = "http://%s:%s/" % (gs_ip, gs_port)
        # OUR REQUEST SESSION
        self.session = requests.session()
        # MISC
        self.is_connected = self.reachable_host(self.gsurl)
        self.effects = None

    # -----HELPER FUNCTIONS-----
    # GET THE EFFECTS CLASS
    def getEffects(self):
        if self.effects is None:
            self.effects = GameSenseEffects(self)
        return self.effects

    # BUILD A NEW UNIVERSIAL HANDLER
    def build_handler(self, device_type, zone, mode, color):
        handler = {"device-type": device_type, "zone": zone, "mode": mode}
        handler["color"] = color
        return [handler]

    # CHECK IF AN GAMESENSE SERVER IS REACHABLE
    def reachable_host(self, url):
        try:
            self.session.get(url)
            return True
        except:
            return False

    # -----API FUNCTIONS-----
    # SEND REQUEST TO RESTFULL API
    def _post(self, endpoint, payload):
        try:
            self.session.post(self.gsurl + endpoint, json=(payload))
            return True
        except:
            return False

    # REGISTER A NEW GAME
    def register_game(self, game_name, game_display_name, icon_color_id):
        payload = {"game": game_name, "game_display_name": game_display_name, "icon_color_id": icon_color_id}
        return self._post("game_metadata", payload)

    # REMOVES THE GAME WITH NAME
    def unregister_game(self, game_name):
        payload = {"game": game_name}
        return self._post("remove_game", payload)

    # REGISTER A NEW EVENT
    def register_event(self, game_name, event, min_value, max_value, icon_id):
        payload = {"game": game_name, "event": event, "min_value": min_value, "max_value": max_value, "icon_id": icon_id}
        return self._post("register_game_event", payload)

    # REMOVES AN EVENT
    def unregister_event(self, game_name, event):
        payload = {"game": game_name, "event": event}
        return self._post("remove_game_event", payload)

    # BINDS AN EVENT TO AN HANDLER
    def bind_event(self, game_name, event, min_value, max_value, icon_id, handler):
        payload = {"game": game_name, "event": event, "min_value": min_value, "max_value": max_value, "icon_id": icon_id}
        payload["handlers"] = handler
        return self._post("bind_game_event", payload)

    # TRIGGERS A GAMEEVENT FOR THE GIVEN GAME NAME
    def send_gameevent(self, game_name, event, value):
        payload = {"game": game_name, "event": event}
        payload["data"] = {"value": value}
        return self._post("game_event", payload)

    # SENDING KEEP ALIVE PACKAGES
    def send_hartbeat(self, game_name):
        payload = {"game": game_name}
        return self._post("game_heartbeat", payload)

    def enter_heartbeat_loop(self, game_name):
        try:
            while True:
                self.send_hartbeat(game_name)
                time.sleep(10)
        except KeyboardInterrupt:
            return None


# GAMESENSEBRIDGE
class GameSenseEffects:
    def __init__(self, gs):
        self.gs = gs

    # SHOW A STATIC COLOR
    def show_static_color(self, game_name, device_type, zones, color):
        (r, g, b) = color
        for zone in zones:
            handler = self.gs.build_handler(device_type, zone, "color", {"red": r, "green": g, "blue": b})
            self.gs.bind_event(game_name, "COLOR", 0, 100, 16, handler)
            self.gs.send_gameevent(game_name, "COLOR", 100)

    # SINGLE COLOR RAINBOW
    def show_rgb_rainbow(self, game_name, device_type, zones):
        while True:
            for i in range(0, 50):
                f = i * 5
                self.show_static_color(game_name, device_type, zones, (255-f, f, 0))
            for i in range(0, 50):
                f = i * 5
                self.show_static_color(game_name, device_type, zones, (0, 255-f, f))  # GREEN -> BLUE
            for i in range(0, 50):
                f = i * 5
                self.show_static_color(game_name, device_type, zones, (f, 0, 255-f))  # BLUE -> RED


# ----ALL KIND OF DEVICES----
class MouseRival:
    DEVICE_TYPE = "rgb-2-zone"
    ZONES = ["one", "two"]
