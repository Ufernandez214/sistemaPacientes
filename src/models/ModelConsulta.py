from .entities.Consulta import Consulta


class ModelConsulta():

    def getPacientesPorConsulta(db, consulta):
        try:
            cursor = db.connection.cursor()   
            sql = """SELECT cantidad_pacientes_atender FROM consulta WHERE id = {}""".format(consulta)
            cursor.execute(sql)
            row = cursor.fetchone()
            return row[0]
        except Exception as ex:
            raise Exception(ex)  

    def getConsultas(db):
        try:
            cursor = db.connection.cursor()   
            sql = """SELECT c.id, h.nombre AS hospital, c.nombre as consulta, e.nombre, c.cantidad_pacientes_atender, es.descripcion
                        FROM consulta c
                        INNER JOIN especialistas e  ON e.id_consulta = c.id
                        INNER JOIN estados es ON es.id = c.estado
                        INNER JOIN hospital h ON h.id = c.id_hospital"""
            cursor.execute(sql)
            row = cursor.fetchall()
            return row
        except Exception as ex:
            raise Exception(ex)

    def updateEstadoConsulta(db, consulta, estado):
        try:
            cursor = db.connection.cursor()   
            sql = f"""UPDATE consulta
                        SET estado = {estado}
                        WHERE id = {consulta} """
            estado = cursor.execute(sql)
            return estado

        except Exception as ex:
            raise Exception(ex) 

    def getEstadoConsulta(db, consulta):
        try:
            cursor = db.connection.cursor()   
            sql = f"""SELECT e.descripcion FROM consulta c
                        INNER JOIN estados e ON e.id = c.estado
                        WHERE c.id  = {consulta}"""
            cursor.execute(sql)
            row = cursor.fetchone()
            return row
        except Exception as ex:
            raise Exception(ex)

    def updatePacienteAtendido(db, consulta):
        try:
            cursor = db.connection.cursor()   
            sql = f"""UPDATE pacientes
                        SET id_estado_atencion = 5
                        WHERE id_consulta = {consulta} AND id_estado_atencion = 2"""
            estado = cursor.execute(sql)
            return estado
        except Exception as ex:
            raise Exception(ex) 