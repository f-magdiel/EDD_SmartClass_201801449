import React,{useState} from "react";
import swal  from "sweetalert";
import {Link} from 'react-router-dom';
function Registro(){

  const [datos,setDatos]=useState({
    carnet:'',
    dpi:'',
    nombre:'',
    carrera:'',
    correo:'',
    password:'',
    edad:''
  });

  const handleInputChange = (event)=>{
    setDatos({
      ...datos,
      [event.target.name]:event.target.value
    })
  }

  const enviarInformacion = async (event) =>{
    event.preventDefault();
    const response = await fetch('http://192.168.185.104:3000/registro',{
      method:'post',
      headers:{
        'Content-Type':'application/json'
      },
      body:JSON.stringify({
        "carnet":datos.carnet,
        "dpi":datos.dpi,
        "nombre":datos.nombre,
        "carrera":datos.carrera,
        "correo":datos.correo,
        "password":datos.password,
        "edad":datos.edad
      })
    }
    
    )

    const data = await response.json();
    var estado;
    data.map(function(dat){
      estado = dat.estado;
      
    })

    if (estado ==="200"){
      swal({
        title:"Registro",
        text:"Se registro exitosamente",
        icon:"success",
        button:"Aceptar"
      })
    }else if (estado==="400"){
      swal({
        title:"Registro",
        text:"Registro fallido",
        icon:"error",
        button:"Aceptar"
      })
    }
    event.target.reset();
  }

    return(
        <form onSubmit={enviarInformacion}>
          <section className="vh-200 gradient-custom">
         <div className="container py-5 h-100">
          <div className="row d-flex justify-content-center align-items-center h-100">
            <div className="col-12 col-md-8 col-lg-6 col-xl-5">
              <div className="card bg-dark text-white" style={{borderRadius: '1rem'}}>
                <div className="card-body p-5 text-center">
                  <div className="mb-md-5 mt-md-4 pb-5">
                    <h2 className="fw-bold mb-2 text-uppercase">Registro</h2>
                    <div className="form-outline form-white mb-2">
                      <input 
                      type="text" 
                      id="typeCarnet" 
                      className="form-control form-control-lg"
                      name ="carnet"
                      onChange={handleInputChange}
                      />
                      <label className="form-label" >Carnet</label>
                    </div>
                    <div className="form-outline form-white mb-2">
                      <input 
                      type="text" 
                      id="typeDpi" 
                      className="form-control form-control-lg"
                      name = "dpi"
                      onChange = {handleInputChange}
                       />
                      <label className="form-label" >DPI</label>
                    </div>
                    <div className="form-outline form-white mb-2">
                      <input 
                      type="text" 
                      id="typeNombre" 
                      className="form-control form-control-lg"
                      name = "nombre"
                      onChange ={handleInputChange}
                      />
                      <label className="form-label">Nombre</label>
                    </div>
                    <div className="form-outline form-white mb-2">
                      <input 
                      type="text" 
                      id="typeCarrera" 
                      className="form-control form-control-lg "
                      name = "carrera"
                      onChange={handleInputChange}
                      />
                      <label className="form-label" >Carrera</label>
                    </div>
                    <div className="form-outline form-white mb-2">
                      <input 
                      type="text" 
                      id="typeCorreo" className="form-control form-control-lg" />
                      <label className="form-label" htmlFor="typeEmailX">Correo</label>
                    </div>
                    <div className="form-outline form-white mb-2">
                      <input 
                      type="password" 
                      id="typePassword" 
                      className="form-control form-control-lg"
                      name = "password"
                      onChange={handleInputChange}
                      />
                      <label className="form-label" htmlFor="typePasswordX">Password</label>
                    </div>
                    <div className="form-outline form-white mb-2">
                      <input 
                      type="text" 
                      id="typeEdad" 
                      className="form-control form-control-lg"
                      name = "edad"
                      onChange={handleInputChange}
                      />
                      <label className="form-label" >Edad</label>
                    </div>
                    <div>
                    <button className="btn btn-outline-light btn-lg px-5" type="submit">Registrarse</button>
                    </div>
                    <br/>
                    <Link to="/">
                    <div>                            
                    <button className="btn btn-outline-light btn-lg px-5" type="submit">Regresar</button>
                    </div>                           
                    </Link>
                  </div>                                                          
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
        </form>
    )
}

export default Registro;