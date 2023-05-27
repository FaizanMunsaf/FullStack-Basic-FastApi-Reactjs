import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import { useState, useEffect } from 'react';

function App() {
  const [people, setPeople] = useState([]);

  useEffect(()=>{
    axios.get("api/v1/users").then(res => setPeople(res.data));

  }, []);

  return people.map((p, index) => {
   return <p key={index}>
      {p.id} {p.first_name} {p.last_name} {p.middle_name} {p.gender} {p.roles}</p>
  })
}

export default App;
