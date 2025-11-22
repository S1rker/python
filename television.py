class Television():
    """
    This class simulates a basic television with power, mute, channel,
    and volume control. Volume is stored independently of the muted
    display state (muting reports Volume = 0 when powered on). Channel
    wraps between `MIN_CHANNEL` and `MAX_CHANNEL`.

    Constants:
    - MIN_VOLUME, MAX_VOLUME: allowed stored volume range (ints).
    - MIN_CHANNEL, MAX_CHANNEL: allowed channel indices (ints).

    Attributes (private):
    - __status: bool -- True when the TV is powered on.
    - __muted: bool -- True when the TV is muted (affects displayed volume).
    - __volume: int -- Stored volume level (not shown when muted).
    - __channel: int -- Current channel index.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3


    def __init__(self) -> None:
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL


    def power(self) -> None:
        """Toggle the TV power state.

        Turns the TV on if it was off, and off if it was on.
        """
        # Simple boolean toggle
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle mute when the TV is powered on.

        Muting only affects the displayed volume; the stored volume
        remains unchanged. If the TV is off, mute does nothing.
        """
        # Only allow mute toggle when TV is powered on
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Advance the channel by one, till MAX_CHANNEL.

        Has effect only when the TV is powered on.
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Go to the previous channel, till MIN_CHANNEL.

        Has effect only when the TV is powered on.
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Increase volume by one step up to MAX_VOLUME.

        Pressing a volume button while muted will unmute the TV and
        then adjust the stored volume. No effect when the TV is off.
        """
        if self.__status:
            # Changing the volume should unmute the TV
            if self.__muted:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease volume by one step down to MIN_VOLUME.

        Pressing a volume button while muted will unmute the TV and
        then adjust the stored volume. No effect when the TV is off.
        """
        if self.__status:
            # Changing the volume should unmute the TV
            if self.__muted:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1


    def __str__(self) -> str:
        # When muted (and powered on) report volume as 0 for display only
        display_volume = 0
        if self.__status:
            if  self.__muted:
                return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}'
            else:
                return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        
    