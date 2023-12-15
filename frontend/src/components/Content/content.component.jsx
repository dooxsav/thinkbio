import './Content.style.css';

import CartographieClient from '../AcceuilComponent/CartographieClient/CartographieClient.component';
import EtatTables from '../AcceuilComponent/EtatdesTables/EtatTables.component'
import MaJTables from '../AcceuilComponent/MaJComponent/MaJTables.component'

const Content = () => {
    return(
        <div className="content-container container-fluid">
            <CartographieClient className='w-auto h-auto'/>
            < EtatTables className='w-auto h-auto'/>
            < MaJTables className='w-auto h-auto'/>
        </div>
    )
}

export default Content;