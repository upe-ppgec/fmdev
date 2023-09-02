//H2O+

import { ConfigContainer } from '../../styles/ConfigContainer';
import { connect } from 'react-redux';
import { Content } from './styles';
import { Header } from '../../styles/global';
import Chart from "react-apexcharts";
import images from './images/linhas1.png'
import images2 from './images/linhas2.png'
import images3 from './images/linhas3.png'
import images4 from './images/linhas4.png'
import React, { Component } from 'react';

class Dsh extends Component {
  // MATRIX - TESTE DO APEXCHARTS
  constructor(props) {
    super(props);
    this.state = {
      options: {
        chart: {
          id: "basic-bar"
        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
        }
      },
      series: [{
        name: "series-1",
        data: [30,40,45,50,49,60,70,91]
      }]
    };
    // MATRIX - TESTE DO APEXCHARTS

  }
    importImages = (i) => {
        return i.keys().map(i);
    };

    catchAll = () => {
        images = this.importImages("./images", false, ".png");
    };

    render() {
        return (
            <ConfigContainer size="big" style={{ color: "#000" }}>
                <Header>
                    <h1>Dashboard</h1>
                </Header>

                <Content>
                    {
                        //FEITO DE MANEIRA BRUTA
                        //PRECISA SER ALTERADA
                    }
                    {/* MATRIX - TESTE DO APEXCHARTS */}
                    <div className="chart">
                        <div className="row">
                            <div className="mixed-chart">
                                <Chart
                                    options={this.state.options}
                                    series={this.state.series}
                                    type="bar"
                                    width="500"
                                />
                            </div>
                        </div>
                    </div>
                    {/* MATRIX - TESTE DO APEXCHARTS */}
                    <div>
                        <img
                            key={0}
                            style={{
                                height: 200,
                                width: 400,
                                borderRadius: 20,
                                display: 20,
                            }}
                            src={images}
                            alt="info"
                        />
                        <img
                            key={1}
                            style={{
                                height: 200,
                                width: 400,
                                borderRadius: 20,
                                display: 20,
                            }}
                            src={images2}
                            alt="info"
                        />
                    </div>
                    <div>
                        <img
                            key={2}
                            style={{
                                height: 200,
                                width: 400,
                                borderRadius: 20,
                                display: 20,
                            }}
                            src={images3}
                            alt="info"
                        />
                        <img
                            key={3}
                            style={{
                                height: 200,
                                width: 400,
                                borderRadius: 20,
                                display: 20,
                            }}
                            src={images4}
                            alt="info"
                        />
                    </div>
                </Content>
            </ConfigContainer>
        );
    }

}






export default connect()(Dsh);