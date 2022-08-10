import React,{useState} from 'react'

function Login() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [errorMessage, setErrorMessage] = useState('')
    const formSubmit = (e) => {
        e.preventDefault()
        if(!username && !password){
            setErrorMessage("Please enter username and password")
        }
        else if (!username){
            setErrorMessage("Please enter username")
        }
        else if (!password){
            setErrorMessage("Please enter password")
        }
        else{
            setErrorMessage("")
            setUsername('')
            setPassword('')
            alert("Login Successful")
        }
    }
  return (
    <div className='w-screen flex  items-center justify-center h-screen bg-black'>
         <form className="p-10 bg-black rounded-xl  space-y-5" onSubmit={(e) => formSubmit(e)}>
      <h1 className='font-bold text-2xl  text-transparent bg-clip-text bg-gradient-to-br from-red-600 to-orange-600'>Login</h1>
      <div className="flex flex-col space-y-2">
        <input className="bg-black w-96 px-3 py-2 text-white rounded-md border border-slate-400 outline-none placeholder:font-normal" type="text" placeholder="Your Username" onChange={(e) => setUsername(e.target.value)}/>
      </div>
      <div className="flex flex-col space-y-2">
        <input className="bg-black w-96 px-3 py-2 text-white rounded-md border border-slate-400 outline-none placeholder:font-normal" type="password" placeholder="Your Password" onChange={(e) => setPassword(e.target.value)}/>
      </div>
      <div className="flex flex-col space-y-2">
      <button className='hover:bg-gradient-to-r hover:from-orange-800 hover:to-red-800 bg-gradient-to-r from-red-600 to-orange-600 font-semibold rounded-lg py-2 text-white'>Login</button>
      </div>
      </form>
    </div>
  )
}

export default Login