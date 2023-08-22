import * as moment from 'moment';
import React, { Component } from 'react';
import { ConfigContainer } from '../../styles/ConfigContainer';
import {
  Header, Table, HeaderColumn, ItemColumn,
  FirstHeaderColumn, FirstItemColumn,
  StatusMsgContainer, LoadingContainer
} from '../../styles/global';
import { connect } from 'react-redux';
import PerfectScrollbar from 'react-perfect-scrollbar';
import { Creators as TrainModelActions } from '../../store/ducks/train_model';
import { Creators as ModelCopyActions } from '../../store/ducks/model_copy';
import { Creators as DialogActions } from '../../store/ducks/dialog';
import { Creators as DownloadActions } from '../../store/ducks/download';
import { actions as toastrActions } from 'react-redux-toastr';
import { Menu, MenuItem } from '@material-ui/core';
import MoreIcon from 'react-feather/dist/icons/more-horizontal';
import CopyIcon from 'react-feather/dist/icons/copy';
import KeyIcon from 'react-feather/dist/icons/key';
import DownloadIcon from 'react-feather/dist/icons/download';
import CodeIcon from 'react-feather/dist/icons/terminal';
import TrashIcon from 'react-feather/dist/icons/trash';
import { primaryColor } from '../../styles/global';
import { PRE_PROCESSING_RAW, TRAIN_PIPELINES } from '../../constants';
import AlertDialog from '../../components/AlertDialog';
import { ProgressSpinner } from 'primereact/progressspinner';

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