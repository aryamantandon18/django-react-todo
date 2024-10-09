import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { MyProvider } from './context/context.jsx'

export const server = 'http://localhost:8000'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <MyProvider>
    <App/>
    </MyProvider>
  </StrictMode>,
)
