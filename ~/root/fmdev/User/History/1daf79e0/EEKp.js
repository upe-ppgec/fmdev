import { connect } from 'react-redux';
import {DSH} from '../../constants';
import { Component } from 'react';
import React from 'react';
import {
    Header, Table, HeaderColumn, ItemColumn,
    FirstHeaderColumn, FirstItemColumn,
    StatusMsgContainer, LoadingContainer
  } from '../../styles/global';

class Dsh extends Component{
    componentDidMount(){
        this.props.Dsh();
    }

    render (){
        return(
            <div className='Dsh'>
                <PerfectScrollbar style={{ width: '100%', overflowX: 'auto' }}>
                    <ConfigContainer size='big' style={{ color: '#000' }}>
                        <Header>
                            <h1>Hello Puta</h1>
                        </Header>
                    </ConfigContainer>
                </PerfectScrollbar>
            </div>
        )
    }
}

export default Dsh;