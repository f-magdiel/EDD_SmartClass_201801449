import React ,{useState}from "react";

function Lista(){
    const [basImg,setBasImg] = useState('')

    const cargar = async(event) =>{
        console.log("ver")
        event.preventDefault();
        const res = await fetch('http://192.168.185.104:3000/graficaHash',{
            method:'post',
            headers:{
                'Content-Type':'application/json'
            }
        })

        const dato_carga = await res.json();
        
        let foto = "data:image/png;base64,"+dato_carga.img
        console.log(foto)
        setBasImg(foto)
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
            <img src={basImg} height="200px"/>
        </div>
    )
}
export default Lista;