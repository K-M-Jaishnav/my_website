import React from 'react';
import { motion } from 'framer-motion';
import { Star, BookOpen, DownloadCloud, ShoppingCart } from 'lucide-react';

const Books = () => {
  const books = [
    {
      id: 1,
      title: "Advanced Aerodynamics: Principles and Applications",
      cover: "https://images.pexels.com/photos/2156/sky-earth-space-working.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
      year: "2022",
      publisher: "Cambridge University Press",
      pages: 512,
      rating: 4.8,
      description: "A comprehensive guide to modern aerodynamic principles with practical applications for engineers and researchers.",
      longDescription: `This extensive textbook provides a thorough understanding of advanced aerodynamic concepts and their real-world applications. From fundamental fluid dynamics principles to cutting-edge computational methods, this book covers the entire spectrum of modern aerodynamics.

The book includes:
• Detailed explanations of boundary layer theory
• Comprehensive coverage of compressible and incompressible flows
• In-depth analysis of wing design and optimization
• Case studies from actual aerospace engineering projects
• Practical examples with Python code for numerical simulations

Ideal for graduate students, researchers, and practicing engineers, this book bridges the gap between theoretical foundations and practical implementation in aerospace engineering.`,
      reviews: [
        { name: "Dr. Emily Chen", institution: "Stanford University", comment: "An excellent resource for both teaching and research. The numerical examples are particularly valuable." },
        { name: "Prof. Mark Johnson", institution: "MIT", comment: "One of the most comprehensive texts on aerodynamics I've encountered. Highly recommended for graduate-level courses." }
      ]
    },
    {
      id: 2,
      title: "Computational Fluid Dynamics with Python",
      cover: "https://images.pexels.com/photos/41006/satellite-soyuz-spaceship-space-station-41006.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
      year: "2020",
      publisher: "Springer Science",
      pages: 486,
      rating: 4.7,
      description: "Learn how to model and simulate complex fluid dynamics using Python for aerospace applications.",
      longDescription: `This practical guide walks readers through the implementation of numerical methods for fluid flow simulation using Python. From basic heat transfer to complex turbulence models, this book provides a hands-on approach to computational fluid dynamics.

The book covers:
• Fundamentals of computational fluid dynamics
• Finite difference, finite volume, and finite element methods
• Turbulence modeling approaches
• Grid generation and mesh refinement techniques
• Parallel computing for large-scale simulations
• Complete Python code examples with step-by-step explanations

Whether you're a student learning CFD for the first time or an experienced engineer looking to leverage Python for your simulations, this book provides the tools and knowledge needed to tackle complex fluid dynamics problems.`,
      reviews: [
        { name: "Dr. Sarah Williams", institution: "NASA Ames Research Center", comment: "The Python implementation examples are incredibly valuable. I recommend this to all our new researchers." },
        { name: "Dr. James Li", institution: "Boeing Research", comment: "A perfect balance of theory and practical code examples. The turbulence modeling section is particularly well done." }
      ]
    },
    {
      id: 3,
      title: "The Future of Aerospace Engineering",
      cover: "https://images.pexels.com/photos/39896/space-station-moon-landing-apollo-15-james-irwin-39896.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
      year: "2018",
      publisher: "Oxford University Press",
      pages: 394,
      rating: 4.6,
      description: "Exploring cutting-edge technologies and methodologies that will shape the future of aerospace engineering.",
      longDescription: `This forward-looking book explores the emerging technologies and methodologies that will define the next generation of aerospace engineering. Covering everything from advanced materials to AI-driven design, this book provides a glimpse into the future of flight and space exploration.

Topics include:
• Next-generation propulsion systems including electric and hybrid propulsion
• Advanced materials and manufacturing techniques
• Autonomous systems and AI in aerospace applications
• Space exploration challenges and solutions
• Sustainable aviation technologies
• Urban air mobility and its infrastructure requirements

Written for professionals, researchers, and enthusiasts alike, this book combines technical insight with accessible explanations of how these technologies will transform our approach to aerospace engineering in the coming decades.`,
      reviews: [
        { name: "Dr. Robert Davis", institution: "European Space Agency", comment: "A visionary work that accurately predicted many of the developments we're now seeing in the aerospace industry." },
        { name: "Prof. Maria Garcia", institution: "Caltech", comment: "I assign chapters from this book in my graduate seminar on emerging aerospace technologies. The students find it both informative and inspiring." }
      ]
    }
  ];

  return (
    <>
      {/* Hero Section */}
      <section className="pt-32 pb-20 bg-gradient-to-b from-space-navy to-space-dark text-white">
        <div className="container-custom">
          <div className="max-w-3xl mx-auto text-center">
            <h1 className="mb-6">My Books</h1>
            <p className="text-xl text-gray-300">
              Comprehensive resources on aerospace engineering, aerodynamics, and 
              computational methods using Python and Django.
            </p>
          </div>
        </div>
      </section>
      
      {/* Books Section */}
      <section className="py-20 bg-white">
        <div className="container-custom">
          {books.map((book, index) => (
            <motion.div 
              key={book.id}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.7, delay: index * 0.1 }}
              className={`flex flex-col lg:flex-row gap-8 mb-20 ${
                index % 2 !== 0 ? 'lg:flex-row-reverse' : ''
              }`}
            >
              <div className="lg:w-2/5">
                <div className="rounded-lg overflow-hidden shadow-lg h-full">
                  <img 
                    src={book.cover} 
                    alt={book.title} 
                    className="w-full h-full object-cover"
                  />
                </div>
              </div>
              
              <div className="lg:w-3/5">
                <p className="text-space-accent font-medium mb-2">{book.year} • {book.publisher}</p>
                <h2 className="text-space-dark mb-3">{book.title}</h2>
                
                <div className="flex items-center mb-4">
                  <div className="flex items-center mr-4">
                    <Star className="w-5 h-5 text-yellow-500 fill-current" />
                    <span className="ml-1 font-medium">{book.rating}/5</span>
                  </div>
                  <div className="flex items-center mr-4">
                    <BookOpen className="w-5 h-5 text-space-dark" />
                    <span className="ml-1">{book.pages} pages</span>
                  </div>
                </div>
                
                <div className="space-y-4 mb-6">
                  <p className="text-gray-700 whitespace-pre-line">{book.longDescription}</p>
                </div>
                
                <div className="mb-8">
                  <h3 className="text-xl font-bold mb-4">What Others Are Saying</h3>
                  <div className="space-y-4">
                    {book.reviews.map((review, i) => (
                      <div key={i} className="bg-space-light p-4 rounded-lg">
                        <p className="italic text-gray-700 mb-2">"{review.comment}"</p>
                        <p className="text-space-dark font-medium">{review.name}, {review.institution}</p>
                      </div>
                    ))}
                  </div>
                </div>
                
                <div className="flex flex-wrap gap-4">
                  <a href="#" className="btn-primary flex items-center">
                    <ShoppingCart className="mr-2 w-5 h-5" /> Purchase Book
                  </a>
                  <a href="#" className="btn-secondary flex items-center">
                    <DownloadCloud className="mr-2 w-5 h-5" /> Sample Chapter
                  </a>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </section>
      
      {/* Call to Action */}
      <section className="py-20 bg-space-light">
        <div className="container-custom text-center">
          <h2 className="text-space-dark mb-6">Interested in a Signed Copy?</h2>
          <p className="text-gray-700 max-w-2xl mx-auto mb-8">
            Contact me directly to request a signed copy of any of my books. 
            I'm also available for book talks, workshops, and guest lectures.
          </p>
          <a href="/contact" className="btn-primary">Get in Touch</a>
        </div>
      </section>
    </>
  );
};

export default Books;
