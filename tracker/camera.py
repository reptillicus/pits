from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)

def take_video():
    """
    This will take 30 second videos every 2 minutes
    :return: None
    """
    i = 0
    camera = PiCamera()
    camera.resolution = (640, 480)
    while True:
        # Should change the location to save to probably
        filename = "/tmp/video.{i}".format(i=i)
        camera.start_recording(filename, splitter_port=2, resize=(640,480))
        camera.wait_recording(30)
        camera.stop_recording()
        i += 1
        sleep(120)


if __name__ == "__main__":
    take_video()
