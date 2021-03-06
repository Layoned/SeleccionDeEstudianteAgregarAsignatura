from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.declarative_base import engine, Base, session

class GestionAsignatura():

    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_asignatura(self, nombreAsignatura):
        if len(nombreAsignatura)==0:
            return False
        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura).all()
        if len(busqueda) == 0:
            asignatura = Asignatura(nombreAsignatura=nombreAsignatura)
            session.add(asignatura)
            session.commit()
            return True
        else:
            return False

    def editar_asignatura(self, idAsignatura, nombreAsignatura):
        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura, id.asignatura != idAsignatura ).all()
        if len(busqueda) == 0:
            asignatura = session.query(Asignatura).filter(id.Asignatura == idAsignatura).first()
            asignatura.nombreAsignatura = nombreAsignatura
            session.commit()
            return True
        else:
            return False

    def eliminar_asignatura(self, idAsignatura):
        try:
            asignatura = session.query(Asignatura).filter(id.Asignatura == idAsignatura).first()
            session.delete(asignatura)
            session.commit()
            return True
        except
            return False
