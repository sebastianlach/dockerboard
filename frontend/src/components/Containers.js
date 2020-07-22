import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import ContainerList from "./ContainerList";

import axios from "axios";

import { API_URL } from "../constants";

class Containers extends Component {

  state = {
    containers: []
  };

  componentDidMount() {
    this.resetState();
  }

  getContainers = () => {
    axios.get(API_URL + 'containers/').then(res => this.setState({containers: res.data}));
  };

  resetState = () => {
    this.getContainers();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <ContainerList
              containers={this.state.containers}
              resetState={this.resetState}
            />
          </Col>
        </Row>
      </Container>
    );
  }

}

export default Containers;
