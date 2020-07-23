import React, { Component, useState } from "react";
import { Container, Row, Col, Button } from "reactstrap";
import { Dropdown, DropdownToggle} from 'reactstrap';
import { DropdownMenu, DropdownItem } from 'reactstrap';


const ContainerButton = (props) => {

  const [dropdownOpen, setDropdownOpen] = useState(false);

  const toggle = () => setDropdownOpen(prevState => !prevState);

  return (
          <Dropdown direction="right" isOpen={dropdownOpen} toggle={toggle}>
            <DropdownToggle color="primary" caret>
                {props.name}
              </DropdownToggle>
            <DropdownMenu>
              <DropdownItem header>Header</DropdownItem>
              <DropdownItem>Some Action</DropdownItem>
              <DropdownItem disabled>Action (disabled)</DropdownItem>
              <DropdownItem divider />
              <DropdownItem>Foo Action</DropdownItem>
              <DropdownItem>Bar Action</DropdownItem>
              <DropdownItem>Quo Action</DropdownItem>
            </DropdownMenu>
          </Dropdown>
        );
}

class ContainerList extends Component {

  render() {
    const containers = this.props.containers;
    return (
      <Container>
        <Row>
          <Col>ID</Col>
          <Col>Name</Col>
          <Col>Status</Col>
          <Col>Image</Col>
          <Col></Col>
        </Row>
        {!containers || containers.length <= 0 ? (
        <Row>
          <Col>
            <b>Ops, no one here yet</b>
          </Col>
        </Row>
        ) : (
          containers.map(container => (
          <Row key={container.id}>
            <Col>
              <ContainerButton name={container.short_id} />
            </Col>
            <Col>{container.name}</Col>
            <Col>
              <Button outline color="success">{container.status}</Button>
            </Col>
            <Col>{container.image.tags}</Col>
            <Col></Col>
          </Row>
          ))
        )}
      </Container>
    );
  }

}

export default ContainerList;
