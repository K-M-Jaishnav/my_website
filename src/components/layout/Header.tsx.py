import React, { useState, useEffect } from 'react';
import { NavLink, Link } from 'react-router-dom';
import { Menu, X, Rocket } from 'lucide-react';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);
  
  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 50) {
        setIsScrolled(true);
      } else {
        setIsScrolled(false);
      }
    };
    
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);
  
  const toggleMenu = () => setIsMenuOpen(!isMenuOpen);
  const closeMenu = () => setIsMenuOpen(false);
  
  return (
    <header 
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        isScrolled ? 'bg-white/95 shadow-md py-2' : 'bg-transparent py-4'
      }`}
    >
      <div className="container-custom">
        <div className="flex items-center justify-between">
          <Link to="/" className="flex items-center">
            <Rocket className={`w-8 h-8 ${isScrolled ? 'text-space-dark' : 'text-space-accent'} mr-2`} />
            <span className={`font-serif font-bold text-xl ${isScrolled ? 'text-space-dark' : 'text-white'}`}>
              Dr. Aerospace
            </span>
          </Link>
          
          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center space-x-8">
            <NavLink 
              to="/" 
              className={({ isActive }) => 
                `${isScrolled ? 'text-gray-800' : 'text-white'} hover:text-space-accent transition-colors ${isActive ? 'font-semibold' : ''}`
              }
            >
              Home
            </NavLink>
            <NavLink 
              to="/about" 
              className={({ isActive }) => 
                `${isScrolled ? 'text-gray-800' : 'text-white'} hover:text-space-accent transition-colors ${isActive ? 'font-semibold' : ''}`
              }
            >
              About
            </NavLink>
            <NavLink 
              to="/books" 
              className={({ isActive }) => 
                `${isScrolled ? 'text-gray-800' : 'text-white'} hover:text-space-accent transition-colors ${isActive ? 'font-semibold' : ''}`
              }
            >
              Books
            </NavLink>
            <NavLink 
              to="/blog" 
              className={({ isActive }) => 
                `${isScrolled ? 'text-gray-800' : 'text-white'} hover:text-space-accent transition-colors ${isActive ? 'font-semibold' : ''}`
              }
            >
              Blog
            </NavLink>
            <NavLink 
              to="/contact" 
              className={({ isActive }) => 
                `${isScrolled ? 'text-gray-800' : 'text-white'} hover:text-space-accent transition-colors ${isActive ? 'font-semibold' : ''}`
              }
            >
              Contact
            </NavLink>
          </nav>
          
          {/* Mobile Menu Button */}
          <button 
            className="md:hidden text-2xl focus:outline-none"
            onClick={toggleMenu}
            aria-label="Toggle menu"
          >
            {isMenuOpen ? 
              <X className={`w-6 h-6 ${isScrolled ? 'text-gray-800' : 'text-white'}`} /> : 
              <Menu className={`w-6 h-6 ${isScrolled ? 'text-gray-800' : 'text-white'}`} />
            }
          </button>
        </div>
      </div>
      
      {/* Mobile Menu */}
      <div 
        className={`fixed inset-0 bg-space-dark bg-opacity-95 z-40 transition-transform duration-300 ease-in-out transform ${
          isMenuOpen ? 'translate-x-0' : 'translate-x-full'
        } md:hidden`}
      >
        <div className="flex flex-col items-center justify-center h-full space-y-8 text-center">
          <NavLink 
            to="/" 
            className={({ isActive }) => 
              `text-white text-2xl hover:text-space-accent transition-colors ${isActive ? 'font-semibold' : ''}`
            }
            onClick={closeMenu}
          >
            Home
          </NavLink>
          <NavLink 
            to="/about" 
            className={({ isActive }) => 
              `text-white text-2xl hover:text-space-accent transition-colors ${isActive ? 'font-semibold' : ''}`
            }
            onClick={closeMenu}
          >
            About
          </NavLink>
          <NavLink 
            to="/books" 
            className={({ isActive }) => 
              `text-white text-2xl hover:text-space-accent transition-colors ${isActive ? 'font-semibold' : ''}`
            }
            onClick={closeMenu}
          >
            Books
          </NavLink>
          <NavLink 
            to="/blog" 
            className={({ isActive }) => 
              `text-white text-2xl hover:text-space-accent transition-colors ${isActive ? 'font-semibold' : ''}`
            }
            onClick={closeMenu}
          >
            Blog
          </NavLink>
          <NavLink 
            to="/contact" 
            className={({ isActive }) => 
              `text-white text-2xl hover:text-space-accent transition-colors ${isActive ? 'font-semibold' : ''}`
            }
            onClick={closeMenu}
          >
            Contact
          </NavLink>
        </div>
      </div>
    </header>
  );
};

export default Header;
