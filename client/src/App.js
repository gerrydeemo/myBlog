import Home from "./Pages/Home";
import Login from "./Pages/Login";
import CreateArticle from "./Pages/CreateArticle";

import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
function App() {
  return (
    <div>
    <Router>
      <Routes>
        <Route path="/" exact element={<Home/>} />
        <Route path="/login" element={<Login/>} />
        <Route path="/createarticle" element={<CreateArticle/>} />
      </Routes>
    </Router>
    </div>
  );
}

export default App;
