import React,{useState} from "react";
import swal from "sweetalert";

function CargaCursos(){

    const [informacion,setInformacion] = useState("");
    
    const handleInputChange = (event)=>{
        console.log(event.target.value)
        setInformacion(event.target.value)
    }

    const enviarCarga = async(event)=>{
        console.log("enviar cursos")
        event.preventDefault();
        const res = await fetch('http://192.168.185.104:3000/cargaCursos',{
            method:'post',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify(informacion)
        })

        const data = await res.json();
        console.log(data.estado)
        if(data.estado==="200"){
            swal({
                title:"Carga Cursos",
                text:"Carga exitosa",
                icon:"success",
                button:"Aceptar"
            })
        }else{
            swal({
                title:"Carga Cursos",
                text:"Carga fallida",
                icon:"error",
                button:"Aceptar"
            })
        }
        event.target.reset();
    }

    return(
        <form onSubmit={enviarCarga}>
            <div>
            <div className="mb-3">
            
            </div>
            <div className="mb-3">
            <label htmlFor="exampleFormControlTextarea1" className="form-label">Carga de Cursos</label>
            <textarea 
            className="form-control" 
            id="exampleFormControlTextarea1" 
            rows={14} 
            defaultValue={""} 
            name="contenido"
            onChange={handleInputChange}
            />
            </div>
            </div>
                <div className="col-sm-2">
                    <button 
                        className="btn btn-outline-light btn-sm px-3" 
                        type="submit"
                        >Cargar
                    </button>
            </div>
        </form>
    )

}

export default CargaCursos;