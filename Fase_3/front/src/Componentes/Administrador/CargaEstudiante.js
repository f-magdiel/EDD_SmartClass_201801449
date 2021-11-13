import React,{useState} from "react";
import swal from "sweetalert";

function CargaEstudiante(){

    const [informacion,setInformacion] = useState("");

    const handleInputChange = (event)=>{
        console.log(event.target.value)
        setInformacion(event.target.value)
    }

    const enviarCarga = async(event)=>{
        console.log("enviar carga")
        event.preventDefault();
        console.log(informacion)
        const res = await fetch('http://192.168.185.102:3000/cargaEstudiantes',{
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
                title:"Carga Estudiantes",
                text:"Carga exitosa",
                icon:"success",
                button:"Aceptar"
            })
        }else{
            swal({
                title:"Carga",
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
            <label htmlFor="exampleFormControlTextarea1" className="form-label">Carga de Estudiantes</label>
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
export default CargaEstudiante;