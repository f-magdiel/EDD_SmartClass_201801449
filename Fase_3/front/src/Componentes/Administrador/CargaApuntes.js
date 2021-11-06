import React from "react";

function CargaApuntes(){
return(
    <form >
            <div>
            <div className="mb-3">
            
            </div>
            <div className="mb-3">
            <label htmlFor="exampleFormControlTextarea1" className="form-label">Carga de Apuntes</label>
            <textarea 
            className="form-control" 
            id="exampleFormControlTextarea1" 
            rows={14} 
            defaultValue={""} 
            name="contenido"
            
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
export default CargaApuntes;