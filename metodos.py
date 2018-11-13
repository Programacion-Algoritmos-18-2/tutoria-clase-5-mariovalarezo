class Persona(object):
    def _init_(self):
        self.nombre = ""
        self.apellido=""
        self.ciudad= Ciudad()

    def agregar_nombre(self, nom):
         self.nombre = nom

    def obtener_nombre(self):
        return self.nombre

    def agregar_apellido(self, ape):
            self.apellido = ape

    def obtener_apellido(self):
            return self.apellido

    def agregarCiudad(self, ci):
        self.ciudad = ci

    def obtenerCiudad(self):
        return self.ciudad

    def presentar_datos(self):
            cadena = "Informancion de\n %s %s \n Ciudad %s \n Poblacion%s " % (self.obtener_nombre(),
                                                               self.obtener_apellido(), self.obtenerCiudad().obtener_nombre(), self.obtenerCiudad().obtener_poblacion())
            return cadena

class Ciudad(object):
    def _init_(self):
        self.nombre=""
        self.poblacion=0

    def agregar_nombre(self, nom):
            self.nombre = nom

    def obtener_nombre(self):
            return self.nombre

    def agregar_poblacion(self, nom):
            self.poblacion = nom

    def obtener_poblacion(self):
            return self.poblacion





class Estudiante(Persona):
    def _init_(self):
        super(Estudiante, self)._init_()
        self.idEstudiante=0

    def agregar_id(self, id):
            self.idEstudiante = id

    def obtener_id(self):
            return self.idEstudiante

    def presentar_datos(self):
        cadena = "%s \n id: %s \n " % (super(Estudiante, self).presentar_datos(), self.obtener_id(), )

        return cadena


class EstPrecencial(Estudiante):
    def _init_(self):
        super(EstPrecencial, self)._init_()
        self.ciclo=0
        self.num_creditos=0

    def agregar_ciclo(self, ci):
            self.ciclo= ci

    def obtener_ciclo(self):
            return  self.ciclo

    def agregar_num_creditos(self, ci):
            self.num_creditos = ci

    def obtener_num_creditos(self):
            return self.num_creditos

    def presentar_datos(self):
            cadena = "%s \n Ciclo: %s \n Numero de creditos: %s" % (super(EstPrecencial, self).presentar_datos(),self.obtener_ciclo(), self.obtener_num_creditos())
            return cadena

class EstDistancia (Estudiante):
    def _init_(self):
        super(EstDistancia, self)._init_()
        self.modulo=0
        self.num_materias=0

    def agregar_modulo(self, ci):
            self.modulo = ci

    def obtener_cmodulo(self):
            return self.modulo

    def agregar_num_materias(self, ci):
            self.num_materias= ci

    def obtener_num_materias(self):
            return self.num_materias

    def presentar_datos(self):
            cadena = "Modulo: %s \n Numero de materias: %s" % (self.obtener_modulo(), self.obtener_num_materias())


            return cadena

