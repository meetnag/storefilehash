import { useState } from 'react';
import StoreHash from '../abi/StoreHash.json'; 

async function connect(web3, setConnectedState) {

    const { ethereum } = window
    await ethereum.request({method: 'eth_requestAccounts'})
    setConnectedState(true)

}

async function setHashOnChain(web3, from, hash, setLoading) {

    const contract = new web3.eth.Contract(StoreHash.abi, "0x34b1b25Bf8a5d0aD2A37fA0531985dFfcDEB9AB7")


    try {

        setLoading(true)
        const _setHash = await contract.methods.storeHash(hash).send({from: from})

        if (_setHash.events.StoredHash) {
            setLoading(false)
            console.log(_setHash)
            alert ("Hash sent")
        }
    } catch (err) {
        setLoading(false)
        console.log(err)
        alert("Transaction not sent")
    }
    
    

   
}

export function Connect({isConnected, web3, setConnectedState}) {

    return (
        <button 
            disabled={ isConnected ? true : false }
            onClick={()=>connect(web3, setConnectedState)}
            className="connect"
        >
        Connect
        </button>
    )

}

export function SetHash({web3, from}) {

    const [hash, setHash] = useState("");
    const [loading, setLoading] = useState(false)

    return (
        <div className="input">

            <input 
                placeholder='hash'
                value={hash}
                onChange={(event)=>setHash(event.target.value)} 
            />
            <button 
                disabled={loading ? true : false} 
                onClick={()=>setHashOnChain(web3, from, hash, setLoading)}
            > 
                {loading ? "Sending" : "Set" }
            </button>

        </div>
    )

}

