import React,{useState} from "react";
import "../App.css"
function Curso(){
    const[img,setImg] = useState('');
    const[codigo,setCodigo] = useState('');
    

    const handleInputChange = (event)=>{
        setCodigo(event.target.value)
    }

    const cargar = async(event)=>{
        console.log("ver analizar")
        
        event.preventDefault();
        const res = await fetch('http://192.168.185.104:3000/graficaCodigo',{
            method:'post',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                "codigo":codigo
            })
        })

        const data_carga = await res.json();

        let foto = "data:image/png;base64,"+data_carga.img
        console.log(foto)
        setImg(foto)
    }
    return(
        <div>
        <form onSubmit={cargar}>
            <div>
            <div className="mb-3">
            <label htmlFor="exampleFormControlInput1" className="form-label">Código Curso</label>
            <input 
            type="text" 
            className="form-control" 
            id="exampleFormControlInput1" 
            placeholder="Código" 
            name="codigo"
            onChange={handleInputChange}
             />
            </div>
            </div>
                <div className="col-sm-2">
                    <button 
                        className="btn btn-outline-light btn-sm px-3" 
                        type="submit"
                        >Analizar
                    </button>
            </div>
            
        </form>
        <br/>
        <div className="pic">
            <img src={img}/>
        </div>
        
        </div>
    )
}

export default Curso;