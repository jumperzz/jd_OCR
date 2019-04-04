__all__ = ['driver']
class driver:
    def drivers(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'bd1e01d'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = '.ui.LauncherUI'
        #desired_caps['appActivity'] = '.plugin.subapp.ui.friend.FMessageConversationUI'
        desired_caps["noReset"] =  'true'
        self.desired_caps = desired_caps
        return self.desired_caps
