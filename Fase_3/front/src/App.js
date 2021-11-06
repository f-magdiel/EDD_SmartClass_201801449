import React from "react";
import {BrowserRouter as Router,Route,Switch} from 'react-router-dom';

//Componentes
import Login from "./Componentes/Login";
import Registro from "./Componentes/Registro";
import Admin from "./Componentes/Admin";
import Inicio from "./Componentes/Inicio";
import Estudiante from "./Componentes/Estudiante";
import Apunte from "./Componentes/Apunte";
import NuevoApunte from "./Componentes/Apuntes/Nuevo"
import VerApunte from "./Componentes/Apuntes/VerApunte"

import "./App.css";


function App(){

  return(
    <Router>
      <Switch>
      <Route exact path="/" component={Inicio}/>
      <Route exact path="/login" component={Login}/>
      <Route exact path="/registro" component={Registro}/>
      <Route exact path="/admin" component={Admin}/>
      <Route exact path="/estudiante" component={Estudiante}/>
      <Route exact path="/estudiante/apunte" component={Apunte}/>
      <Route exact path="/estudiante/apunte/nuevo" component={NuevoApunte}/>
      <Route exact path="/estudiante/apunte/ver" component={VerApunte}/>
      
      </Switch>
    </Router>
         
  )
   
}


export default App