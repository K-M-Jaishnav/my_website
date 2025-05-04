import React from 'react';
import { motion } from 'framer-motion';
import { Award, BookOpen, FileText, Rocket, Plane, Satellite } from 'lucide-react';

const About = () => {
  return (
    <>
      {/* Hero Section */}
      <section className="pt-32 pb-20 bg-gradient-to-b from-space-navy to-space-dark text-white">
        <div className="container-custom">
          <div className="max-w-3xl mx-auto text-center">
            <h1 className="mb-6">About Me</h1>
            <p className="text-xl text-gray-300">
              Aerospace engineer, aerophysics researcher, and author with a passion for
              pushing the boundaries of flight and space exploration.
            </p>
          </div>
        </div>
      </section>
      
      {/* Profile Section */}
      <section className="py-20 bg-white">
        <div className="container-custom">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.8 }}
              className="space-y-6"
            >
              <div>
                <p className="text-space-accent font-medium mb-2">MY BACKGROUND</p>
                <h2 className="text-space-dark mb-4">Dr. John Smith</h2>
                <p className="text-gray-700">Ph.D. in Aerospace Engineering, MIT</p>
              </div>
              
              <div className="space-y-4 text-gray-700">
                <p>
                  I've dedicated my career to advancing the field of aerospace engineering through
                  cutting-edge research, innovative computational methods, and knowledge sharing.
                </p>
                <p>
                  After earning my Ph.D. from MIT, I worked on several key research projects at NASA and
                  private aerospace companies, focusing on computational fluid dynamics and aerodynamic
                  optimization.
                </p>
                <p>
                  My passion for teaching led me to academia, where I've mentored dozens of graduate
                  students and published extensively in peer-reviewed journals. My three books on
                  aerospace engineering and computational methods have been adopted by universities worldwide.
                </p>
              </div>
              
              <div className="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4">
                <a href="#publications" className="btn-primary">View Publications</a>
                <a href="/contact" className="btn-secondary">Contact Me</a>
              </div>
            </motion.div>
            
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.8, delay: 0.2 }}
              className="bg-space-light p-8 rounded-lg shadow-lg"
            >
              <div className="grid grid-cols-2 gap-6">
                <div className="bg-white p-6 rounded-lg shadow-md">
                  <BookOpen className="w-8 h-8 text-space-accent mb-3" />
                  <h3 className="font-bold text-xl mb-2">Education</h3>
                  <ul className="space-y-2 text-gray-700">
                    <li>Ph.D. Aerospace Engineering, MIT</li>
                    <li>M.S. Mechanical Engineering, Stanford</li>
                    <li>B.S. Physics, Caltech</li>
                  </ul>
                </div>
                
                <div className="bg-white p-6 rounded-lg shadow-md">
                  <Award className="w-8 h-8 text-space-accent mb-3" />
                  <h3 className="font-bold text-xl mb-2">Awards</h3>
                  <ul className="space-y-2 text-gray-700">
                    <li>NASA Exceptional Scientific Achievement</li>
                    <li>AIAA Best Paper Award</li>
                    <li>Dean's Award for Excellence in Teaching</li>
                  </ul>
                </div>
                
                <div className="bg-white p-6 rounded-lg shadow-md">
                  <FileText className="w-8 h-8 text-space-accent mb-3" />
                  <h3 className="font-bold text-xl mb-2">Research</h3>
                  <ul className="space-y-2 text-gray-700">
                    <li>Computational Fluid Dynamics</li>
                    <li>Advanced Aerodynamics</li>
                    <li>Machine Learning in Aerospace</li>
                  </ul>
                </div>
                
                <div className="bg-white p-6 rounded-lg shadow-md">
                  <Rocket className="w-8 h-8 text-space-accent mb-3" />
                  <h3 className="font-bold text-xl mb-2">Experience</h3>
                  <ul className="space-y-2 text-gray-700">
                    <li>Professor, Aerospace University</li>
                    <li>Senior Researcher, NASA</li>
                    <li>Consultant, SpaceX</li>
                  </ul>
                </div>
              </div>
            </motion.div>
          </div>
        </div>
      </section>
      
      {/* Expertise Section */}
      <section id="expertise" className="py-20 bg-space-light">
        <div className="container-custom">
          <div className="text-center mb-16">
            <p className="text-space-accent font-medium mb-2">AREAS OF EXPERTISE</p>
            <h2 className="text-space-dark mb-4">My Specializations</h2>
            <p className="max-w-2xl mx-auto text-gray-600">
              I've spent my career developing expertise in several key areas of aerospace 
              engineering and computational physics.
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5 }}
              className="bg-white p-8 rounded-lg shadow-md"
            >
              <Plane className="w-12 h-12 text-space-accent mb-6" />
              <h3 className="text-xl font-bold mb-4">Advanced Aerodynamics</h3>
              <p className="text-gray-600 mb-4">
                Specializing in computational and experimental approaches to complex 
                aerodynamic systems, including supersonic and hypersonic flow regimes.
              </p>
              <ul className="space-y-2 text-gray-700">
                <li>• Boundary layer control strategies</li>
                <li>• Vortex dynamics and manipulation</li>
                <li>• Low Reynolds number aerodynamics</li>
                <li>• Wing design optimization</li>
              </ul>
            </motion.div>
            
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: 0.2 }}
              className="bg-white p-8 rounded-lg shadow-md"
            >
              <FileText className="w-12 h-12 text-space-accent mb-6" />
              <h3 className="text-xl font-bold mb-4">Computational Methods</h3>
              <p className="text-gray-600 mb-4">
                Developing and applying advanced computational tools for fluid dynamics, 
                structural analysis, and multiphysics simulations.
              </p>
              <ul className="space-y-2 text-gray-700">
                <li>• Python for scientific computing</li>
                <li>• Machine learning for flow prediction</li>
                <li>• Large-scale parallel computing</li>
                <li>• Uncertainty quantification</li>
              </ul>
            </motion.div>
            
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: 0.4 }}
              className="bg-white p-8 rounded-lg shadow-md"
            >
              <Satellite className="w-12 h-12 text-space-accent mb-6" />
              <h3 className="text-xl font-bold mb-4">Space Systems</h3>
              <p className="text-gray-600 mb-4">
                Researching innovative approaches to spacecraft design, propulsion, 
                and orbital mechanics for future space exploration.
              </p>
              <ul className="space-y-2 text-gray-700">
                <li>• Electric propulsion systems</li>
                <li>• Thermal management in space</li>
                <li>• Reentry vehicle design</li>
                <li>• Orbital trajectory optimization</li>
              </ul>
            </motion.div>
          </div>
        </div>
      </section>
      
      {/* Publications Section */}
      <section id="publications" className="py-20 bg-white">
        <div className="container-custom">
          <div className="text-center mb-16">
            <p className="text-space-accent font-medium mb-2">RESEARCH & WRITING</p>
            <h2 className="text-space-dark mb-4">Selected Publications</h2>
            <p className="max-w-2xl mx-auto text-gray-600">
              A selection of my most significant publications in academic journals, conferences, 
              and popular science platforms.
            </p>
          </div>
          
          <div className="space-y-6">
            <div className="border-l-4 border-space-accent pl-6 py-2">
              <h3 className="text-xl font-bold mb-2">Advanced Aerodynamics: Principles and Applications</h3>
              <p className="text-gray-700 mb-1">Cambridge University Press, 2022</p>
              <p className="text-gray-600">
                A comprehensive textbook covering modern aerodynamic theory and practical applications 
                for engineers, researchers, and graduate students.
              </p>
            </div>
            
            <div className="border-l-4 border-space-accent pl-6 py-2">
              <h3 className="text-xl font-bold mb-2">Computational Fluid Dynamics with Python</h3>
              <p className="text-gray-700 mb-1">Springer Science, 2020</p>
              <p className="text-gray-600">
                A practical guide to implementing numerical methods for fluid flow simulation using 
                Python, with applications in aerospace engineering.
              </p>
            </div>
            
            <div className="border-l-4 border-space-accent pl-6 py-2">
              <h3 className="text-xl font-bold mb-2">The Future of Aerospace Engineering</h3>
              <p className="text-gray-700 mb-1">Oxford University Press, 2018</p>
              <p className="text-gray-600">
                An exploration of emerging technologies and methodologies in aerospace engineering, 
                with case studies and future projections.
              </p>
            </div>
            
            <div className="border-l-4 border-space-light pl-6 py-2">
              <h3 className="text-xl font-bold mb-2">Journal Articles</h3>
              <ul className="space-y-4 mt-4">
                <li>
                  <p className="font-medium">Optimization of Wing Design for Supersonic Aircraft Using Machine Learning</p>
                  <p className="text-gray-600">Journal of Aircraft, 2023</p>
                </li>
                <li>
                  <p className="font-medium">Novel Approaches to Boundary Layer Control in High-Speed Flight</p>
                  <p className="text-gray-600">AIAA Journal, 2022</p>
                </li>
                <li>
                  <p className="font-medium">Computational Methods for Hypersonic Flow Simulation</p>
                  <p className="text-gray-600">Journal of Computational Physics, 2021</p>
                </li>
                <li>
                  <p className="font-medium">Vortex Dynamics in Aircraft Wake Turbulence</p>
                  <p className="text-gray-600">Physics of Fluids, 2020</p>
                </li>
              </ul>
            </div>
          </div>
          
          <div className="text-center mt-12">
            <a href="/contact" className="btn-primary">
              Request Complete CV
            </a>
          </div>
        </div>
      </section>
    </>
  );
};

export default About;
