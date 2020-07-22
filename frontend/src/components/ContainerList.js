import React, { Component } from "react";
import { Table } from "reactstrap";

class ContainerList extends Component {

  render() {
    const containers = this.props.containers;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Name</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!containers || containers.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            containers.map(container => (
              <tr key={container.pk}>
                <td>{container.image.tags}</td>
                <td align="center">
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }

}

export default ContainerList;
