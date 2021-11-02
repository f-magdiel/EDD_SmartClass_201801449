import React,{useState} from "react";

function Nuevo (){

    const [datos,setDatos] = useState ({
        titulo:'',
        contenido:''
    });

    const handleInputChange = (event) =>{
        console.log(event.target.value)
        setDatos({
            ...datos,
            [event.target.name]:event.target.value
        })
    }
    return(
        <div>
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
                type="submit"  >Guardar
            </button>
        </div>
        </div>
    )
}

export default Nuevo;