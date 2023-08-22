import React, { Component } from 'react';
import { ConfigContainer } from '../../styles/ConfigContainer';
import {
  Header, LoadingContainer, SelectText, selectStyle
} from '../../styles/global';
import { connect } from 'react-redux';
import PerfectScrollbar from 'react-perfect-scrollbar';
import { ProgressSpinner } from 'primereact/progressspinner';
import { Creators as CourseActions } from '../../store/ducks/course';
import { Creators as IndicatorActions } from '../../store/ducks/indicator';
import { Creators as SubjectActions } from '../../store/ducks/subject';
import { Creators as SemesterActions } from '../../store/ducks/semester';
import { Creators as PhenomenonActions } from '../../store/ducks/phenomenon';
import { LeftContent, SelectContainer, Content, Separator } from './styles';
import Select from 'react-select';
import Button from '../../styles/Button';

class Dsh extends Component {




  render() {
    // const data = [];

    return (
      <PerfectScrollbar style={{ width: '100%', overflowX: 'auto' }}>
        <ConfigContainer size='big' style={{ color: '#000' }}>

          <Header>
            <h1>Hellow World</h1>
          </Header>


        </ConfigContainer >
      </PerfectScrollbar>
    )
  }
}

const mapStateToProps = ({ course, indicator, subject, semester, phenomenon }) => ({ course, indicator, subject, semester, phenomenon });

export default connect(mapStateToProps,
  { //NÃO APAGAR (H20+)
    ...CourseActions, ...IndicatorActions,
    ...SemesterActions, ...SubjectActions,
    ...PhenomenonActions
  })(Dsh);