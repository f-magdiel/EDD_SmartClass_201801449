import React,{useEffect,useState} from "react";
import "./stile.css"
import {Table,Button,Container,Modal,ModalBody,ModalHeader,FormGroup,ModalFooter} from 'reactstrap';


function VerApunte({value}){
    const [ventana,setVentana]= useState(false);
    const [user,setUser]=useState(value);
    
    const [info,setInfo] = useState([]);
    function abrir(){
        setVentana(true);
    }
    function cerrar(){
        setVentana(false);
    }
    useEffect(()=>{
        console.log("get method")
        getDatos();
        
      },[])

     
    const getDatos=async()=>{
        console.log("user")
        console.log(user)
        const res = await fetch('http://192.168.185.104:3000/getEstudiantes',{
          method:'post',
          headers:{
            'Content-Type':'application/json'
          },
          body: JSON.stringify({
            "carnet":user
          })
        })
        const data = await res.json();
        const infoObj = JSON.parse(data);
        setInfo(infoObj);
    }
    

    return(
        <>
        <br/>
        <br/>
        <Container>
            <Table striped bordered hover variant="dark" className="tableh">
                <thead><tr>
                <th>Titulo</th>
                <th>Contenido</th>
                </tr>
                </thead>
                
                <tbody className="tableHover">
                  {info.map(user=>(
                      <tr>
                      <td>{user.titulo}</td>
                      <td>{user.contenido}</td>
                  </tr>
                  ))

                  }      
                    
                </tbody>
            </Table>
        </Container>

        </>

    )
}

export default VerApunte;