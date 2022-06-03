class Pacientes():

    def __init__(self, id, nombres, apellidos, edad, email, telefono, tipo_paciente, id_consulta, id_historia_clinica, id_hospital = 1) -> None:
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.email = email
        self.telefono = telefono
        self.tipo_paciente = tipo_paciente
        self.id_consulta = id_consulta
        self.id_historia_clinica = id_historia_clinica
        self.id_hospital = id_hospital
