import React,{useState,useEffect} from "react";
import {Link} from 'react-router-dom';

import Apunte from "./Apunte";
import Curso from "./Curso";
import Nuevo from "./Apuntes/Nuevo"

function Estudiante(props){
    console.log("Estudiantes")
    console.log(props.location.state)
    const [banderaApunte,setBanderaApunte] = useState(false);
    const [banderaCurso,setBanderaCurso] = useState(false);
    const [user,setUser] = useState('')

    function Apuntes(){
        setBanderaApunte(true);
        setBanderaCurso(false);
    }

    function Cursos(){
        setBanderaCurso(true);
        setBanderaApunte(false);
    }

    const getDatos=async()=>{
      const res = await fetch('http://192.168.185.102:3000/getEstudiantes',{
        method:'post',
        headers:{
          'Content-Type':'application/json'
        },
        body: JSON.stringify({
          "carnet":props.location.state
        })
      })
      const data = await res.json();
      const dataObj = JSON.parse(data)
      dataObj.map(function(dat){
        console.log(dat.titulo);
        console.log(dat.contenido);
      })
    }

    useEffect(()=>{
      getDatos();
      setUser(props.location.state)
      
    },[])

    return(
    <section className="vh-100 gradient-custom">  
      <nav className="navbar navbar-expand-lg bg-dark navbar-dark ">
      {/* Container wrapper */}
      <div className="container-fluid">
        {/* Navbar brand */}
        <a className="navbar-brand" href="#">Usuario: {user}</a>
        {/* Toggle button */}
        <button className="navbar-toggler" type="button" data-mdb-toggle="collapse" data-mdb-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <i className="fas fa-bars" />
        </button>
        {/* Collapsible wrapper */}
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-4 mb-lg-0">
          <div className="col-md-5">
          
            <button 
                className="btn btn-outline-light btn-sm px-3" 
                type="submit"  
                onClick={Apuntes}
                >Apuntes
                
            </button>
            
            </div>
            <div className="col-md-5">
            <button 
                className="btn btn-outline-light btn-sm px-3" 
                type="submit" 
                onClick={Cursos}
                >Cursos
                
            </button>
            </div>

            <div className="col-md-5">
            <Link to="/">
            <button 
                className="btn btn-outline-light btn-sm px-3" 
                type="submit"  
                >Salir
            </button>
            </Link>
            </div>
          </ul>
        </div>
      </div>
      {/* Container wrapper */}
    </nav>
    <div className="container py-5 h-10">
                   <div className="row d-flex justify-content-center align-items-center h-100">
                       <div className="col-12 col-md-8 col-lg-6 col-xl-12">
                           <div className="card bg-dark text-white" style={{borderRadius: '1rem'}}>
                               <div className="card-body p-5 text-center">
                                   <div className="mb-md-5 mt-md-4 pb-5">
                                    
                                    {banderaApunte?<Apunte value={user}/>
                                    :banderaCurso?<Curso value={user}/>
                                    :<h1>Bienvenido</h1>
                                    }
                                             
                                    </div>
                                  
                           </div>
                       </div>
                   </div>
               </div>
            </div>
    </section>
      
    )
}

export default Estudiante;