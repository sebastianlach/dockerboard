import React, { Component } from "react";
import { Table } from "reactstrap";

class ContainerList extends Component {

  render() {
    const containers = this.props.containers;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Status</th>
            <th>Image</th>
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
              <tr key={container.id}>
                <td>{container.short_id}</td>
                <td>{container.name}</td>
                <td>{container.status}</td>
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
