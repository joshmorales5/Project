from gui import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Initializes the TV remote control application.
        """
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('TV Remote Control')

        self.tv_on = False
        self.channel_min = 0
        self.volume_min = 0
        self.channel_max = 5
        self.volume_max = 5
        self.mute = False

        self.channel = self.channel_min
        self.volume = self.volume_min

        self.PowerButton.clicked.connect(self.power)
        self.VolumeUpButton.clicked.connect(self.volume_up)
        self.VolumeDownButton.clicked.connect(self.volume_down)
        self.ChannelUpButton.clicked.connect(self.channel_up)
        self.ChannelDownButton.clicked.connect(self.channel_down)
        self.MuteButton.clicked.connect(self.mute_button)

        self.update_ui()

    def power(self) -> None:
        """
        Turns the power of the TV ON/OFF.
        """
        self.tv_on = not self.tv_on
        self.muted = False
        self.update_ui()

    def volume_up(self) -> None:
        """
        Increases the volume of the TV.
        """
        if self.tv_on and not self.muted and self.volume < self.volume_max:
            self.volume += 1
        self.update_ui()

    def volume_down(self) -> None:
        """
        Decreases the volume of the TV.
        """
        if self.tv_on and not self.muted and self.volume > self.volume_min:
            self.volume -= 1
        self.update_ui()

    def channel_up(self) -> None:
        """
        Increases the channel of the TV.
        """
        if self.tv_on:
            self.channel = (self.channel + 1) if self.channel < self.channel_max else self.channel_min
        self.update_ui()

    def channel_down(self) -> None:
        """
        Decreases the channel of the TV.
        """
        if self.tv_on:
            self.channel = (self.channel - 1) if self.channel > self.channel_min else self.channel_max
        self.update_ui()

    def mute_button(self) -> None:
        """
        Mutes or unmutes the TV.
        """
        if self.tv_on:
            self.muted = not self.muted
        self.update_ui()

    def update_ui(self):
        """
        Updates the UI elements based on the current state of the TV.
        """
        if self.tv_on:
            channel_images = {              # Dictionary to map channel numbers to image files
                0: "channel_1.png",
                1: "channel_2.svg",
                2: "channel_3.png",
                3: "channel_4.jpeg",
                4: "channel_5.png"
            }
            current_channel = channel_images.get(self.channel, "channel_1.png") # Default to channel 1
            pixmap = QPixmap(current_channel)                                   # Loads the image for the current channel
            #Youtube helped with this part
            self.ChannelDisplay.setPixmap(pixmap)                           # Set the pixmap for the label
            self.ChannelDisplay.setStyleSheet("background-color: White;")    # Set the background color to white when the TV is on
            self.ChannelDisplay.setScaledContents(True)                       # Scale the pixmap to fit the label

            self.VolumeBar.setMaximum(self.volume_max)                     # Set the maximum value of the volume bar
            self.VolumeBar.setValue(0 if self.muted else self.volume)      # Set the value of the volume bar when muted/unmuted
        else:
            self.ChannelDisplay.clear()                                    # Clear the pixmap when the TV is off
            self.VolumeBar.setValue(0)                                     # Set the volume bar to 0 when the TV is off
            self.VolumeBar.setStyleSheet("background-color: Clear;")       # Set the background color to clear when the TV is off





















