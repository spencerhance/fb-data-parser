from lxml import etree
from datetime import datetime
import json


class Parser:
    def __init__(self):
        self.threads = []

    def parse_threads(self, filenames):
        for filename in filenames:
            thread = Thread()
            thread.parse_thread(filename)
            self.threads.append(thread)

    def export(self, file_type='json', filename=None):
        if file_type == 'json':
            thread_dict = {"threads": [thread.to_dict() for thread in self.threads]}
            result = json.dumps(thread_dict)
        
        # Save to a file if a filename is provided
        if filename is not None:
            with open(filename, 'w') as f:
                f.write(result)

        # Default is to print to stdout
        else:
            print(result)


class Thread:
    def __init__(self, title=None, participants=None, messages=None):
        self.title = title
        self.participants = participants
        self.in_conversation = True
        
        if not messages:
            self.messages = []

    def parse_thread(self, filename):
        # Setup tree
        tree = etree.parse(filename)
        root = tree.getroot()

        # Search for thread and title
        thread_node = root.find(".//div[@class='thread']")
        self.title = root.find(".//title").text

        # Get the list of participants
        # Kinda hacky since the text is hidden inside the div
        for text in thread_node.itertext():
            if "Participants" in text:
                self.participants = text.split(": ")[1:]
                break

        # Figure out if we are still in the conversation
        # TODO check if there are other warnings that could be here
        warning = thread_node.find(".//span[@class='warning']")
        if warning is not None and warning.text == 'You are no longer in this conversation.':
            self.in_conversation = False

        # Get messages
        for elem in thread_node.findall(".//div[@class='message']"):
            message = Message()
            message.parse_message(elem)

            # Only add messages that contain text
            if message.body:
                self.messages.append(message)

    def to_dict(self):
        return {"title": self.title, "participants": self.participants,
                "in_conversation": self.in_conversation, "messages":
                [message.to_dict() for message in self.messages]}

 
class Message:
    def __init__(self, user=None, body=None, timestamp=None, time_string=None):
        self.user = user
        self.body = body
        self.timestamp = timestamp
        self.time_string = time_string

    def parse_message(self, message_node):
        self.user = message_node.find(".//span[@class='user']").text
        self.time_string = message_node.find(".//span[@class='meta']").text

        # Convert time to datetime object
        #self.timestamp = datetime.strptime(self.time_string, "%A, %B %d, %Y at %I:%M%p %Z")
        
        # Text is in <p> tag following message, so we grab the "next" node
        self.body = message_node.getnext().text

    def to_dict(self):
        return {"user": self.user, "body": self.body, "time_string":
                self.time_string}
