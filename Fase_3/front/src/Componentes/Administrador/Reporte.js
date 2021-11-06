import React ,{useState}from "react";
import Lista from "./Lista";
import Graf from "./Grafo";
function Reporte(){

    const [hash,setHash] = useState(false);
    const [grafo,setGrafo] = useState(false);

    function Hash(){
        setHash(true);
        setGrafo(false);
    }

    function Grafo(){
        setGrafo(true);
        setHash(false);
    }

    return(
        
        <div>
            <div className="row">
            <div className="col-sm-2">
            <button 
                className="btn btn-outline-light btn-sm px-3" 
                type="submit"  
                onClick={Hash}
                >Reporte hash
            </button>
            </div> 
            <div className="col-sm-2">
            <button 
                className="btn btn-outline-light btn-sm px-3" 
                type="submit"  
                onClick={Grafo}
                >Reporte Grafo
            </button>
            </div>
            
        </div>
        <div>
            {hash? <Lista/>
            :grafo?<Graf/>
            :<h1>Reportes</h1> }
        </div>
        </div>
       
    )
}
export default Reporte;