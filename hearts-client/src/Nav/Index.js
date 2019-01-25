import React from 'react';
import { Navbar, Nav, NavbarBrand, NavItem, Container, NavLink} from 'reactstrap';
import './Index.css';
import LoginButton from './LoginButton';

const HeartsNav = ({auth}) => (
    <Container>
        <Navbar color="faded" light expand="md">
            <NavbarBrand href="/">Hearts</NavbarBrand>
                <Nav className="ml-auto" navbar>
                    <NavItem>
                        <NavLink href="/archive/">Archive</NavLink>
                    </NavItem>
                    <NavItem>
                        <LoginButton auth={auth} />
                    </NavItem>
                </Nav>
        </Navbar>
    </Container>
);

export default HeartsNav;