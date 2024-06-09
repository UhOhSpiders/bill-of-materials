import useFetch from '../utilities/useFetch'
import './App.css'

import BOMTable from './BOMTable'

function App() {
  const { data, isLoading, error } = useFetch(`/products`);
  return (
    <>
      <h1>Bill of Materials</h1>
      {isLoading ? (
        <p>loading...</p>
      ): error ? (
        console.log(error)
      ) : (
        <>
        <BOMTable data={data}/>
        </>
      )
    
    }
      
    </>
  )
}

export default App
