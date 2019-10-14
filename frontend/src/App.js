import React from 'react';
import ReactDOM from 'react-dom';
import './App.css';
import './components/slider_rad'
import InputSlider from './components/slider_rad';


function App() {
  var mySlider = ReactDOM.render(InputSlider, document.body);


  return (
    <div className="App">
      <header className="App-header">
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <InputSlider/>
    </div>
  );
}

export default App;
