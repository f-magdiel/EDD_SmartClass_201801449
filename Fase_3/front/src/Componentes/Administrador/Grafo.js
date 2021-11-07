import React,{useState} from "react";
import "./estilo.css";

function Grafo(){
    const [image,setImage] = useState("");

    const cargar = async(event)=>{
        console.log("ver grafo")
        const res = await fetch('http://192.168.185.104:3000/graficaGrafo',{
            method:'post',
            headers:{
                'Content-Type':'application/json'
            }
        })

        const data_carga = await res.json();
         
        let foto = "data:image/png;base64,"+data_carga.img
        console.log(foto)
        setImage(foto)
    }
    
    return(
        <div>
            <h1>Imagen</h1>
            <div className="col-sm-2">
            <button 
                className="btn btn-outline-light btn-sm px-3" 
                type="submit"  
                onClick={cargar}
                >Ver
            </button>
            </div>
            <br/>
            <div className="pic">
                <img src={image}  />    
            </div>
            
            
        </div>
    )
}
export default Grafo;