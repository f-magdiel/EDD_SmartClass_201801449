import React,{useState,useEffect} from "react";

function App(){

  const [data,setData] = useState([{}])

  useEffect(()=>{
    fetch("/login").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  },[])

  return(
    <div>
      {(typeof data.miembros ==="undefined")?(
        <p>Loading...</p>
      ):(
        data.miembros.map((miembro,i)=>(
          <p key={i}>{miembro}</p>
        )
        )
      )
      }
    </div>
  )
}

export default App