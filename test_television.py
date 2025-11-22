from television import Television


def test_init_defaults():
	tv = Television()
	assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_power_toggle():
	tv = Television()
	tv.power()
	assert "Power = True" in str(tv)
	tv.power()
	assert "Power = False" in str(tv)
	
def test_mute_toggle():
	tv = Television()
	tv.power()
	tv.volume_up()
	tv.mute()
	assert f"Volume = 0" in str(tv)
	tv.mute()
	assert f"Volume = 1" in str(tv) 
	tv.power()
	tv.mute()
	assert f"Volume = 0" in str(tv)
	tv.mute()
	assert f"Volume = 0" in str(tv) 


def test_channel_wrap_up_down():
	tv = Television()
	tv.power()
	# advance to MAX_CHANNEL
	for _ in range(Television.MAX_CHANNEL):
		tv.channel_up()
	assert f"Channel = {Television.MAX_CHANNEL}" in str(tv)
	# wrap to MIN_CHANNEL
	tv.channel_up()
	assert f"Channel = {Television.MIN_CHANNEL}" in str(tv)
	# wrap down from MIN_CHANNEL to MAX_CHANNEL
	tv.channel_down()
	assert f"Channel = {Television.MAX_CHANNEL}" in str(tv)


def test_volume_bounds_and_unmute():
	tv = Television()
	tv.power()
	# can't go below MIN_VOLUME
	tv.volume_down()
	assert f"Volume = {Television.MIN_VOLUME}" in str(tv)
	# increase up to MAX_VOLUME
	tv.volume_up()
	assert f"Volume = 1" in str(tv)
	tv.volume_up()
	assert f"Volume = {Television.MAX_VOLUME}" in str(tv)
	# further increases have no effect
	tv.volume_up()
	assert f"Volume = {Television.MAX_VOLUME}" in str(tv)


def test_mute_and_volume_buttons_unmute():
	tv = Television()
	tv.power()
	# set volume to 1
	tv.volume_up()
	assert "Volume = 1" in str(tv)
	# mute should affect displayed volume
	tv.mute()
	assert "Volume = 0" in str(tv)
	# pressing a volume button should unmute and adjust stored volume
	tv.volume_up()
	# starting from stored 1, this should unmute and increment to 2
	assert f"Volume = {Television.MAX_VOLUME}" in str(tv)


    
