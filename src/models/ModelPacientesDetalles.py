from .entities.PacientesDetalles import PacientesDetalles


class ModelPacientesDetalles():

    def save(db, paciente_detalles):
        try:
            cursor = db.connection.cursor()
            sql = f""" INSERT INTO pacientes_detalles (es_fumador, tiempo_fumador, tiene_dieta, peso, estatura, id_paciente) 
                       VALUES({paciente_detalles.es_fumador},{paciente_detalles.tiempo_fumador}, {paciente_detalles.tiene_dieta}, {paciente_detalles.peso}, {paciente_detalles.estatura},{paciente_detalles.id_paciente})"""
            cursor.execute(sql)
            record_last = cursor.lastrowid
            return record_last
            cursor.close()
            
        except Exception as ex:
            raise Exception(ex)