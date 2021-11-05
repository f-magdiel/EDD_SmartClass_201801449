import React,{useState} from "react";
import Reporte from "./Administrador/Reporte";

function Admin(props){
    
    const [reporte,setReporte] = useState(false);

    function estadoReporte(){
        setReporte(true);
    }
    return(
        <section className="vh-100 gradient-custom">  
          <nav className="navbar navbar-expand-lg bg-dark navbar-dark ">
          {/* Container wrapper */}
          <div className="container-fluid">
            {/* Navbar brand */}
            <a className="navbar-brand" href="#">Admin</a>
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
                    onClick={estadoReporte}
                    >Reportes
                    
                </button>
                
                </div>
                <div className="col-md-5">
                <button 
                    className="btn btn-outline-light btn-sm px-3" 
                    type="submit" 
                    
                    >Cargas
                    
                </button>
                </div>
    
                <div className="col-md-5">
                
                <button 
                    className="btn btn-outline-light btn-sm px-3" 
                    type="submit"  
                    >Salir
                </button>
                
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
                                        {reporte?<Reporte/>
                                        :<h1>Admin</h1>
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

export default Admin;