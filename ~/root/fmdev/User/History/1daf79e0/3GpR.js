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
            <h1>Hellow World</h1>
          </Header>

          <h2>Temos uma feat</h2>




        </ConfigContainer >
    )
  }
}

const mapStateToProps = ({ course, indicator, subject, semester, phenomenon }) => ({ course, indicator, subject, semester, phenomenon });

export default connect()(Dsh);