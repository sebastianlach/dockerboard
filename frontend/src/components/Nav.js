import React, { Component} from "react";
import { Link, useLocation } from 'react-router-dom';

function DashboardLink() {
    const active = useLocation().pathname === '/' ? 'active' : null;
    return ( 
        <li className="nav-item">
            <Link to="/">
                <span className={"nav-link " + active}>
                    Dashboard
                </span>
            </Link>
        </li>
    );
}

function ContainersLink() {
    const active = useLocation().pathname === '/containers' ? 'active' : null;
    return ( 
        <li className="nav-item">
            <Link to="/containers">
                <span className={"nav-link " + active}>
                    Containers
                </span>
            </Link>
        </li>
    );
}

function ImagesLink() {
    const active = useLocation().pathname === '/images' ? 'active' : null;
    return ( 
        <li className="nav-item">
            <Link to="/images">
                <span className={"nav-link " + active}>
                    Images
                </span>
            </Link>
        </li>
    );
}


class Nav extends Component {

    render() {
        return (
            <header>
                <nav className="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
                    <Link to="/">
                        <span className="navbar-brand">Dockerboard</span>
                    </Link>
                    <div className="collapse navbar-collapse" id="navbarCollapse">
                        <ul className="navbar-nav mr-auto">
                            <DashboardLink />
                            <ContainersLink />
                            <ImagesLink />
                            <li className="nav-item">
                                <span className="nav-link disabled">v0.1.0</span>
                            </li>
                        </ul>

                        <button className="btn btn-secondary">Run container</button>
                        <button className="btn btn-secondary">Pull image</button>

                    </div>
                </nav>
            </header>
        );
    }

}

export default Nav;
