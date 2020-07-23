import React, { Component } from "react";
import { Container, Row, Col } from "reactstrap";

class ImageList extends Component {

  render() {
    const images = this.props.images;
    return (
      <Container>
        <Row>
          <Col>ID</Col>
          <Col>Tags</Col>
          <Col></Col>
        </Row>
        {!images || images.length <= 0 ? (
        <Row>
          <Col>
            <b>Ops, no one here yet</b>
          </Col>
        </Row>
        ) : (
          images.map(image => (
          <Row key={image.id}>
            <Col>{image.short_id}</Col>
            <Col>{image.tags}</Col>
            <Col></Col>
          </Row>
        ))
        )}
      </Container>
    );
  }

}

export default ImageList;
