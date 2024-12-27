"""React app template generation module."""

def generate_app_template():
    return """import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import styled from 'styled-components';
import { AppContainer, Header, Logo, Nav, NavLink, MainContent, 
         TextContent, Title, Description, Button, ImageContainer, 
         Image } from './styles/components';
import { GlitchText } from './components/GlitchText';

const App = () => {
  return (
    <AppContainer className="cyber-cursor">
      <Header
        initial={{ y: -100, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.8 }}
      >
        <Logo
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ delay: 0.5 }}
        >
          <GlitchText text="JARVIS" />
        </Logo>
        <Nav>
          {['Home', 'Features', 'About', 'Contact'].map((item, index) => (
            <NavLink
              key={item}
              href="#"
              initial={{ opacity: 0, y: -20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.8 + index * 0.1 }}
              whileHover={{ scale: 1.1 }}
              whileTap={{ scale: 0.95 }}
            >
              {item}
            </NavLink>
          ))}
        </Nav>
      </Header>
      
      <MainContent
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 1, delay: 1 }}
      >
        <TextContent>
          <Title
            initial={{ x: -100, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            transition={{ duration: 0.8, delay: 1.5 }}
          >
            <GlitchText text="Welcome to the Future" />
          </Title>
          <Description
            initial={{ x: -100, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            transition={{ duration: 0.8, delay: 1.7 }}
          >
            Experience the next generation of AI assistance with JARVIS.
            Powered by cutting-edge technology and designed for the future.
          </Description>
          <Button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            initial={{ y: 50, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ duration: 0.8, delay: 1.9 }}
          >
            Get Started
          </Button>
        </TextContent>
        
        <ImageContainer
          initial={{ x: 100, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ duration: 0.8, delay: 2 }}
        >
          <Image
            src="https://source.unsplash.com/random/800x600/?cyberpunk,technology"
            alt="Cyberpunk Interface"
            whileHover={{ scale: 1.05 }}
            transition={{ duration: 0.3 }}
          />
        </ImageContainer>
      </MainContent>
    </AppContainer>
  );
};

export default App;""" 