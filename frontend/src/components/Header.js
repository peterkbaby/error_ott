import React from 'react'
import { Nav, Navbar, NavDropdown, Container, Row, Col } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import { logout } from '../actions/userActions'
import { useNavigate } from 'react-router-dom'


export default function Header() {

  const userLogin = useSelector(state => state.userLogin)
  const { userInfo } = userLogin
  const navigate = useNavigate()
  const dispatch = useDispatch()
  const logoutHandler = () => {
    dispatch(logout());
    navigate('/');
};

  return (
    <header>
            <Navbar expand="lg" className="bg-body-tertiary" bg="dark" data-bs-theme="dark">
        <Container>
        <LinkContainer to='/'>
        <Navbar.Brand>Tour-Booking</Navbar.Brand>
        </LinkContainer>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
          <LinkContainer to='/home'>
            <Nav.Link ><i class="fa fa-home" aria-hidden="true"></i>Home</Nav.Link>
            </LinkContainer>
            { userInfo ? (
              <NavDropdown title = {userInfo.name} id='username'>
                <LinkContainer to={'/profile'}>
                  <NavDropdown.Item>Profile</NavDropdown.Item>
                </LinkContainer>
                <NavDropdown.Item onClick={logoutHandler}>Logout</NavDropdown.Item>
              </NavDropdown> 
             ) : (

            <LinkContainer to='/'>
            <Nav.Link><i class="fa fa-user" aria-hidden="true"></i>Login</Nav.Link>
            </LinkContainer>
            )}
          </Nav>
          
      </Navbar.Collapse>
      </Container>
    </Navbar>
    </header>
  )
}
