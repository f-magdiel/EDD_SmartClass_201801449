import React, { useState } from "react";
import {Redirect,Link} from 'react-router-dom';
import swal from "sweetalert";


function Login(){
    
    const [Loginadmin,setLoginadmin] = useState(false);
    const [LoginUser,setLoginUser] = useState(false);

    const [datos,setDatos] = useState ({
        usuario:'',
        contraseña:''
    });

    const handleInputChange = (event) =>{
        //console.log(event.target.value)
        setDatos({
            ...datos,
            [event.target.name]:event.target.value
        })
    }
    
    const enviarDatos = async (event) =>{
        event.preventDefault();
        const res = await fetch('http://192.168.185.104:3000/login',{
            method:'post',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                "usuario":datos.usuario,
                "contraseña":datos.contraseña
            })
        }

        )
        const data = await res.json();
         var tipo,bandera;
        data.map(function(dat){
            tipo = dat.tipo;
            bandera = dat.bandera;
        })
        console.log(bandera)
        console.log(tipo)
        if(tipo ==="admin" && bandera===true){
            swal({
                title:"Admin",
                text:"Sesión iniciada",
                icon:"success",
                button:"Aceptar"
              })
            setLoginadmin(true);
        }else if(tipo ==="estudiante" && bandera ===true){
            swal({
                title:"Estudiante",
                text:"Sesión iniciada",
                icon:"success",
                button:"Aceptar"
              })
            setLoginUser(true);
        }else if (tipo==="error"){
            swal({
                title:"Login",
                text:"Contraseña o carnet inválido",
                icon:"error",
                button:"Aceptar"
              })
        }
        
        event.target.reset();
    } 

    
    return(
       <div>
           {Loginadmin ? <Redirect to="/admin"/>
           :
           LoginUser ? <Redirect to ="/estudiante"/>
           :
           <form onSubmit={enviarDatos} >
           <section className="vh-100 gradient-custom">
               <div className="container py-5 h-100">
                   <div className="row d-flex justify-content-center align-items-center h-100">
                       <div className="col-12 col-md-8 col-lg-6 col-xl-5">
                           <div className="card bg-dark text-white" style={{borderRadius: '1rem'}}>
                               <div className="card-body p-5 text-center">
                                   <div className="mb-md-5 mt-md-4 pb-5">
                                       <h2 className="fw-bold mb-2 text-uppercase">Login</h2>
                                           <p className="text-white-50 mb-5">Por favor ingrese su usuario  y contraseña</p>
                                               <div className="form-outline form-white mb-4">
                                                   <input 
                                                   type="text" 
                                                   id="typeUsuario" 
                                                   className="form-control form-control-lg" 
                                                   name="usuario" 
                                                   onChange={handleInputChange} />
                                                   <label className="form-label" htmlFor="typeEmailX">Carnet</label>
                                               </div>
                                               <div className="form-outline form-white mb-4">
                                                   <input 
                                                   type="password" 
                                                   id="typeContrasena" 
                                                   className="form-control form-control-lg" 
                                                   name="contraseña" 
                                                   onChange={handleInputChange} />
                                                   <label className="form-label" htmlFor="typePasswordX">Contraseña</label>
                                               </div>
                                               <div>
                                                   <button 
                                                   className="btn btn-outline-light btn-lg px-5" 
                                                   type="submit"  >Login</button>
                                                </div>
                                                <br/>
                                                 <Link to="/">
                                                <div>
                                                <button className="btn btn-outline-light btn-lg px-5" type="submit">Regresar</button>
                                                </div>
                                                </Link>
                                   </div>
                                   <div>
                                    <p className="mb-0">Estructura de Datos </p>
                                   </div>
                           </div>
                       </div>
                   </div>
               </div>
            </div>
           </section>
           </form>
        }   
        </div>
    ) 
        
   
}
export default Login;