import sounddevice as sd

# 利用可能なデバイスの情報を取得
devices = sd.query_devices()
print(devices)
