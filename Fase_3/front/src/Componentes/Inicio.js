import React from 'react';
import {Link} from 'react-router-dom';

function Inicio(){

    return(
        <div>
        
         <section className="vh-100 gradient-custom">
           <div className="container py-5 h-100">
             <div className="row d-flex justify-content-center align-items-center h-100">
               <div className="col-12 col-md-8 col-lg-6 col-xl-5">
                 <div className="card bg-dark text-white" style={{borderRadius: '1rem'}}>
                   <div className="card-body p-5 text-center">
                     <div className="mb-md-5 mt-md-4 pb-5">
                       <h2 className="fw-bold mb-2 text-uppercase">Fase 3</h2>
                       <p className="text-white-50 mb-5">Estructura de Datos</p>
                       <Link to="/login">
                       <div>
                       <button className="btn btn-outline-light btn-lg px-5 " type="submit" >Login</button>
                       </div>
                       </Link>
                       <br/>
                       <Link to="/registro">
                       <div>
                       <button className="btn btn-outline-light btn-lg px-5" type="submit">Registrarse</button>
                       </div>
                       </Link>
                       
                     </div>
                   </div>
                 </div>
               </div>
             </div>
           </div>
         </section>
       </div>
    )
}

export default Inicio;
