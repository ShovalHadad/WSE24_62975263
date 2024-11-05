import requests

class Plane:
    base_url = "http://airline.mssql.somee.com/api/planes" 

    def __init__(self, plane_id, name, year, made_by, picture, 
                 num_of_seats1, num_of_seats2, num_of_seats3):
        self.plane_id = plane_id
        self.name = name
        self.year = year
        self.made_by = made_by
        self.picture = picture
        self.num_of_seats1 = num_of_seats1
        self.num_of_seats2 = num_of_seats2
        self.num_of_seats3 = num_of_seats3

    @classmethod
    def from_dict(cls, data):
        return cls(
            plane_id=data.get("PlaneId"),
            name=data.get("Name"),
            year=data.get("Year"),
            made_by=data.get("MadeBy"),
            picture=data.get("Picture"),
            num_of_seats1=data.get("NumOfSeats1"),
            num_of_seats2=data.get("NumOfSeats2"),
            num_of_seats3=data.get("NumOfSeats3")
        )

    def to_dict(self):
        return {
            "PlaneId": self.plane_id,
            "Name": self.name,
            "Year": self.year,
            "MadeBy": self.made_by,
            "Picture": self.picture,
            "NumOfSeats1": self.num_of_seats1,
            "NumOfSeats2": self.num_of_seats2,
            "NumOfSeats3": self.num_of_seats3
        }

    @staticmethod
    def get_all_planes():
        try:
            response = requests.get(f"{Plane.base_url}")
            response.raise_for_status()
            plane_data_list = response.json()
            return [Plane.from_dict(data) for data in plane_data_list]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching planes: {e}")
            return []

    @staticmethod
    def get_plane_by_id(plane_id):
        try:
            response = requests.get(f"{Plane.base_url}/{plane_id}")
            response.raise_for_status()
            plane_data = response.json()
            return Plane.from_dict(plane_data)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching plane {plane_id}: {e}")
            return None

    def create(self):
        try:
            plane_data = self.to_dict()
            response = requests.post(f"{Plane.base_url}", json=plane_data)
            response.raise_for_status()
            print("Plane created successfully")
        except requests.exceptions.RequestException as e:
            print(f"Error creating plane: {e}")

    def update(self):
        try:
            plane_data = self.to_dict()
            response = requests.put(f"{Plane.base_url}/{self.plane_id}", json=plane_data)
            response.raise_for_status()
            print("Plane updated successfully")
        except requests.exceptions.RequestException as e:
            print(f"Error updating plane {self.plane_id}: {e}")

    def delete(self):
        try:
            response = requests.delete(f"{Plane.base_url}/{self.plane_id}")
            response.raise_for_status()
            print("Plane deleted successfully")
        except requests.exceptions.RequestException as e:
            print(f"Error deleting plane {self.plane_id}: {e}")
