import React, { Component, useState } from "react";
import { Container, Row, Col, Button } from "reactstrap";
import { Dropdown, DropdownToggle} from 'reactstrap';
import { DropdownMenu, DropdownItem } from 'reactstrap';


const ContainerButton = (props) => {

  const [dropdownOpen, setDropdownOpen] = useState(false);

  const toggle = () => setDropdownOpen(prevState => !prevState);

  return (
          <Dropdown direction="right" isOpen={dropdownOpen} toggle={toggle}>
            <DropdownToggle color="primary" className="btn-block" caret>
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
        {!containers || containers.length <= 0 ? (
        <Row>
          <Col>
            <b>Ops, no one here yet</b>
          </Col>
        </Row>
        ) : (
          containers.map(container => (
          <Row key={container.id} style={{padding: '8px'}}>
            <Col>
              <ContainerButton name={container.short_id} />
            </Col>
            <Col>
              <Button className="btn-block">{container.name}</Button>
            </Col>
            <Col>
              <Button className="btn-block" outline
                color={container.status === 'running' ? 'success' : 'secondary'}>
                {container.status}
              </Button>
            </Col>
            <Col>
              {container.image.tags}
            </Col>
          </Row>
          ))
        )}
      </Container>
    );
  }

}

export default ContainerList;
