//H2O+

import React, { Component } from 'react';
import { ConfigContainer } from '../../styles/ConfigContainer';
import {
  Header
} from '../../styles/global';
import { connect } from 'react-redux';


class Dsh extends Component {
  render() {

    return (
        <ConfigContainer size='big' style={{ color: '#000' }}>

          <Header>
            <h1>Dashboard</h1>
          </Header>

          <section>
          <h2>Temos uma feat</h2>
          </section>



        </ConfigContainer >
    )
  }
}


export default connect()(Dsh);