from cpr.Resource import Resource
import cloudpickle

class DataFrameSource(Resource):
    def __init__(self, location: str, name: str, ext: str):
        """
        Parameters
        ----------
        location
            Where the image file is stored
        name
            Name of the image file
        ext
            File extension
        """
        super(DataFrameSource, self).__init__(
            location=location,
            name=name,
            ext=ext,
        )

        def _read_data(self):
            return cloudpickle.load(self.get_path())