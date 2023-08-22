//H2O+

import React, { Component } from 'react';
import { ConfigContainer } from '../../styles/ConfigContainer';
import {
  Header
} from '../../styles/global';
import { connect } from 'react-redux';
import { Content } from '../Dialog/styles';


class Dsh extends Component {
  render() {

    return (
        <ConfigContainer size='big' style={{ color: '#000' }}>

          <Header>
            <h1>Dashboard</h1>
          </Header>

        <Content>
            <h2>Temos uma feat</h2>
        </Content>


        </ConfigContainer >
    )
  }
}


export default connect()(Dsh);