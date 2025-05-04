import React from 'react';
import { Link } from 'react-router-dom';
import { 
  Rocket, 
  Mail, 
  Twitter, 
  Linkedin, 
  Github, 
  ArrowRight 
} from 'lucide-react';

const Footer = () => {
  const currentYear = new Date().getFullYear();
  
  return (
    <footer className="bg-space-navy text-white">
      <div className="container-custom pt-16 pb-6">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-12">
          <div className="col-span-1 md:col-span-2">
            <Link to="/" className="flex items-center mb-4">
              <Rocket className="w-6 h-6 text-space-accent mr-2" />
              <span className="font-serif font-bold text-xl">K M Jaishnav</span>
            </Link>
            <p className="mb-6 text-gray-300 max-w-md">
              Interested in aerospace engineering and aerophysics with over 5 years of experience.
              Author of 3 books and some theories on Quantum Mechanics,Extra-Terrestrial life, Aerophysics and 
              aerospace technology.
            </p>
            <div className="flex space-x-4">
              <a href="#" aria-label="Twitter" className="text-gray-300 hover:text-space-accent transition-colors">
                <Twitter className="w-5 h-5" />
              </a>
              <a href="#" aria-label="LinkedIn" className="text-gray-300 hover:text-space-accent transition-colors">
                <Linkedin className="w-5 h-5" />
              </a>
              <a href="#" aria-label="Github" className="text-gray-300 hover:text-space-accent transition-colors">
                <Github className="w-5 h-5" />
              </a>
              <a href="jaiaerospace08@example.com" aria-label="Email" className="text-gray-300 hover:text-space-accent transition-colors">
                <Mail className="w-5 h-5" />
              </a>
            </div>
          </div>
          
          <div>
            <h4 className="font-serif text-lg font-bold mb-4">Quick Links</h4>
            <ul className="space-y-2">
              <li>
                <Link to="/" className="text-gray-300 hover:text-space-accent transition-colors flex items-center">
                  <ArrowRight className="w-4 h-4 mr-2" />
                  Home
                </Link>
              </li>
              <li>
                <Link to="/about" className="text-gray-300 hover:text-space-accent transition-colors flex items-center">
                  <ArrowRight className="w-4 h-4 mr-2" />
                  About
                </Link>
              </li>
              <li>
                <Link to="/books" className="text-gray-300 hover:text-space-accent transition-colors flex items-center">
                  <ArrowRight className="w-4 h-4 mr-2" />
                  Books
                </Link>
              </li>
              <li>
                <Link to="/blog" className="text-gray-300 hover:text-space-accent transition-colors flex items-center">
                  <ArrowRight className="w-4 h-4 mr-2" />
                  Blog
                </Link>
              </li>
              <li>
                <Link to="/contact" className="text-gray-300 hover:text-space-accent transition-colors flex items-center">
                  <ArrowRight className="w-4 h-4 mr-2" />
                  Contact
                </Link>
              </li>
            </ul>
          </div>
          
          <div>
            <h4 className="font-serif text-lg font-bold mb-4">Contact</h4>
            <address className="not-italic text-gray-300 space-y-2">
              <p>Senthil Public School</p>
              <p>Tamilnadu, India</p>
              <p>Salem City,636 006</p>
              <p className="mt-4">
                <a href="jaiaerospace08@gmail.com" className="hover:text-space-accent transition-colors">
                  jaiaerospace08@gmail.com
                </a>
              </p>
              <p>
                <a href="tel:+91 7598972493" className="hover:text-space-accent transition-colors">
                  +91 7598972493
                </a>
              </p>
            </address>
          </div>
        </div>
        
        <div className="border-t border-gray-700 pt-6">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <p className="text-sm text-gray-400 mb-4 md:mb-0">
              &copy; {currentYear} Dr. Aerospace. All rights reserved.
            </p>
            <div className="text-sm text-gray-400 flex space-x-4">
              <a href="#" className="hover:text-space-accent transition-colors">Privacy Policy</a>
              <a href="#" className="hover:text-space-accent transition-colors">Terms of Service</a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
