import "../styles/App.css"
import FormComponent from "./Form"

function App() {

  const handleSubmit = (formData: { field1: string; field2: number }) => {
    // Handle form submission logic here
    console.log(formData); // For demonstration purposes, you can replace this with your logic
  };


  return(
    <div className="app-wrapper">

      <nav>
        <div className="nav-logo">
          <h1>CodeTrendz</h1>
        </div>
        <div className="nav-links">
          <a>About</a>
          <a>Contact</a>
          <a>Contribute</a>
        </div>
      </nav>

      <FormComponent onSubmit={handleSubmit} />

    </div>
  )
 
}

export default App
