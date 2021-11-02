import React,{useState} from "react";
import Nuevo from "./Apuntes/Nuevo"

function Apunte(){

    const [nuevo,setNuevo] = useState(false);

    function nuevoApunte(){
        setNuevo(true);

    }
    return(
        
        <div>
            <div className="row">
            <div className="col-sm-2">
            <button 
                className="btn btn-outline-light btn-sm px-3" 
                type="submit"  
                onClick={nuevoApunte}
                >Nuevo apunte
            </button>
            </div> 
            <div className="col-sm-2">
            <button 
                className="btn btn-outline-light btn-sm px-3" 
                type="submit"  >Ver apunte
            </button>
            </div>
            
        </div>
        <div>
            {nuevo?<Nuevo/>
            :<h1>Apuntes</h1>
            
            }
        </div>
        </div>
       
    )
}

export default Apunte;