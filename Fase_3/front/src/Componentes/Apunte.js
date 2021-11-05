import React,{useState} from "react";
import Nuevo from "./Apuntes/Nuevo"
import VerApunte from "./Apuntes/VerApunte"

function Apunte({value}){

    const [nuevo,setNuevo] = useState(false);
    const [ver,setVer] = useState(false);
    const [user,setUser] = useState('');
   
    function nuevoApunte(){
        setNuevo(true);
        console.log("Nuevo Apunte")
        console.log(value)
        setUser(value)
        setVer(false)
    }

    function verApunte(){
        console.log("ver apunte")
        setVer(true);
        setNuevo(false);
        setUser(value);
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
                type="submit"  
                onClick={verApunte}
                >Ver apunte
            </button>
            </div>
            
        </div>
        <div>
            {nuevo?<Nuevo value={user}/>
            :ver?<VerApunte value={user}/>:
            <h1>Apuntes</h1>
            
            }
        </div>
        </div>
       
    )
}

export default Apunte;