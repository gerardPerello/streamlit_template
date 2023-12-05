from services import connect_snowflake
from models import Tutorial


class TutorialRepository:

    @staticmethod
    def get_all():
        connection = connect_snowflake()
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT * FROM TUTORIALS")
            results = cursor.fetchall()
            return [Tutorial(*result) for result in results]
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_name(name):
        connection = connect_snowflake()
        cursor = connection.cursor()

        try:
            query = "".join(("SELECT * FROM TUTORIALS WHERE NAME ILIKE '%" , name , "%'"))
            cursor.execute(query)
            results = cursor.fetchall()
            return [Tutorial(*result) for result in results]
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete_by_id(id):
        connection = connect_snowflake()
        cursor = connection.cursor()

        try:
            query = (f"DELETE FROM TUTORIALS WHERE ID = {id}")
            cursor.execute(query)
            results = cursor.fetchone()
            return f"Tutorial {id} has been deleted succesfully"
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            connection.close()


    @staticmethod
    def create(data_list):
        required_fields = ['name','date','author','content']
        
        for data in data_list:
            if not all(field in data for field in required_fields):
                return {'error': 'Required currency data is missing'}

        connection = connect_snowflake()
        cursor = connection.cursor()

        try:
            query = "INSERT INTO TUTORIALS (name, creation_date, author, content) VALUES %s" % ', '.join(
                ['(%s, %s, %s, %s)'] * len(data_list))
            params = []
            for data in data_list:
                params.extend([data['name'], data['date'], data['author'], data['content']])

            cursor.execute(query, params)
            connection.commit()

            return {'message': 'Currencies created successfully'}
        except Exception as e:
            print("error")
            return {'error': str(e)}
        finally:
            cursor.close()
            connection.close()

    