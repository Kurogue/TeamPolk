def execute_query(connection, query, data=None):
    with connection.cursor() as cursor:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()

def add_exterior(connection, exterior_id, type_, description, color):
    query = """
    INSERT INTO Exterior (Exterior_id, Type, Description, Color)
    VALUES (%s, %s, %s, %s);
    """
    data = (exterior_id, type_, description, color)
    execute_query(connection, query, data)

def lookup_exterior(connection, exterior_id):
    query = "SELECT * FROM Exterior WHERE Exterior_id = %s;"
    data = (exterior_id,)
    with connection.cursor() as cursor:
        cursor.execute(query, data)
        return cursor.fetchone()

def delete_exterior(connection, exterior_id):
    query = "DELETE FROM Exterior WHERE Exterior_id = %s;"
    data = (exterior_id,)
    try:
        execute_query(connection, query, data)
    except:
        print("Error deleting exterior with ID:", exterior_id)
        connection.rollback()
