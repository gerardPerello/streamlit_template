from repositories import TutorialRepository

class TutorialService:
    @staticmethod
    def get_all_tutorials():
        # This method can include additional logic, such as filtering, sorting, etc.
        try:
            message = TutorialRepository.get_all()
            return message
        except:
          return "Error!"
    
    @staticmethod
    def get_tutorial_by_name(name):
        # This method can include additional logic, such as filtering, sorting, etc.
        try:
            message = TutorialRepository.get_by_name(name)
            return message
        except:
          return "Error!"
    
    @staticmethod
    def push_tutorials(data_list):
        # This method can include additional logic, such as filtering, sorting, etc.
        try:
            message = TutorialRepository.create(data_list)
            return message
        except:
          return "Error!"
        
    @staticmethod
    def delete_tutorial_by_id(id):
        # This method can include additional logic, such as filtering, sorting, etc.
        try:
            message = TutorialRepository.delete_by_id(id)
            return message
        except:
          return "Error!"