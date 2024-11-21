#Hudson Stovall
#CS 417
#Exam 2
#Question 3

class Widget:
    def __init__(self):
        self.wheels = []
        self.container = None
        self.body = None

    def attachWheel(self, wheel):
        self.wheels.append(wheel)

    def setContainerVolume(self, volume):
        self.container = volume

    def setBody(self, bodytype):
        self.body = bodytype

    def __str__(self):
        wheels = f"{len(self.wheels)} wheels" if self.wheels else "No wheels"
        container = f"Container has {self.container} gallons" if self.container else "No container"
        body = f"Body: {self.body}" if self.body else "No body"
        return f"Widget with {wheels}, {container}, and {body}."


class Builder:
    def getWheel(self): pass
    def getContainer(self): pass
    def getBody(self): pass
    def getWheelCount(self): pass

    def buildWidget(self):
        widget = Widget()
        for _ in range(self.getWheelCount()):
            widget.attachWheel(self.getWheel())
        widget.setContainerVolume(self.getContainer())
        widget.setBody(self.getBody())
        return widget


class CarBuilder(Builder):
    def getWheel(self): return Wheel(size=15)
    def getContainer(self): return None
    def getBody(self): return "car body"
    def getWheelCount(self): return 4


class BucketBuilder(Builder):
    def getWheel(self): return None
    def getContainer(self): return 5
    def getBody(self): return "bucket"
    def getWheelCount(self): return 0


class Wheel:
    def __init__(self, size): self.size = size
    def __str__(self): return f"Wheel size is {self.size}"


class FactoryMethod:
    def createWidget(builder):
        return builder.buildWidget()
