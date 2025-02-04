#----------------------------PAQUETES------------------------------------------------------------------

from lxml import etree
import xmltodict
import json


xml_data = r"C:\Users\alfon\OneDrive\Escritorio\Practica1_BDNR\viaje.xml"
xsd_data = r"C:\Users\alfon\OneDrive\Escritorio\Practica1_BDNR\viaje.xsd"


#----------------------------VALIDADOR------------------------------------------------------------------

class Validador:
    def __init__(self, xsd_path: str):
        try:
            xmlschema_doc = etree.parse(xsd_path)
            self.xmlschema = etree.XMLSchema(xmlschema_doc)
            print(f"Esquema XSD '{xsd_path}' cargado correctamente.")
        except (etree.XMLSchemaParseError, etree.XMLSyntaxError) as exception:
            print(f"Error al cargar el esquema XSD: {exception}")
        except FileNotFoundError:
            print(f"Archivo XSD no encontrado: {xsd_path}")
        except Exception as exception:
            print(f"Ocurrió un error inesperado: {exception}")

    def validate(self, xml_path: str) -> bool:
        try:
            xml_doc = etree.parse(xml_path)
            result = self.xmlschema.validate(xml_doc)
            if not result:
                log = self.xmlschema.error_log
                print("Errores de validación encontrados:")
                for error in log:
                    print(error)
            else:
                print(f"El archivo XML '{xml_path}' es válido según el esquema XSD.")
            return result
        except (etree.XMLSyntaxError, etree.DocumentInvalid) as exception:
            print(f"Error al validar el XML: {exception}")
        except FileNotFoundError:
            print(f"Archivo XML no encontrado: {xml_path}")
        except Exception as exception:
            print(f"Ocurrió un error inesperado: {exception}")
        return False
    
Validador = Validador(xsd_data)
Validador.validate(xml_data)



#------------------------------CARGA DE XML A UN OBJETO PYTHON----------------------------------------------

with open(xml_data) as archivo_xml:
    content = archivo_xml.read()
    diccionario_xml = xmltodict.parse(content)

#------------------------------CARGA DE UN NUEVO VIAJERO AL DICCIONARIO XML--------------------------------- 

nuevo_viajero_alfonso = {
    "nombre":"Alfonso Jimena Ruiz",
    "edad":"20",
    "DNI":"05977025S",
    "Pasaporte":"123456789",
    "Genero":"Masculino"
}
validacion_json = {"$schema":r"C:\Users\alfon\OneDrive\Escritorio\Practica1_BDNR\viaje.schema.json"}

diccionario_xml['viaje']['Viajeros']['viajero'].append(nuevo_viajero_alfonso)


print(diccionario_xml)

#-----------------------------GUARDAR DATOS EN UN ARCHIVO TIPO JSON-------------------------------------------

diccionario_xml['viaje'].update(validacion_json)
print(diccionario_xml)

json_file_path = r"C:\Users\alfon\OneDrive\Escritorio\Practica1_BDNR\viaje.json"

with open(json_file_path, 'w', encoding="UTF-8") as datos_json:
    json.dump(diccionario_xml,datos_json, ensure_ascii=False, indent=4)
    print("Los datos se guardaron en: {json_file_path}")

