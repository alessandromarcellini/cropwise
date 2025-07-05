from models.routes.log import LogEntry

class LogController:
    def __init__(self):
        pass

    def get_logs(self, filter = None): #TODO add a filter using the strategy pattern
        entries = [] # TODO retrieve them from the database using its controller
        if filter:
            entries = filter.filter(entries)
        return entries
    
    def add_log(self, entry: LogEntry):
        pass

    def get_actions_anomalies(self):
        pass

    def get_metrics_anomalies(self):
        pass
