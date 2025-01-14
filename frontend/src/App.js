import React from 'react'
import './App.css';

import { Container } from 'react-bootstrap'
import { BrowserRouter as  Router, Route, Routes } from 'react-router-dom'

import Header from './components/Header';
import Footer from './components/Footer'
import HomeScreen from './components/screens/HomeScreen';
import LoginScreen from './components/screens/LoginScreen';
import RegisterScreen from './components/screens/RegisterScreen';
import PlanScreen from './components/screens/PlanScreen';
import VideoScreen from './components/screens/VideoScreen';
import ProfileScreen from './components/screens/ProfileScreen';


function App() {
  return (
    <Router>
    <div>
      
      <Header />
        <main className='py-3'>
          <Container>
            <Routes>
            <Route path='/home' element={<HomeScreen />} />
            <Route path='/' element={<LoginScreen />} exact/>
            <Route path='/register' element={<RegisterScreen />} />
            <Route path='/profile' element={<ProfileScreen />} />
            <Route path='/plans' element={<PlanScreen />} />
            <Route path='/video/:id' element={<VideoScreen />} />

            </Routes>
          </Container>
        </main>
      <Footer />
    </div>
    </Router>
  );
}

export default App;
