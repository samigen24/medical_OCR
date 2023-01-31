
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.camera = camera
        self.ram = ram
        self.storage = storage

    def make_call(self):
        pass

    def receive_call(self):
        pass

    def take_a_picture(self):
        pass


class Apple(MobilePhone):
    def __init__(self, product_name, network_type, ram, storage):
        self.product_name = product_name
        super().__init__(network_type=network_type,
                         screen_type='Touch Screen',
                         camera="12MP",
                         dual_sim=False,
                         front_camera='8MP',
                         ram=ram,
                         storage=storage)

    def make_call(self):
        print(f"Making a call from {self.product_name} Apple mobile phone.")

    def receive_call(self):
        print(f"Receiving a call on {self.product_name} Apple mobile phone.")

    def take_a_picture(self):
        return f"Taking picture on {self.product_name} with {self.front_camera} camera"

    def get_info(self):
        return f""" Product Name: {self.product_name}
        Camera: {self.camera}
        Network Type: {self.network_type}
        ...
        """

    def __str__(self):
        return f"Apple({self.product_name}, {self.storage}, ...)"


class Samsung(MobilePhone):
    def __init__(self, product_name, network_type, dual_sim, front_camera, camera, ram, storage):
        self.product_name = product_name
        super().__init__(network_type=network_type,
                         screen_type='Touch Screen',
                         camera=camera,
                         dual_sim=dual_sim,
                         front_camera=front_camera,
                         ram=ram,
                         storage=storage)

    def make_call(self):
        print(f"Making a call from {self.product_name} Samsung mobile phone.")

    def receive_call(self):
        print(f"Receiving a call on {self.product_name} Samsung mobile phone.")

    def take_a_picture(self):
        return f"Taking picture on {self.product_name} with {self.front_camera} camera"

    def get_info(self):
        return f""" Product Name: {self.product_name}
        Camera: {self.camera}
        Network Type: {self.network_type}
        ...
        """

    def __str__(self):
        return f"Samsung({self.product_name}, {self.storage}, ...)"


apple1 = Apple("Iphone6", "4G", "4GB", "64GB")
apple2 = Apple("Iphone8", "5G", "6GB", "128GB")

# Samsung Phones

samsung1 = Samsung("Samsung1", "4G", True, "16MP", "32MP", "4GB", "64GB")
samsung2 = Samsung("Samsung2", "3G", True, "8MP", "16MP", "3GB", "16GB")


print(apple1.get_info())
print(samsung1.get_info())
print(samsung2)
