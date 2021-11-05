import React ,{useState}from "react";
import Lista from "./Lista";

function Reporte(){

    const [hash,setHash] = useState(false);

    function Hash(){
        setHash(true);
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
                
                >Ver apunte
            </button>
            </div>
            
        </div>
        <div>
            {hash? <Lista/>
            :<h1>Reporte</h1>}
        </div>
        </div>
       
    )
}
export default Reporte;