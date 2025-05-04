import React, { useEffect } from 'react';
import { motion } from 'framer-motion';
import { ChevronDown } from 'lucide-react';

const Hero = () => {
  // Create particles effect
  useEffect(() => {
    const createParticles = () => {
      const heroSection = document.getElementById('hero');
      if (!heroSection) return;
      
      // Clear existing particles
      const existingParticles = document.querySelectorAll('.particle');
      existingParticles.forEach(particle => particle.remove());
      
      // Create new particles
      const particleCount = window.innerWidth < 768 ? 40 : 100;
      const colors = ['#ffffff', '#E9F1F7', '#93c5fd'];
      
      for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        
        // Random position
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.top = `${Math.random() * 100}%`;
        
        // Random size
        const size = Math.random() * 3 + 1;
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        
        // Random color
        particle.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        
        // Random animation delay
        particle.style.animationDelay = `${Math.random() * 10}s`;
        
        heroSection.appendChild(particle);
      }
    };
    
    createParticles();
    window.addEventListener('resize', createParticles);
    
    return () => {
      window.removeEventListener('resize', createParticles);
    };
  }, []);
  
  return (
    <section 
      id="hero" 
      className="relative min-h-screen flex items-center justify-center bg-gradient-to-b from-space-navy via-space-dark to-space-purple overflow-hidden"
    >
      <div className="star-field"></div>
      <div className="container-custom relative z-10 py-20 md:py-0">
        <div className="max-w-3xl mx-auto text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            <p className="text-space-accent font-medium mb-4">AEROSPACE & AEROPHYSICS</p>
            <h1 className="text-white mb-6">
              Exploring the Boundaries of 
              <span className="text-space-accent"> Aerospace Science</span>
            </h1>
            <p className="text-gray-300 text-lg mb-8 md:text-xl">
              Author of 3 books on advanced aerodynamics, computational fluid dynamics, 
              and aerospace engineering applications using Python and Django.
            </p>
            
            <div className="flex flex-col sm:flex-row justify-center gap-4">
              <motion.a 
                href="#books" 
                className="btn-primary"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                Explore My Books
              </motion.a>
              <motion.a 
                href="/contact" 
                className="btn-secondary"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                Get in Touch
              </motion.a>
            </div>
          </motion.div>
        </div>
      </div>
      
      <a 
        href="#about" 
        className="absolute bottom-8 left-1/2 transform -translate-x-1/2 text-white animate-bounce"
        aria-label="Scroll down"
      >
        <ChevronDown className="w-8 h-8" />
      </a>
    </section>
  );
};

export default Hero;
