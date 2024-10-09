import { useState } from 'react'
import './App.css'
import { BrowserRouter as Router,Routes,Route } from 'react-router-dom'
import Home from './components/Home'
import Header from './components/Header/Header'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Router>
      <Header/>
      <div className='pt-[108px]'>
      <Routes>
        <Route path='/' element={<Home/>}/>
      </Routes>
      </div>
    </Router>
  )
}

export default App
