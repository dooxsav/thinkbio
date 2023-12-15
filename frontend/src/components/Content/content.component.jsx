import './Content.style.css';

import CartographieClient from '../AcceuilComponent/CartographieClient/CartographieClient.component';
import EtatTables from '../AcceuilComponent/EtatdesTables/EtatTables.component'
import MaJTables from '../AcceuilComponent/MaJComponent/MaJTables.component'

const Content = () => {
    return(
        <div className="content-container">
            <div className="content-carte"><CartographieClient/></div>
            <div className="content-etattable"><EtatTables/></div>
            <div className="content-majtable"><MaJTables/></div>
        </div>
    )
}

export default Content;