import logo from './logo.svg';
import './App.css';
import {Connect, SetHash} from "./components/connect"
import { Web3 } from "web3";
import { useEffect, useState } from 'react';

function App() {

  const [connectedState, setConnectedState] = useState(false);
  const [address, setAddress] = useState('')

  let web3

  try {
    web3 = new Web3(window.ethereum)
  } catch (err) {
    alert ("Wallet not detected")
  }

  

  useEffect(()=>{

    async function checkConnect() {
      const accounts = await web3.eth.getAccounts()

      if (accounts.length > 0) {
        setConnectedState(true);
        setAddress(accounts[0])
      }
    }

    checkConnect()
   
  })
  
 


  return (
    <div className="App">
      
      <Connect isConnected={connectedState} web3={web3} setConnectedState={setConnectedState}/>
      <SetHash web3={web3} from={address}/>

    </div>
  );
}

export default App;
