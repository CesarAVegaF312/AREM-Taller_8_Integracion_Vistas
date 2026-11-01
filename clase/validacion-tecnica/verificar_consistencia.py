"""Verifica la consistencia de un modelo integrado en formato ArchiMate Model Exchange.

Uso:  python verificar_consistencia.py modelo.xml

Aplica de forma automática el Paso 5 de la guía (revisar consistencia) y agrega
las revisiones que se vuelven difíciles a mano cuando el tablero crece.
Solo usa la biblioteca estándar de Python: no hay que instalar nada.
"""
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

NS = "{http://www.opengroup.org/xsd/archimate/3.0/}"
XSI_TYPE = "{http://www.w3.org/2001/XMLSchema-instance}type"
XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"

# Capas del tablero del Taller 8, de arriba hacia abajo, y los tipos de ArchiMate de cada una.
CAPAS = [
    ("Negocio", {"BusinessActor", "BusinessRole", "BusinessCollaboration", "BusinessInterface",
                 "BusinessProcess", "BusinessFunction", "BusinessInteraction", "BusinessEvent",
                 "BusinessService", "Contract", "Representation", "Product"}),
    ("Aplicaciones", {"ApplicationComponent", "ApplicationCollaboration", "ApplicationInterface",
                      "ApplicationFunction", "ApplicationInteraction", "ApplicationProcess",
                      "ApplicationEvent", "ApplicationService"}),
    ("Información", {"DataObject", "BusinessObject"}),
    ("Infraestructura", {"Node", "Device", "SystemSoftware", "TechnologyCollaboration",
                         "TechnologyInterface", "Path", "CommunicationNetwork", "TechnologyFunction",
                         "TechnologyProcess", "TechnologyInteraction", "TechnologyEvent",
                         "TechnologyService", "Artifact", "Equipment", "Facility",
                         "DistributionNetwork", "Material"}),
    ("Seguridad", {"Requirement", "Constraint"}),
]
OTROS_TIPOS = {"Stakeholder", "Driver", "Assessment", "Goal", "Outcome", "Principle", "Meaning",
               "Value", "Resource", "Capability", "CourseOfAction", "ValueStream", "WorkPackage",
               "Deliverable", "ImplementationEvent", "Plateau", "Gap", "Grouping", "Location",
               "AndJunction", "OrJunction"}
TIPOS_RELACION = {"Composition", "Aggregation", "Assignment", "Realization", "Serving", "Access",
                  "Influence", "Triggering", "Flow", "Specialization", "Association"}
TIPOS_ELEMENTO = set().union(*(tipos for _, tipos in CAPAS), OTROS_TIPOS)


def nombre(nodo):
    for n in nodo.findall(NS + "name"):
        if n.get(XML_LANG, "es") == "es":
            return (n.text or "").strip()
    n = nodo.find(NS + "name")
    return (n.text or "").strip() if n is not None else "(sin nombre)"


def normalizar(texto):
    sin_tildes = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", sin_tildes.lower())


def capa_de(tipo):
    for i, (_, tipos) in enumerate(CAPAS):
        if tipo in tipos:
            return i
    return None


def main(ruta):
    raiz = ET.parse(ruta).getroot()
    elementos = {e.get("identifier"): (e.get(XSI_TYPE), nombre(e))
                 for e in raiz.iter(NS + "element")}
    relaciones = [(r.get("identifier"), r.get(XSI_TYPE), r.get("source"), r.get("target"))
                  for r in raiz.iter(NS + "relationship")]
    en_vistas = {n.get("elementRef") for n in raiz.iter(NS + "node") if n.get("elementRef")}

    print(f"Modelo: {nombre(raiz)}")
    print(f"{len(elementos)} elementos, {len(relaciones)} relaciones\n")

    # 1. Estructura: tipos válidos y referencias a elementos que existen.
    errores = []
    for ident, (tipo, nom) in elementos.items():
        if tipo not in TIPOS_ELEMENTO:
            errores.append(f"El elemento '{nom}' tiene un tipo que no existe en ArchiMate: {tipo}")
    for ident, tipo, origen, destino in relaciones:
        if tipo not in TIPOS_RELACION:
            errores.append(f"La relación {ident} tiene un tipo que no existe en ArchiMate: {tipo}")
        for extremo in (origen, destino):
            if extremo not in elementos:
                errores.append(f"La relación {ident} apunta a un elemento que no existe: {extremo}")
    print("1. Estructura del archivo")
    print("   " + ("\n   ".join(errores) if errores else "Sin errores."))

    # 2. Elementos sin ninguna relación.
    conectados = {extremo for _, _, o, d in relaciones for extremo in (o, d)}
    aislados = [nom for ident, (_, nom) in elementos.items() if ident not in conectados]
    print("\n2. Elementos sin ninguna relación (huérfanos)")
    print("   " + (", ".join(aislados) if aislados else "Ninguno."))

    # 3. Conexión hacia la capa de arriba y hacia la de abajo (tabla del Paso 5).
    #    Igual que en la guía, una conexión con un elemento de la misma capa cuenta si ese
    #    elemento sí está conectado (la Base de Datos llega a las aplicaciones a través de la Nube).
    #    La conexión hacia abajo se exige a Negocio, Aplicaciones e Información; Infraestructura
    #    y Seguridad cierran el hilo.
    vecinos = {ident: set() for ident in elementos}
    for _, _, origen, destino in relaciones:
        if origen in vecinos and destino in vecinos:
            vecinos[origen].add(destino)
            vecinos[destino].add(origen)
    capa = {ident: capa_de(tipo) for ident, (tipo, _) in elementos.items()}

    def alcanza(hacia_arriba):
        marcados = set()
        cambio = True
        while cambio:
            cambio = False
            for ident, c in capa.items():
                if c is None or ident in marcados:
                    continue
                for v in vecinos[ident]:
                    cv = capa[v]
                    if cv is None:
                        continue
                    if (cv < c if hacia_arriba else cv > c) or (cv == c and v in marcados):
                        marcados.add(ident)
                        cambio = True
                        break
        return marcados

    con_arriba, con_abajo = alcanza(True), alcanza(False)
    print("\n3. Conexión entre capas (solo elementos con al menos una relación)")
    print(f"   {'Elemento':32} {'Capa':16} {'Arriba':8} Abajo")
    incompletos = 0
    for ident, (tipo, nom) in elementos.items():
        c = capa[ident]
        if c is None or ident not in conectados:
            continue
        arriba = "-" if c == 0 else ("sí" if ident in con_arriba else "NO")
        abajo = "-" if c >= 3 else ("sí" if ident in con_abajo else "NO")
        incompletos += "NO" in (arriba, abajo)
        print(f"   {nom:32} {CAPAS[c][0]:16} {arriba:8} {abajo}")

    # 4. Elementos que no aparecen en ninguna vista.
    fuera = [nom for ident, (_, nom) in elementos.items() if ident not in en_vistas]
    print("\n4. Elementos que no aparecen en ninguna vista")
    print("   " + (", ".join(fuera) if fuera else "Ninguno."))

    # 5. Posibles duplicados: nombres iguales al quitar mayúsculas, tildes, espacios y guiones.
    grupos = {}
    for ident, (tipo, nom) in elementos.items():
        grupos.setdefault((normalizar(nom), capa_de(tipo)), []).append(nom)
    duplicados = [g for g in grupos.values() if len(g) > 1]
    print("\n5. Posibles duplicados (el mismo elemento con dos nombres)")
    print("   " + ("\n   ".join(" / ".join(g) for g in duplicados) if duplicados else "Ninguno."))

    print("\nResumen: "
          f"{len(errores)} errores de estructura, {len(aislados)} huérfanos, "
          f"{incompletos} elementos sin conexión arriba o abajo, "
          f"{len(fuera)} fuera de las vistas, {len(duplicados)} posibles duplicados.")
    return 1 if errores else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Uso: python verificar_consistencia.py modelo.xml")
    sys.exit(main(sys.argv[1]))
