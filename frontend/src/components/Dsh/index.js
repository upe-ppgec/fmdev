//H2O+

import React, { Component } from 'react';
import { ConfigContainer } from '../../styles/ConfigContainer';
import {
  Header
} from '../../styles/global';
import { connect } from 'react-redux';
import { Content } from './styles';
import images from './images/linhas1.png'
import images2 from './images/linhas2.png'
import images3 from './images/linhas3.png'
import images4 from './images/linhas4.png'

class Dsh extends Component {


  importImages = (i) => {
    return i.keys().map(i);
  }

  catchAll = () => {
    
    images = this.importImages('./images',false,'.png')

  }

  render() {

    return (
        <ConfigContainer size='big' style={{ color: '#000' }}>

          <Header>
            <h1>Dashboard</h1>
          </Header>

        <Content>
          {
            //FEITO DE MANEIRA BRUTA
            //PRECISA SER ALTERADA 
          }
          <div>
            <img key={0}
            style={{
              height:200,
              width:400,
              borderRadius:20,
              display: 20,
            }}
            src={images}
            alt='info'
            />
            <img key={1}
            style={{
              height:200,
              width:400,
              borderRadius:20,
              display: 20,
            }}
            src={images2}
            alt='info'
            />
            </div>
            <div>
            <img key={2}
            style={{
              height:200,
              width:400,
              borderRadius:20,
              display: 20,
            }}
            src={images3}
            alt='info'
            />
            <img key={3}
            style={{
              height:200,
              width:400,
              borderRadius:20,
              display: 20,
            }}
            src={images4}
            alt='info'
            />
            </div>
        </Content>


        </ConfigContainer >
    )
  }
}


export default connect()(Dsh);