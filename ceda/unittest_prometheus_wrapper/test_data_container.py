class TestDataContainer:
    '''Container to store data for each test case being passed to create Prometheus endpoints
    '''
    
    def __init__(self, test_class, test_names=None, service_name=None):
        self.test_class = test_class

        if test_names = None:
            self.test_names = []
        else:
            self.test_names = test_names

        if service_name is None:
            self.service_name = '{}_status'.format(test_class.__name__)
        else:
            self.service_name = service_name
