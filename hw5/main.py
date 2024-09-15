from hw5.file_creator import FileCreator
from hw5.record_creator import RecordCreator
from hw5.user_input import UserInput


class Main:
    file_creator = FileCreator()
    file_creator.add_record_to_file(RecordCreator().create_record(UserInput().record_type_input()))








