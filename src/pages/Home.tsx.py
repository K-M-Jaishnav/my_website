import React from 'react';
import Hero from '../components/home/Hero';
import About from '../components/home/About';
import FeaturedBooks from '../components/home/FeaturedBooks';
import LatestArticles from '../components/home/LatestArticles';
import ContactSection from '../components/home/Contact';

const Home = () => {
  return (
    <>
      <Hero />
      <About />
      <FeaturedBooks />
      <LatestArticles />
      <ContactSection />
    </>
  );
};

export default Home;
