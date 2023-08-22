//H2O+

import React, { Component } from 'react';
import { ConfigContainer } from '../../styles/ConfigContainer';
import {
  Header
} from '../../styles/global';
import { connect } from 'react-redux';
import { Creators as CourseActions } from '../../store/ducks/course';
import { Creators as IndicatorActions } from '../../store/ducks/indicator';
import { Creators as SubjectActions } from '../../store/ducks/subject';
import { Creators as SemesterActions } from '../../store/ducks/semester';
import { Creators as PhenomenonActions } from '../../store/ducks/phenomenon';


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

export default connect(mapStateToProps,
  { //NÃO APAGAR (H20+)
  })(Dsh);