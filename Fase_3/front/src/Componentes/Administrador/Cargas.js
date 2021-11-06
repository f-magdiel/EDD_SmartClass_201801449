import React,{useState} from "react";
import CargaEstudiante from "./CargaEstudiante";
import CargaCursos from "./CargaCursos";
import CargaApuntes from "./CargaApuntes";

function Cargas(){
    const [carga_estudiante,setCarga_Estudiante] = useState(false);
    const [carga_cursos,setCarga_Cursos] = useState(false);
    const [carga_apuntes,setCarga_Apuntes] = useState(false);

    function actEstudiantes(){
        setCarga_Estudiante(true);
        setCarga_Cursos(false);
        setCarga_Apuntes(false);
    }

    function actCursos(){
        setCarga_Estudiante(false);
        setCarga_Cursos(true);
        setCarga_Apuntes(false);
    }

    function actApuntes(){
        setCarga_Estudiante(false);
        setCarga_Cursos(false);
        setCarga_Apuntes(true);
    }

    return(
         
        <div>
            <div className="row">
            <div className="col-sm-3">
            <button 
                className="btn btn-outline-light btn-sm px-3" 
                type="submit"  
                onClick={actEstudiantes}
                >Carga de Estudiantes
            </button>
            </div> 
            <div className="col-sm-2">
            <button 
                className="btn btn-outline-light btn-sm px-3" 
                type="submit"  
                onClick={actCursos}
                >Carga de Cursos
            </button>
            </div>
            <div className="col-sm-2">
            <button 
                className="btn btn-outline-light btn-sm px-3" 
                type="submit"  
                onClick={actApuntes}
                >Carga de Apuntes
            </button>
            </div>
            
        </div>
        <div>
            {carga_estudiante?<CargaEstudiante/>
            :carga_cursos ? <CargaCursos/>
            :carga_apuntes ? <CargaApuntes/>:
            <h1>Cargas</h1>
            }
        </div>
        </div>
    )
}
export default Cargas;