import React,{useState} from "react";
import {BrowserRouter as Router,Route,Switch} from 'react-router-dom';

//Componentes
import Login from "./Componentes/Login";
import Registro from "./Componentes/Registro";
import Admin from "./Componentes/Admin";
import Inicio from "./Componentes/Inicio"
import Estudiante from "./Componentes/Estudiante"

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
      </Switch>
    </Router>
         
  )
   
}


export default App