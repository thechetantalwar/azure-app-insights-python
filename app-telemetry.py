import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)

# TODO: replace the all-zero GUID with your instrumentation key.
logger.addHandler(AzureLogHandler(connection_string='AI'))
def valuePrompt():
    line = input("Enter a value: ")
    logger.warning(line)

def main():
    
    while True:
        valuePrompt()
    

if __name__ == "__main__":
    main()

