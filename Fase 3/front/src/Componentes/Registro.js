import React from "react";

function Registro(){
    return(
        <section className="vh-200 gradient-custom">
         <div className="container py-5 h-100">
          <div className="row d-flex justify-content-center align-items-center h-100">
            <div className="col-12 col-md-8 col-lg-6 col-xl-5">
              <div className="card bg-dark text-white" style={{borderRadius: '1rem'}}>
                <div className="card-body p-5 text-center">
                  <div className="mb-md-5 mt-md-4 pb-5">
                    <h2 className="fw-bold mb-2 text-uppercase">Registro</h2>
                    <div className="form-outline form-white mb-2">
                      <input type="email" id="typeEmailX" className="form-control form-control-lg" />
                      <label className="form-label" >Carnet</label>
                    </div>
                    <div className="form-outline form-white mb-2">
                      <input type="email" id="typeEmailX" className="form-control form-control-lg" />
                      <label className="form-label" >DPI</label>
                    </div>
                    <div className="form-outline form-white mb-2">
                      <input type="email" id="typeEmailX" className="form-control form-control-lg" />
                      <label className="form-label">Nombre</label>
                    </div>
                    <div className="form-outline form-white mb-2">
                      <input type="email" id="typeEmailX" className="form-control form-control-lg " />
                      <label className="form-label" >Carrera</label>
                    </div>
                    <div className="form-outline form-white mb-2">
                      <input type="email" id="typeEmailX" className="form-control form-control-lg" />
                      <label className="form-label" htmlFor="typeEmailX">Correo</label>
                    </div>
                    <div className="form-outline form-white mb-2">
                      <input type="password" id="typePasswordX" className="form-control form-control-lg" />
                      <label className="form-label" htmlFor="typePasswordX">Password</label>
                    </div>
                    <div className="form-outline form-white mb-2">
                      <input type="email" id="typeEmailX" className="form-control form-control-lg" />
                      <label className="form-label" >Edad</label>
                    </div>
                    <button className="btn btn-outline-light btn-lg px-5" type="submit">Registrarse</button>
                  </div>
                 
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    )
}

export default Registro;