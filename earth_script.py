

def test01_launch(self):
    time.sleep(self.sleep_long_load)
    launch = self.wait.until(ec.visibility_of(find_element.FindElementByName('ArcGIS Earth')))
    print("Success: App launched")

def test02_connect_to_portal(self):