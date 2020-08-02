class Location:
    def getXLoc(self, centreX):
        return 'on Left Side' if centreX < 0.33 else 'on Centre' if centreX < 0.66 else 'on  Right Side'

    # def getYLoc(self, centreY):
    #     return 'Top' if centreY < 0.33 else 'Centre' if centreY < 0.66 else 'Bottom'

