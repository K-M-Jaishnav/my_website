import React from 'react';
import { motion } from 'framer-motion';
import { ArrowRight } from 'lucide-react';
import { Link } from 'react-router-dom';

const books = [
  {
    id: 1,
    title: "Advanced Aerodynamics: Principles and Applications",
    cover: "https://images.pexels.com/photos/2156/sky-earth-space-working.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    year: "2022",
    description: "A comprehensive guide to modern aerodynamic principles with practical applications for engineers and researchers."
  },
  {
    id: 2,
    title: "Computational Fluid Dynamics with Python",
    cover: "https://images.pexels.com/photos/41006/satellite-soyuz-spaceship-space-station-41006.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    year: "2020",
    description: "Learn how to model and simulate complex fluid dynamics using Python for aerospace applications."
  },
  {
    id: 3,
    title: "The Future of Aerospace Engineering",
    cover: "https://images.pexels.com/photos/39896/space-station-moon-landing-apollo-15-james-irwin-39896.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    year: "2018",
    description: "Exploring cutting-edge technologies and methodologies that will shape the future of aerospace engineering."
  }
];

const FeaturedBooks = () => {
  const container = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
      transition: {
        staggerChildren: 0.2
      }
    }
  };
  
  const item = {
    hidden: { y: 20, opacity: 0 },
    show: { y: 0, opacity: 1, transition: { duration: 0.6 } }
  };
  
  return (
    <section id="books" className="section bg-white">
      <div className="container-custom">
        <div className="text-center mb-12">
          <p className="text-space-accent font-medium mb-2">PUBLISHED WORKS</p>
          <h2 className="text-space-dark mb-4">Featured Books</h2>
          <p className="max-w-2xl mx-auto text-gray-600">
            Discover my published works on aerospace engineering, aerodynamics, and 
            computational methods using Python and Django.
          </p>
        </div>
        
        <motion.div 
          className="grid grid-cols-1 md:grid-cols-3 gap-8"
          variants={container}
          initial="hidden"
          whileInView="show"
          viewport={{ once: true, amount: 0.3 }}
        >
          {books.map((book) => (
            <motion.div 
              key={book.id} 
              className="bg-gray-50 rounded-lg overflow-hidden shadow-md hover:shadow-xl transition-shadow duration-300"
              variants={item}
            >
              <div className="h-64 overflow-hidden">
                <img 
                  src={book.cover} 
                  alt={book.title} 
                  className="w-full h-full object-cover transition-transform duration-500 hover:scale-105"
                />
              </div>
              <div className="p-6">
                <p className="text-space-accent font-medium mb-2">{book.year}</p>
                <h3 className="text-xl font-bold mb-3">{book.title}</h3>
                <p className="text-gray-600 mb-4">{book.description}</p>
                <Link to="/books" className="text-space-dark font-medium inline-flex items-center hover:text-space-accent transition-colors">
                  Read More <ArrowRight className="w-4 h-4 ml-1" />
                </Link>
              </div>
            </motion.div>
          ))}
        </motion.div>
        
        <div className="text-center mt-12">
          <Link to="/books" className="btn-primary">
            View All Books
          </Link>
        </div>
      </div>
    </section>
  );
};

export default FeaturedBooks;
