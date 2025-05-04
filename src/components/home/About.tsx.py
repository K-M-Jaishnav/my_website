import React from 'react';
import { motion } from 'framer-motion';
import { Award, BookOpen, FileText, Code } from 'lucide-react';

const Stats = [
  { icon: <BookOpen className="w-8 h-8 text-space-accent" />, value: "3", label: "Published Books" },
  { icon: <FileText className="w-8 h-8 text-space-accent" />, value: "45+", label: "Research Papers" },
  { icon: <Code className="w-8 h-8 text-space-accent" />, value: "12", label: "Software Projects" },
  { icon: <Award className="w-8 h-8 text-space-accent" />, value: "15+", label: "Years Experience" }
];

const About = () => {
  return (
    <section id="about" className="section bg-gray-50">
      <div className="container-custom">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8 }}
          >
            <p className="text-space-accent font-medium mb-2">ABOUT ME</p>
            <h2 className="text-space-dark mb-6">Pioneering Aerospace Research & Development</h2>
            
            <div className="space-y-4 text-gray-700 mb-8">
              <p>
                With over 15 years of experience in aerospace engineering and aerophysics, 
                I've dedicated my career to pushing the boundaries of what's possible in 
                flight and space exploration.
              </p>
              <p>
                My research focuses on advanced fluid dynamics, computational modeling, 
                and innovative aerospace technologies. I've published extensively in 
                prestigious journals and have been invited to speak at conferences worldwide.
              </p>
              <p>
                As an author, I've written three comprehensive books that bridge the gap 
                between theoretical aerophysics and practical applications using Python 
                and Django for computational modeling and data analysis.
              </p>
            </div>
            
            <motion.a 
              href="/about" 
              className="btn-primary"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              More About Me
            </motion.a>
          </motion.div>
          
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="grid grid-cols-2 gap-6"
          >
            {Stats.map((stat, index) => (
              <div 
                key={index} 
                className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow"
              >
                <div className="mb-3">{stat.icon}</div>
                <div className="font-serif font-bold text-4xl text-space-dark mb-1">{stat.value}</div>
                <div className="text-gray-600">{stat.label}</div>
              </div>
            ))}
          </motion.div>
        </div>
      </div>
    </section>
  );
};

export default About;
