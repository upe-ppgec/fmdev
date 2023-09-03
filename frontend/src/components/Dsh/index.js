//H2O+

import React, { Component } from 'react';
import { ConfigContainer } from '../../styles/ConfigContainer';
import {
  Header
} from '../../styles/global';
import { connect } from 'react-redux';
import { Content } from './styles';
import Chart from 'react-apexcharts';

class Dsh extends Component {
  constructor(props){
    super(props);
    this.state = {
      options:{
        chart: {
        id:"basic-bar"
        },
      xaxis: {
        categories: [1900,2000,2100]
      }
    },
    series: [
      {
        name:"Século",
        data: [30,40,50]

      }
    ]
  };
}

  render() {

    return (
        <ConfigContainer size='big' style={{ color: '#000' }}>

          <Header>
            <h1>Dashboard</h1>
          </Header>

        <Content>
          {
            //Primeira Coluna
          }
            <div className="dsh">
              <div className="row">
                <div className="mixed-chart">
                  <Chart
                  options={this.state.options}
                  series={this.state.series}
                  type='line'
                  />
                  <Chart
                  options={this.state.options}
                  series={this.state.series}
                  type='bar'
                  />
                </div>
              </div>
            </div>
        {
        //Segunda Coluna
        }
            <div className="dsh">
              <div className="row">
                <div className="mixed-chart">
                  <Chart
                  options={this.state.options}
                  series={this.state.series}
                  type='scatter'
                  />
                  <Chart
                  options={this.state.options}
                  series={this.state.series}
                  type='heatmap'
                  />
                </div>
              </div>
            </div>
          
        </Content>


        </ConfigContainer >
    )
  }
}
export default connect()(Dsh);
