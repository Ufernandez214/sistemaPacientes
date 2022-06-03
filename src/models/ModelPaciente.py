from .entities.Paciente import Pacientes


class ModelPacientes():

    def save(db, paciente):
        try:
            cursor = db.connection.cursor()
            sql = f""" INSERT INTO pacientes (nombres, apellidos, edad, email, telefono, tipo_paciente, id_consulta, id_historia_clinica, id_hospital) 
                       VALUES('{paciente.nombres}','{paciente.apellidos}', {paciente.edad}, '{paciente.email}', '{paciente.telefono}', {paciente.tipo_paciente}, {paciente.id_consulta}, {paciente.id_historia_clinica}, {paciente.id_hospital})"""
            cursor.execute(sql)
            record_last = cursor.lastrowid
            return record_last

        except Exception as ex:
            raise Exception(ex)


    def getPacientes(db):
        try:
            cursor = db.connection.cursor()   
            sql2 = """SELECT p.ID, p.nombres, p.apellidos, p.email, p.telefono, p.id_historia_clinica
                        FROM pacientes p
                        INNER JOIN pacientes_detalles pd ON pd.id_paciente = p.id
                        INNER JOIN consulta c ON c.id = p.id_consulta
                        INNER JOIN especialistas e ON e.id_consulta = c.id""" 
           
            cursor.execute(sql2)
            row = cursor.fetchall()
            if row != None:
                return row
                #return User(row[0], row[1], None, row[2])
            else:
                return None
            #return row
        except Exception as ex:
            raise Exception(ex)    

    def getPacientesUrgencia(db):
        try:
            cursor = db.connection.cursor()   
            sql2 = """SELECT 
                        p.id,
                        CONCAT(p.nombres, " ", p.apellidos) AS nombre, 
                        p.edad, 
                        'Urgencia' AS nombre_consulta, 
                        'Jose Pino' AS nombre_especialista, 
                        pd.peso, 
                        pd.estatura,
                        CASE WHEN (p.edad BETWEEN 1 AND 5) THEN TRUNCATE(p.edad* (pd.peso/pd.estatura * pd.estatura + 3)/100, 0) 
                            ELSE CASE WHEN (p.edad BETWEEN 6 AND 12) THEN TRUNCATE(p.edad*(pd.peso/pd.estatura * pd.estatura + 2)/100, 0)
                                ELSE CASE WHEN (p.edad BETWEEN 13 AND 15) THEN TRUNCATE(p.edad*(pd.peso/pd.estatura * pd.estatura + 1)/100, 0)
                                    ELSE CASE WHEN (p.tipo_paciente = 3 AND pd.tiene_dieta = 1 AND p.edad BETWEEN 60 AND 100 ) THEN TRUNCATE(p.edad *(p.edad/20 + 4)/100 +5.3 ,4)
                                        ELSE CASE WHEN   (p.tipo_paciente = 3 AND pd.tiene_dieta = 0 AND p.edad < 60) THEN TRUNCATE(p.edad *(p.edad/20 + 4)/100 +5.3 ,4)
                                            ELSE CASE WHEN (p.tipo_paciente = 2 AND pd.es_fumador = 1) THEN TRUNCATE(p.edad *(pd.tiempo_fumador/4 + 2)/100,0)
                                                ELSE p.edad * (2)/100  END END END END END END AS URGENCIA,

                        sp.descripcion,
                        sp.id,
                        p.id_estado_atencion

                        FROM pacientes p
                        INNER JOIN consulta c ON c.id = p.id_consulta
                        INNER JOIN especialistas e ON e.id_consulta = c.id
                        INNER JOIN pacientes_detalles pd ON pd.id_paciente = p.ID
                        INNER JOIN estados s ON s.id = c.estado
                        INNER JOIN estados sp ON sp.id = p.id_estado_atencion
                        WHERE p.id_estado_atencion NOT IN (5,2) AND
                        (CASE WHEN (p.edad BETWEEN 1 AND 5) THEN TRUNCATE(p.edad* (pd.peso/pd.estatura * pd.estatura + 3)/100, 0) 
                            ELSE CASE WHEN (p.edad BETWEEN 6 AND 12) THEN TRUNCATE(p.edad*(pd.peso/pd.estatura * pd.estatura + 2)/100, 0)
                                ELSE CASE WHEN (p.edad BETWEEN 13 AND 15) THEN TRUNCATE(p.edad*(pd.peso/pd.estatura * pd.estatura + 1)/100, 0)
                                    ELSE CASE WHEN (p.tipo_paciente = 3 AND pd.tiene_dieta = 1 AND p.edad BETWEEN 60 AND 100 ) THEN TRUNCATE(p.edad *(p.edad/20 + 4)/100 +5.3 ,4)
                                            ELSE CASE WHEN   (p.tipo_paciente = 3 AND pd.tiene_dieta = 0 AND p.edad < 60) THEN TRUNCATE(p.edad *(p.edad/20 + 4)/100 +5.3 ,4)
                                                ELSE CASE WHEN (p.tipo_paciente = 2 AND pd.es_fumador = 1) THEN TRUNCATE(p.edad *(pd.tiempo_fumador/4 + 2)/100,0)
                                                    ELSE p.edad * (2)/100  END END END END END END) > 4
                        ORDER BY URGENCIA DESC""" 
           
            cursor.execute(sql2)
            row = cursor.fetchall()
            if row != None:
                return row
                #return User(row[0], row[1], None, row[2])
            else:
                return None
            #return row
        except Exception as ex:
            raise Exception(ex)

    def getPacientesNinos(db):
        try:
            cursor = db.connection.cursor()   
            sql2 = """SELECT 
                        p.id,
                        CONCAT(p.nombres, " ", p.apellidos) AS nombre, 
                        p.edad, 
                        c.nombre AS nombre_consulta, 
                        e.nombre AS nombre_especialista, 
                        pd.peso, 
                        pd.estatura,
                        CASE WHEN (p.edad BETWEEN 1 AND 5) THEN TRUNCATE(p.edad* (pd.peso/pd.estatura * pd.estatura + 3)/100, 0) 
                            ELSE CASE WHEN (p.edad BETWEEN 6 AND 12) THEN TRUNCATE(p.edad*(pd.peso/pd.estatura * pd.estatura + 2)/100, 0) 
                                ELSE CASE WHEN (p.edad BETWEEN 13 AND 15) THEN TRUNCATE(p.edad*(pd.peso/pd.estatura * pd.estatura + 1)/100, 0) END END END  AS URGENCIA,
                        sp.descripcion,
                        sp.id,
                        p.tipo_paciente

                        FROM pacientes p
                        INNER JOIN consulta c ON c.id = p.id_consulta
                        INNER JOIN especialistas e ON e.id_consulta = c.id
                        INNER JOIN pacientes_detalles pd ON pd.id_paciente = p.ID
                        INNER JOIN estados s ON s.id = c.estado
                        INNER JOIN estados sp ON sp.id = p.id_estado_atencion
                        WHERE p.tipo_paciente = 1 AND p.id_estado_atencion <> 5
                        ORDER BY URGENCIA DESC""" 
           
            cursor.execute(sql2)
            row = cursor.fetchall()
            if row != None:
                return row
                #return User(row[0], row[1], None, row[2])
            else:
                return None
            #return row
        except Exception as ex:
            raise Exception(ex)      

    def getPacientesCGI(db):
            try:
                cursor = db.connection.cursor()   
                sql2 = """SELECT 
                            p.id,
                            CONCAT(p.nombres, " ", p.apellidos) AS nombre, 
                            p.edad, 
                            c.nombre AS nombre_consulta, 
                            e.nombre AS nombre_especialista, 
                            pd.peso, 
                            pd.estatura,
                            
                            CASE WHEN (p.tipo_paciente = 3 AND pd.tiene_dieta = 1 AND p.edad BETWEEN 60 AND 100 ) THEN TRUNCATE(p.edad *(p.edad/20 + 4)/100 +5.3 ,4)
                                    ELSE CASE WHEN   (p.tipo_paciente = 3 AND pd.tiene_dieta = 0 AND p.edad < 60) THEN TRUNCATE(p.edad *(p.edad/20 + 4)/100 +5.3 ,4)
                                        ELSE CASE WHEN (p.tipo_paciente = 2 AND pd.es_fumador = 1) THEN TRUNCATE(p.edad *(pd.tiempo_fumador/4 + 2)/100,0)
                                            ELSE p.edad * (2)/100 END END END AS URGENCIA,
                            
                            sp.descripcion,
                            sp.id

                            FROM pacientes p
                            INNER JOIN consulta c ON c.id = p.id_consulta
                            INNER JOIN especialistas e ON e.id_consulta = c.id
                            INNER JOIN pacientes_detalles pd ON pd.id_paciente = p.ID
                            INNER JOIN estados s ON s.id = c.estado
                            INNER JOIN estados sp ON sp.id = p.id_estado_atencion
                            WHERE p.id_estado_atencion NOT IN (5) AND p.tipo_paciente NOT IN (3)
                            ORDER BY URGENCIA DESC""" 
                cursor.execute(sql2)
                row = cursor.fetchall()
                if row != None:
                    return row
                    #return User(row[0], row[1], None, row[2])
                else:
                    return None
                #return row
            except Exception as ex:
                raise Exception(ex)      

    def updateEstadoPaciente(db, paciente, estado):
        try:
            cursor = db.connection.cursor()   
            sql = f"""UPDATE pacientes 
                        SET id_estado_atencion = {estado}
                        WHERE id ={paciente} """
            estado = cursor.execute(sql)
            if(estado):
                return estado
            else:
                return None
        except Exception as ex:
            raise Exception(ex)   

    def updateTipoPaciente(db, paciente, tipo):
        try:
            cursor = db.connection.cursor()   
            sql = f"""UPDATE pacientes 
                        SET tipo_paciente = {tipo} 
                        WHERE id ={paciente} """
            estado = cursor.execute(sql)
            if(estado):
                return estado
            else:
                return None
        except Exception as ex:
            raise Exception(ex)          
