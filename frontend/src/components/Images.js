import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import ImageList from "./ImageList";

import axios from "axios";

import { API_URL } from "../constants";

class Images extends Component {

  state = {
    images: []
  };

  componentDidMount() {
    this.resetState();
  }

  getImages = () => {
    axios.get(API_URL + 'images/').then(res => this.setState({images: res.data}));
  };

  resetState = () => {
    this.getImages();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <ImageList
              images={this.state.images}
              resetState={this.resetState}
            />
          </Col>
        </Row>
      </Container>
    );
  }

}

export default Images;
