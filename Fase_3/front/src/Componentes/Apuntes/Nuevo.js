import React,{useState,useEffect} from "react";
import swal from "sweetalert";


function Nuevo ({value}){

    const [datos,setDatos] = useState ({
        titulo:'',
        contenido:''
    });
    const [user,setUser] = useState('');

    const handleInputChange = (event) =>{
        console.log(event.target.value)
        setDatos({
            ...datos,
            [event.target.name]:event.target.value
        })
    }

    useEffect(()=>{
        setUser(value)
        
      },[])
    
    const enviarDatos = async (event)=>{
        console.log("Envio de datos")
        console.log(value)//aqui me quedo
        event.preventDefault();

        const res = await fetch('http://192.168.185.104:3000/newApunte',{
            method:'post',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                "carnet":user,
                "titulo":datos.titulo,
                "contenido":datos.contenido
            })
        })

        const data = await res.json();
        var estado;
        data.map(function(dat){
            estado = dat.estado
        })

        if(estado ==="200"){
            swal({
                title:"Apunte",
                text:"Apunte guardado",
                icon:"success",
                button:"Aceptar"
            })
        }else if(estado==="400"){
            swal({
                title:"Apunte",
                text:"Apunte no guardado",
                icon:"error",
                button:"Aceptar"
            })
        }
        event.target.reset();
    }
   
    return(
        <form onSubmit={enviarDatos}>
            <div>
            <div className="mb-3">
            <label htmlFor="exampleFormControlInput1" className="form-label">Titulo</label>
            <input 
            type="text" 
            className="form-control" 
            id="exampleFormControlInput1" 
            placeholder="Título" 
            name="titulo"
            onChange={handleInputChange}
             />
            </div>
            <div className="mb-3">
            <label htmlFor="exampleFormControlTextarea1" className="form-label">Contenido</label>
            <textarea 
            className="form-control" 
            id="exampleFormControlTextarea1" 
            rows={10} 
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
                        >Guardar
                    </button>
            </div>
        </form>
    )
}

export default Nuevo;