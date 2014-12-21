class DeviceType(object):
    ios = "ios"
    android = "android"
    winrt = "winrt"
    winphone = "winphone"
    dotnet = "dotnet"

    @classmethod
    def get_choices(cls):
        choices = (
            (cls.ios, "iOS"),
            (cls.android, "Android"),
            (cls.winrt, "Windows Runtime"),
            (cls.winphone, "Windows Phone"),
            (cls.dotnet, ".NET"))
        return choices
