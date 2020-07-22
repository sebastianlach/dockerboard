import React, { Component } from "react";
import { Table } from "reactstrap";

class ImageList extends Component {

  render() {
    const images = this.props.images;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>ID</th>
            <th>Tags</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!images || images.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            images.map(image => (
              <tr key={image.id}>
                <td>{image.short_id}</td>
                <td>{image.tags}</td>
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

export default ImageList;
