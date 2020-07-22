import React from 'react';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Nav from './components/Nav.js'
import Dashboard from './components/Dashboard.js'
import Containers from './components/Containers.js'
import Images from './components/Images.js'

function App() {
  return (
    <Router>
      <Nav />
      <Switch>
        <div>
            <Route path="/" exact={true} component={Dashboard} />
            <Route path="/containers" exact={true} component={Containers} />
            <Route path="/images" exact={true} component={Images} />
        </div>
      </Switch>
    </Router>
  );
}

export default App;
