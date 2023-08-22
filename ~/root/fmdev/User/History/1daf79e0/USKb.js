import { connect } from 'react-redux';
import {DSH} from '../../constants';
import { Component } from 'react';
import React from 'react';

class Dsh extends Component{
    componentDidMount(){
        this.props.Dsh();
    }

    render (){
        return(
            <Header>
                <h1>Hello World</h1>
            </Header>
        )
    }
}

const mapStateToProps = ({ dsh }) => ({ dsh });

export default connect(mapStateToProps,{
    ...DshActions
})(Dsh);